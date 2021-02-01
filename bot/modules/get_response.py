import aiohttp

async def nyaa(query):
    url = f"https://nyaaapi.herokuapp.com/nyaa/{query[0]}?query={query[-1]}&sub_category={query[1]}"
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            return data["data"]

async def nyaa_id(unique_id):
    url = f"https://nyaaapi.herokuapp.com/nyaa/id/{unique_id}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            return data["info"]

async def sukebei(query):
    url = f"https://nyaaapi.herokuapp.com/sukebei/{query[0]}?query={query[-1]}&sub_category={query[1]}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            return data["data"]

async def sukebei_id(unique_id):
    url = f"https://nyaaapi.herokuapp.com/sukebei/id/{unique_id}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            return data["info"]