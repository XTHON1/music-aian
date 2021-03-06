import asyncio

from pyrogram import Client

TG = """
A bot that can play music on telegram group's voice chat.

This file is part of < https://github.coM/XTHON1/music-aian > project,
and is released under the "Apache 2.0".
"""

print(TG)
api_id = input("Enter Your API ID: \n")
api_hash = input("Enter Your API HASH : \n")


async def main():
    async with Client(":memory:", api_id=int(input("API ID:")), api_hash=input("API HASH:")) as app:
        print(await app.export_session_string())


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
