REDIS_QUEUE_KEY = "packet_queue"

# Berkley Packet Filter expression
# port 6379 - ignore local Redis connections
# port 8000 - ignore local connections to the WebSocker server
BFP = "not tcp port 6379 and not tcp port 8000"
