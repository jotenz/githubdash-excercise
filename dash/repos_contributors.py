import asyncio
from aiohttp import ClientSession
from concurrent.futures import ThreadPoolExecutor
import json
import requests

from authentication import settings

HEADERS = {'Authorization': 'token ' + settings.ACCESS_TOKEN}

async def fetch(repo_name, url, session):
    # The async task

    async with session.get(url, headers=HEADERS) as response:

        response = await response.read()

        return {repo_name: len(json.loads(response))}


async def fetch_all(repo_urls):
    tasks = []
    async with ClientSession() as session:
        for repo_name, url in repo_urls.items():
            task = asyncio.ensure_future(fetch(repo_name, url, session))
            tasks.append(task)
        responses = await asyncio.gather(*tasks)

    return responses


def get_data(repos):
    repo_urls = {repo['name']: _clean_url(repo['contributors_url']) for repo in repos}
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    future = asyncio.ensure_future(fetch_all(repo_urls)) 
    responses = loop.run_until_complete(future) 
    loop.close()
    return responses


def _clean_url(url):
    split = url.split('{')
    return split[0]
