import os
import json
import aiohttp
import asyncio

async def aiohttp_json_objects():
    url = "https://jsonplaceholder.typicode.com/posts"
    directory = "aiohttp"
    os.mkdir(directory)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
                data = await response.json()
                for i, obj in enumerate(data, start=1):
                    filename = os.path.join(directory, f"json_object_{i}.json")
                    with open(filename, 'w') as file:
                        json.dump(obj, file, indent=2)
                        print(f"Saved {filename}")

async def main():
    await aiohttp_json_objects()

if __name__ == "__main__":
    asyncio.run(main())