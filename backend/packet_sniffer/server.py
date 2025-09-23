"""
WebSocket server to stream parsed packet data
"""

import asyncio
import logging

from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse

from .consts import REDIS_QUEUE_KEY
from .redis_client import ConnectionQueue, redis_client

logger = logging.getLogger()

app = FastAPI()


def load_home_html():
    with open("../frontend/home.html") as file:
        return file.read()


@app.get("/")
async def get():
    return HTMLResponse(load_home_html())


@app.websocket("/connections")
async def raw_packet_data(websocket: WebSocket):
    await websocket.accept()
    redis = redis_client()
    queue = ConnectionQueue(redis, REDIS_QUEUE_KEY)
    while True:
        conn = queue.pop()
        await websocket.send_json(conn)
        await asyncio.sleep(0.5)  # dont spam
