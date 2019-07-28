import requests

import json

from authentication import settings
from dash import repos_contributors, repos_stars_forks

HEADERS = {'Authorization': 'token ' + settings.ACCESS_TOKEN}
HOST = settings.HOST

def get_all_data(organization):
    """Retrieves the most popular repos for the given
    organization by stars and forks

    Keyword arguments:
    organization -- string
    """ 
    repos = _get_repos(organization)
    stars_forks_data = repos_stars_forks.get_data(repos)
    contributors_data = repos_contributors.get_data(repos)
    return stars_forks_data, contributors_data


def _get_repos(organization):
    url = '{}/users/{}/repos'.format(HOST, organization)
    response = requests.get(url, headers=HEADERS)
    return json.loads(response.text)
