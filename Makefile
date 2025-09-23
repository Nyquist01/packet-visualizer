format:
	uv run ruff format
	uv run ruff check --fix
	uv run ruff check --fix --select I

lint:
	uv run pylint --disable=C,W,R backend/
	uv run mypy backend/

docker-up:
	docker compose up -d --wait

redis:
	docker exec -it packet-sniffer-redis bash -c "redis-cli"

docker-down:
	docker compose down

run:
	make docker-up
	trap "make docker-down" EXIT; sudo uv run --directory backend -m packet_sniffer
