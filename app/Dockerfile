# EN: Stage 1 — Create virtualenv and install deps (even if empty), caching-friendly
# VI: Buoc 1 — Tao virtualenv cai deps de cache tot hon
FROM python:3.12-slim AS builder


ENV VENV_PATH=/opt/venv
RUN python -m venv ${VENV_PATH} \
&& ${VENV_PATH}/bin/pip install --upgrade pip


WORKDIR /app
COPY requirements.txt ./
RUN ${VENV_PATH}/bin/pip install -r requirements.txt || true


# EN: Stage 2 — Minimal runtime image, non-root user, volume for logs, healthcheck
# VI: Buoc 2 — Image chay nhe, dung user khong phai root, mount volume log, them healthcheck
FROM python:3.12-slim AS runtime


ENV VENV_PATH=/opt/venv \
PATH=/opt/venv/bin:$PATH \
LOG_DIR=/app/logs \
LOG_FILE=/app/logs/app.log \
ROTATE_BY=size \
MAX_BYTES=1000000 \
BACKUP_COUNT=5 \
ITERATIONS=0 \
LOG_INTERVAL_SEC=1 \
HEALTH_WINDOW_SEC=120


# Create non-root user
RUN useradd -m -u 1001 blu \
&& mkdir -p /app/src ${LOG_DIR} \
&& chown -R blu:blu /app


COPY --from=builder /opt/venv /opt/venv


WORKDIR /app
COPY src ./src
RUN chown -R blu:blu /app


USER blu
VOLUME ["/app/logs"]


# Healthcheck: file must be recently updated
HEALTHCHECK --interval=15s --timeout=5s --retries=5 CMD python -u /app/src/healthcheck.py || exit 1


CMD ["python", "-u", "/app/src/main.py"]