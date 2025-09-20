from redis import Redis


def redis_client():
    return Redis(decode_responses=True)


class ConnectionQueue:
    """
    Queue for the WebSocket server to consume connection data from
    """

    def __init__(self, redis: Redis, q_name: str):
        self.redis = redis
        self.queue_name = q_name

    def push(self, conn: str) -> None:
        self.redis.rpush(self.queue_name, conn)

    def pop(self) -> str | None:
        """
        Pop a connection from the queue. This function blocks until
        an item is available
        """
        return self.redis.blpop(self.queue_name)
