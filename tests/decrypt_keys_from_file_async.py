import asyncio

from key_shuffler import aiofilesOpenEncrypted


async def test():
    async with aiofilesOpenEncrypted("tests/encrypted_wallets.txt", 'r') as file:
        print("AsyncOpenEncrypted:")
        for line in file:
            print(line)

async def main():
    await test()

asyncio.run(main())
