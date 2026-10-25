"""Master test runner for all Python projects in the portfolio."""

import subprocess
import sys
from pathlib import Path

PROJECT_DIRS = [
    Path("projects/personal-finance-dashboard"),
    Path("projects/retail-sales-analytics"),
    Path("projects/customer-churn-prediction"),
    Path("projects/ecommerce-sales-analytics"),
    Path("projects/data-quality-pipeline"),
    Path("projects/python-api-pipeline"),
    Path("projects/business-report-automation"),
    Path("project 1"),
]

def run_tests():
    print("=" * 70)
    print("RUNNING AUTOMATED PYTEST SUITES ACROSS ALL PORTFOLIO PROJECTS")
    print("=" * 70 + "\n")

    total_projects = len(PROJECT_DIRS)
    passed_projects = 0

    for p in PROJECT_DIRS:
        if not p.exists():
            print(f"[SKIPPED] {p} does not exist.")
            continue

        test_dir = p / "tests"
        if not test_dir.exists():
            print(f"[SKIPPED] {p}/tests does not exist.")
            continue

        print(f"[TESTING] {p.name} ...")
        cmd = [sys.executable, "-m", "pytest", "-q", "tests"]
        res = subprocess.run(cmd, cwd=str(p), capture_output=True, text=True)

        if res.returncode == 0:
            print(f"  [PASS] {p.name} -> {res.stdout.strip()}")
            passed_projects += 1
        else:
            print(f"  [FAIL] {p.name}")
            print(f"     Output: {res.stdout.strip()}")
            print(f"     Error: {res.stderr.strip()}")

    print("\n" + "=" * 70)
    print(f"RESULT: {passed_projects}/{total_projects} PROJECTS PASSED AUTOMATED TESTS")
    print("=" * 70)

    if passed_projects == total_projects:
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == "__main__":
    run_tests()
