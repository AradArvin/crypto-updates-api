import asyncio
import aiohttp
import redis
from datetime import datetime



redisClient = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)


def set_time(minute: int):
    if minute == 1:
        start_time = int(datetime.timestamp(datetime.now())) - 60
    elif minute == 5:
        start_time = int(datetime.timestamp(datetime.now())) - 300

    end_time = int(datetime.timestamp(datetime.now()))

    return start_time, end_time



def cache_data_to_redis(req_data, symbol, update_time):
    data = str(req_data['data'][0]) if req_data.get('data') else ''
    score = int(req_data['data'][0][0]) if req_data.get('data') else 0
    redisClient.zadd(f"{symbol}_{update_time}min", {data:score})



async def get_req_data(update_time: int):
    async with aiohttp.ClientSession() as session:
        symbols = "ETH-BTC, LTC-BTC, EOS-BTC, XRP-BTC, KCS-BTC, DIA-BTC, VET-BTC, DASH-BTC, DOT-BTC, XTZ-BTC, ZEC-BTC, BSV-BTC, ADA-BTC, ATOM-BTC, LINK-BTC, LUNA-BTC, NEO-BTC, UNI-BTC, ETC-BTC, BNB-BTC, TRX-BTC, XLM-BTC, BCH-BTC, USDC-BTC, GRT-BTC, 1INCH-BTC, AAVE-BTC, SNX-BTC, API3-BTC, CRV-BTC, MIR-BTC, SUSHI-BTC, COMP-BTC, ZIL-BTC, YFI-BTC, OMG-BTC, XMR-BTC, WAVES-BTC, MKR-BTC, COTI-BTC, SXP-BTC, THETA-BTC, ZRX-BTC, DOGE-BTC, LRC-BTC, FIL-BTC, DAO-BTC, BTT-BTC, KSM-BTC, BAT-BTC, ROSE-BTC, CAKE-BTC, CRO-BTC, XEM-BTC, MASK-BTC, FTM-BTC, IOST-BTC, ALGO-BTC, DEGO-BTC, CHR-BTC, CHZ-BTC, MANA-BTC, ENJ-BTC, IOST-BTC, ANKR-BTC, ORN-BTC, SAND-BTC, VELO-BTC, AVAX-BTC, DODO-BTC, WIN-BTC, ONE-BTC, SHIB-BTC, ICP-BTC, MATIC-BTC, CKB-BTC, SOL-BTC, VRA-BTC, DYDX-BTC, ENS-BTC, NEAR-BTC, SLP-BTC, AXS-BTC, TLM-BTC, ALICE-BTC, IOTX-BTC, QNT-BTC, SUPER-BTC, HABR-BTC, RUNE-BTC, EGLD-BTC, AR-BTC, RNDR-BTC, LTO-BTC, YGG-BTC".replace('BTC', 'USDT').split(', ')
        symbols.append("BTC-USDT")

        start_time, end_time = set_time(update_time)

        for symbol in symbols:

            url =  f'https://api.kucoin.com/api/v1/market/candles?type={update_time}min&symbol={symbol}&startAt={start_time}&endAt={end_time}'
            
            async with session.get(url) as response:
                req_data = await response.json()
            
            cache_data_to_redis(req_data, symbol, update_time)

