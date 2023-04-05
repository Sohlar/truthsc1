import aiohttp


async def request_json(url, body=None, method="GET", headers=None, params=None, timeout=100, **kwargs):
    async with aiohttp.ClientSession() as session:
        async with session.request(method, url, json=body, headers=headers, params=params, timeout=timeout, **kwargs) as response:
            try:
                return await response.json()
            except aiohttp.ContentTypeError:
                data = {}
                data['next'] = response.headers['Link'].split(',')[1].split(';')[0].replace('<', '').replace('>', '')[1:]
                data['prev'] = response.headers['Link'].split(',')[0].split(';')[0].replace('<', '').replace('>', '')
                data['feed'] = await response.json(content_type=None)
                return data
            except aiohttp.TimeoutError:
                return print('Run')