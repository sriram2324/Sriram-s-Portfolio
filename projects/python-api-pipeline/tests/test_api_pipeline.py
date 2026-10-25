import sys
from pathlib import Path
from unittest.mock import patch, MagicMock
import pytest
import sqlite3

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.api_pipeline import APIDataPipeline

@pytest.fixture
def memory_pipeline():
    return APIDataPipeline(db_path=":memory:", timeout=5, max_retries=2)

def test_database_initialization(memory_pipeline):
    conn = memory_pipeline._get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='api_posts';")
    assert cursor.fetchone() is not None

def test_validate_and_normalize(memory_pipeline):
    raw_payload = [
        {"userId": 1, "id": 101, "title": " Test Title ", "body": " Test Body Content "},
        {"invalidKey": "Bad Item"}  # Malformed item should be discarded
    ]
    df = memory_pipeline.validate_and_normalize(raw_payload)

    assert len(df) == 1
    assert df.iloc[0]['id'] == 101
    assert df.iloc[0]['user_id'] == 1
    assert df.iloc[0]['title'] == "Test Title"

def test_store_records(memory_pipeline):
    raw_payload = [
        {"userId": 1, "id": 101, "title": "Title 1", "body": "Body 1"},
        {"userId": 2, "id": 102, "title": "Title 2", "body": "Body 2"}
    ]
    df = memory_pipeline.validate_and_normalize(raw_payload)
    count = memory_pipeline.store_records(df)

    assert count == 2
    conn = memory_pipeline._get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM api_posts;")
    assert cursor.fetchone()[0] == 2

@patch("requests.get")
def test_mocked_fetch_success(mock_get, memory_pipeline):
    mock_resp = MagicMock()
    mock_resp.status_code = 200
    mock_resp.json.return_value = [{"userId": 1, "id": 1, "title": "Mock", "body": "Text"}]
    mock_get.return_value = mock_resp

    items = memory_pipeline.fetch_page(page=1, limit=1)
    assert len(items) == 1
    assert items[0]['id'] == 1
