"""
Simple test: run the generator for a few iterations into a temp dir and assert a log file exists and is non-empty.
"""
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


APP_ENTRY = Path(__file__).resolve().parents[1] / "app" / "src" / "main.py"




def test_generates_log_file():
tmp = Path(tempfile.mkdtemp())
try:
env = os.environ.copy()
env.update({
"LOG_DIR": str(tmp),
"LOG_FILE": str(tmp / "app.log"),
"ITERATIONS": "5",
"LOG_INTERVAL_SEC": "0.01",
})
# Run the script directly (no Docker needed for CI unit test)
proc = subprocess.run([sys.executable, str(APP_ENTRY)], env=env, capture_output=True, text=True, timeout=30)
assert proc.returncode == 0
logfile = tmp / "app.log"
assert logfile.exists()
assert logfile.stat().st_size > 0
finally:
shutil.rmtree(tmp)