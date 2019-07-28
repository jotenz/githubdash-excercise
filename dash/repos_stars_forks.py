def get_data(repos):
	return {repo['name']: {'forks_count': repo['forks_count'],
			'stargazers_count': repo['stargazers_count']} for repo in repos}
	
