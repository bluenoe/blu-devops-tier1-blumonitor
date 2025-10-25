"""
EN: BluMonitor — simple log generator with basic rotation (size or time).
VI: BluMonitor — sinh log don gian, co quay vong log theo kich thuoc hoac theo thoi gian.


Environment variables:
LOG_DIR=/app/logs
LOG_FILE=/app/logs/app.log
ROTATE_BY=size|time
MAX_BYTES=1000000
BACKUP_COUNT=5
ITERATIONS=0 (0 = infinite loop; >0 = number of log events then exit)
LOG_INTERVAL_SEC=1


This script writes mixed INFO/WARNING/ERROR lines continuously.
"""
from __future__ import annotations
import logging
import os
import random
import sys
import time
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler


LOG_DIR = os.environ.get("LOG_DIR", "/app/logs")
LOG_FILE = os.environ.get("LOG_FILE", os.path.join(LOG_DIR, "app.log"))
ROTATE_BY = os.environ.get("ROTATE_BY", "size").lower() # "size" or "time"
MAX_BYTES = int(os.environ.get("MAX_BYTES", "1000000"))
BACKUP_COUNT = int(os.environ.get("BACKUP_COUNT", "5"))
ITERATIONS = int(os.environ.get("ITERATIONS", "0")) # 0 → infinite
LOG_INTERVAL_SEC = float(os.environ.get("LOG_INTERVAL_SEC", "1"))


os.makedirs(LOG_DIR, exist_ok=True)


logger = logging.getLogger("blumonitor")
logger.setLevel(logging.INFO)


# File handler with rotation
if ROTATE_BY == "time":
handler = TimedRotatingFileHandler(LOG_FILE, when="midnight", backupCount=BACKUP_COUNT, encoding="utf-8")
else:
handler = RotatingFileHandler(LOG_FILE, maxBytes=MAX_BYTES, backupCount=BACKUP_COUNT, encoding="utf-8")


fmt = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
handler.setFormatter(fmt)
logger.addHandler(handler)
main()