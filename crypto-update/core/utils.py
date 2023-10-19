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



async def get_req_data(update_time):
    async with aiohttp.ClientSession() as session:
        symbols = "ETH-BTC, LTC-BTC, EOS-BTC, XRP-BTC, KCS-BTC, DIA-BTC, VET-BTC, DASH-BTC, DOT-BTC, XTZ-BTC, ZEC-BTC, BSV-BTC, ADA-BTC, ATOM-BTC, LINK-BTC, LUNA-BTC, NEO-BTC, UNI-BTC, ETC-BTC, BNB-BTC, TRX-BTC, XLM-BTC, BCH-BTC, USDC-BTC, GRT-BTC, 1INCH-BTC, AAVE-BTC, SNX-BTC, API3-BTC, CRV-BTC, MIR-BTC, SUSHI-BTC, COMP-BTC, ZIL-BTC, YFI-BTC, OMG-BTC, XMR-BTC, WAVES-BTC, MKR-BTC, COTI-BTC, SXP-BTC, THETA-BTC, ZRX-BTC, DOGE-BTC, LRC-BTC, FIL-BTC, DAO-BTC, BTT-BTC, KSM-BTC, BAT-BTC, ROSE-BTC, CAKE-BTC, CRO-BTC, XEM-BTC, MASK-BTC, FTM-BTC, IOST-BTC, ALGO-BTC, DEGO-BTC, CHR-BTC, CHZ-BTC, MANA-BTC, ENJ-BTC, IOST-BTC, ANKR-BTC, ORN-BTC, SAND-BTC, VELO-BTC, AVAX-BTC, DODO-BTC, WIN-BTC, ONE-BTC, SHIB-BTC, ICP-BTC, MATIC-BTC, CKB-BTC, SOL-BTC, VRA-BTC, DYDX-BTC, ENS-BTC, NEAR-BTC, SLP-BTC, AXS-BTC, TLM-BTC, ALICE-BTC, IOTX-BTC, QNT-BTC, SUPER-BTC, HABR-BTC, RUNE-BTC, EGLD-BTC, AR-BTC, RNDR-BTC, LTO-BTC, YGG-BTC".replace('BTC', 'USDT').split(', ')
        symbols.append("BTC-USDT")
        start_time, end_time = set_time(update_time)
        print(symbols)
        for symbol in symbols:
            print(symbol)
            url =  f'https://api.kucoin.com/api/v1/market/candles?type={update_time}min&symbol={symbol}&startAt={start_time}&endAt={end_time}'
            async with session.get(url) as response:
                x = await response.json()
            with open("j_file.json", "a+") as jf:
                json.dump(x, jf)

asyncio.run(get_req_data(1))