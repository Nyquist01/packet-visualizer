REDIS_QUEUE_KEY = "packet_queue"

# Berkley Packet Filter expression
# 6379 - ignore local Redis connections
BFP = "not tcp port 6379 and not tcp port 8000"
