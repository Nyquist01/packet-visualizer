# Packet Visualizer

Visualizes connections being made to/from your device.

This is a personal project so I can learn some frontend development, understand web sockets, and understanding networking better.

# Requirements

- [UV package + project manager](https://docs.astral.sh/uv/getting-started/installation/)
- Docker Engine/[Docker Desktop](https://docs.docker.com/desktop/)

# Usage

On MacOS/Linux:

```
make run
```

On Windows:

1. `docker compose up -d --wait`
2. `uv run -m packet_sniffer`


> [!NOTE]
>  Requires root access to be able to read packets from your device's network interfaces.
