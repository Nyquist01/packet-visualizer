format:
	uv run ruff format
	uv run ruff check --fix
	uv run ruff check --fix --select I

lint:
	uv run pylint --disable=C,W,R packet_sniffer/
	uv run mypy packet_sniffer/

docker-up:
	docker compose up -d --wait

redis:
	docker exec -it packet-sniffer-redis bash -c "redis-cli"

run:
	make docker-up
	sudo uv run -m packet_sniffer
