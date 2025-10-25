#!/usr/bin/env bash
# EN: Quick helpers to observe logs/resources.
# VI: Script nhanh de xem log va tai nguyen.
set -euo pipefail
cmd=${1:-help}
case "$cmd" in
logs)
echo "Tailing service logs (docker compose logs -f blumonitor_app)"
docker compose logs -f --tail=100 blumonitor_app
;;
tail)
echo "Exec into container and tail the raw file: /app/logs/app.log"
docker exec -it blumonitor_app sh -c 'tail -n 100 -f /app/logs/app.log'
;;
stats)
echo "Live container stats"
docker stats blumonitor_app
;;
*)
echo "Usage: $0 {logs|tail|stats}"; exit 1
;;
esac