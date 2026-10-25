"""Automated test runner and guaranteed post-test cleanup script.
Executes pytest with isolated fixtures, cleans any remaining temporary test directories,
and preserves the exact pytest exit code.
"""

from pathlib import Path
import subprocess
import sys

# Ensure src is in Python path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from news_sentiment.cleanup import clean_temp_directory
from news_sentiment.config import TEMP_DIR


def main():
    print("=" * 65)
    print(" NEWS SENTIMENT ANALYZER: TEST & CLEAN RUNNER")
    print("=" * 65)
    print(f"Project root        : {PROJECT_ROOT}")
    print(f"Designated temp dir : {TEMP_DIR}")
    print("-" * 65)

    exit_code = 1
    try:
        # Run pytest via subprocess, capturing exit code
        cmd = [sys.executable, "-m", "pytest", "tests", "-v", "--tb=short"]
        print(f"Executing: {' '.join(cmd)}\n")
        res = subprocess.run(cmd, cwd=str(PROJECT_ROOT))
        exit_code = res.returncode
    except Exception as exc:
        print(f"Error launching test runner: {exc}")
        exit_code = 1
    finally:
        print("\n" + "-" * 65)
        print("Executing post-test isolated temporary artifact cleanup...")
        cleanup_result = clean_temp_directory(temp_dir=TEMP_DIR, allowed_root=PROJECT_ROOT)
        if cleanup_result.get("success"):
            print(f"Cleanup status: SUCCESS (removed {cleanup_result.get('cleaned_files', 0)} temp file(s)/dir(s))")
        else:
            print(f"Cleanup note: {cleanup_result.get('message', cleanup_result.get('error'))}")
        print("=" * 65)

    sys.exit(exit_code)


if __name__ == "__main__":
    main()
