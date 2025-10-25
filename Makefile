# EN: Simple automation for daily flow
# VI: Lenh tat de chay nhanh


.PHONY: build run stop clean logs stats


build:
docker compose build


run:
docker compose up -d


stop:
docker compose down


clean:
docker compose down -v --rmi local


logs:
./scripts/monitor.sh logs


stats:
./scripts/monitor.sh stats