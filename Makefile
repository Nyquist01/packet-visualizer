format:
	uv run ruff format
	uv run ruff check --fix --select I

lint:
	uv run pylint --disable=C,W,R packet_sniffer/
	uv run mypy packet_sniffer/
