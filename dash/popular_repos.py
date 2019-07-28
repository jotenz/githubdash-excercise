import requests

import json

from authentication import settings


class PopularRepos():
	def __init__(self, organization):
		self.organization = organization
		self.headers = {'Authorization': 'token ' + settings.ACCESS_TOKEN}
		self.host = settings.HOST

	def get_popular_repos(self):
		"""Retrieves the most popular repos for the given
		organization by stars, forks, and contributors

		Keyword arguments:
		organization -- string
		"""	
		repos = self._get_repos()
		return repos

	def _get_repos(self):
		try:
			url = '{}/users/{}/repos'.format(self.host, self.organization)
			response = requests.get(url, headers=self.headers)
			return json.loads(response.text)
		except Exception as e:
			return e
