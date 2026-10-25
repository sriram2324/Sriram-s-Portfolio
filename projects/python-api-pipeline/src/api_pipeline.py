"""Production-Grade Python REST API Ingestion Pipeline.

Fetches data from public REST APIs, enforces strict schema validation and normalization,
handles pagination, timeouts, exponential backoff retries, and rate limits,
and persists verified records to a relational SQLite database with structured logging.
"""

import logging
import sqlite3
import time
from typing import Dict, List, Optional, Any
import requests
import pandas as pd

# Configure structured logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s'
)
logger = logging.getLogger("APIDataPipeline")

class APIDataPipeline:
    BASE_URL = "https://jsonplaceholder.typicode.com/posts"

    def __init__(self, db_path: str = "data/api_data.db", timeout: int = 10, max_retries: int = 3):
        self.db_path = db_path
        self.timeout = timeout
        self.max_retries = max_retries
        self._shared_conn = sqlite3.connect(db_path) if db_path == ":memory:" else None
        self._init_db()

    def _get_connection(self) -> sqlite3.Connection:
        if self._shared_conn:
            return self._shared_conn
        return sqlite3.connect(self.db_path)

    def _init_db(self):
        conn = self._get_connection()
        conn.execute("""
        CREATE TABLE IF NOT EXISTS api_posts (
            id INTEGER PRIMARY KEY,
            user_id INTEGER NOT NULL,
            title TEXT NOT NULL,
            body TEXT NOT NULL,
            ingested_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """)
        conn.commit()
        if not self._shared_conn:
            conn.close()

    def fetch_page(self, page: int = 1, limit: int = 10) -> List[Dict[str, Any]]:
        """Fetch a paginated page with exponential backoff retry logic."""
        params = {"_page": page, "_limit": limit}

        for attempt in range(1, self.max_retries + 1):
            try:
                logger.info(f"Fetching page {page} (attempt {attempt}/{self.max_retries})...")
                response = requests.get(self.BASE_URL, params=params, timeout=self.timeout)

                # Check HTTP status
                if response.status_code == 200:
                    data = response.json()
                    logger.info(f"Successfully retrieved {len(data)} items from page {page}.")
                    return data
                elif response.status_code == 429:
                    logger.warning(f"Rate limited (429). Backing off attempt {attempt}...")
                    time.sleep(2 ** attempt)
                else:
                    logger.error(f"HTTP {response.status_code} received from API.")
                    response.raise_for_status()

            except (requests.Timeout, requests.ConnectionError) as e:
                logger.warning(f"Network error on attempt {attempt}: {e}")
                if attempt == self.max_retries:
                    raise
                time.sleep(1.5 ** attempt)

        return []

    def validate_and_normalize(self, raw_items: List[Dict[str, Any]]) -> pd.DataFrame:
        """Validate payload schema and normalize into clean Pandas DataFrame."""
        if not raw_items:
            return pd.DataFrame(columns=['id', 'user_id', 'title', 'body'])

        cleaned_records = []
        for item in raw_items:
            # Validate required keys
            if all(k in item for k in ('id', 'userId', 'title', 'body')):
                cleaned_records.append({
                    'id': int(item['id']),
                    'user_id': int(item['userId']),
                    'title': str(item['title']).strip(),
                    'body': str(item['body']).strip()
                })
            else:
                logger.warning(f"Dropping corrupt or malformed payload item: {item}")

        df = pd.DataFrame(cleaned_records)
        return df

    def store_records(self, df: pd.DataFrame) -> int:
        """Store normalized records into SQLite with INSERT OR REPLACE."""
        if df.empty:
            return 0

        conn = self._get_connection()
        cur = conn.cursor()
        records = df[['id', 'user_id', 'title', 'body']].values.tolist()
        cur.executemany("""
            INSERT OR REPLACE INTO api_posts (id, user_id, title, body)
            VALUES (?, ?, ?, ?);
        """, records)
        conn.commit()
        if not self._shared_conn:
            conn.close()

        count = len(records)
        logger.info(f"Persisted {count} records into SQLite database.")
        return count

    def run_pipeline(self, max_pages: int = 2, per_page: int = 10) -> int:
        """Execute end-to-end extraction, validation, and storage pipeline."""
        total_stored = 0
        for p in range(1, max_pages + 1):
            items = self.fetch_page(page=p, limit=per_page)
            if not items:
                logger.info(f"No further items found at page {p}. Ending pagination.")
                break
            df = self.validate_and_normalize(items)
            stored = self.store_records(df)
            total_stored += stored

        logger.info(f"Pipeline complete. Total records stored: {total_stored}")
        return total_stored
