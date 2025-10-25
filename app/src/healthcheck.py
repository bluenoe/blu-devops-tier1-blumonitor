"""
EN: Healthcheck that ensures LOG_FILE exists and was modified recently.
VI: Kiem tra suc khoe — file log ton tai va duoc cap nhat gan day.
"""
import os
import sys
import time


LOG_FILE = os.environ.get("LOG_FILE", "/app/logs/app.log")
WINDOW = int(os.environ.get("HEALTH_WINDOW_SEC", "120"))


try:
st = os.stat(LOG_FILE)
except FileNotFoundError:
sys.exit(1)


age = time.time() - st.st_mtime
if age > WINDOW or st.st_size == 0:
sys.exit(1)


print("ok")