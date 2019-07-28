from flask import Flask, render_template

from dash.popular_repos import PopularRepos

app = Flask(__name__)


@app.route('/')
def home():
    popular_repos = PopularRepos('jotenz')
    repos_by_stars = popular_repos.get_popular_repos()

    return render_template('index.html', repos=repos_by_stars)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)