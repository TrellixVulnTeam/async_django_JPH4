async def get_data(session, url):
    async with session.get(url) as response:
        res_data = await response.json()
        return res_data