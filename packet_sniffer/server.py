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

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var ws = new WebSocket("ws://localhost:8000/raw");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""


@app.get("/")
async def get():
    return HTMLResponse(html)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")


@app.websocket("/raw")
async def raw_packet_data(websocket: WebSocket):
    await websocket.accept()
    redis = redis_client()
    queue = ConnectionQueue(redis, REDIS_QUEUE_KEY)
    while True:
        conn = queue.pop()
        await websocket.send_json(conn)
        await asyncio.sleep(0.5)  # dont spam
