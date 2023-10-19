import asyncio
import aiohttp
import redis
import json
from datetime import datetime


def set_time(minute: int):
    if minute == 1:
        start_time = int(datetime.timestamp(datetime.now())) - 60
    elif minute == 5:
        start_time = int(datetime.timestamp(datetime.now())) - 300

    end_time = int(datetime.timestamp(datetime.now()))

    return start_time, end_time


