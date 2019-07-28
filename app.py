from flask import Flask, Markup, render_template, request
import plotly.graph_objects as go
from plotly.offline import plot

from dash import dash_data

app = Flask(__name__)


animals=['giraffes', 'orangutans', 'monkeys']


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dash', methods=['POST'])
def dash():
    stars_forks_data, contributors_data = dash_data.get_all_data(request.form['organization'])

    stars_div = plot(_create_stars_figure(stars_forks_data), output_type='div')
    forks_div = plot(_create_forks_figure(stars_forks_data), output_type='div')
    contributors_div = plot(_create_contributors_figure(contributors_data), output_type='div')

    return render_template('dash.html',
                            stars=Markup(stars_div),
                            forks=Markup(forks_div),
                            contributors=Markup(contributors_div))


def _create_stars_figure(stars_forks_data):
    x_axis = [key for key in stars_forks_data.keys()]
    y_axis = [stars_forks_data[key]['stargazers_count'] for key in x_axis]
    fig = go.Figure([go.Bar(x=x_axis, y=y_axis)])
    return fig


def _create_forks_figure(stars_forks_data):
    x_axis = [key for key in stars_forks_data.keys()]
    y_axis = [stars_forks_data[key]['forks_count'] for key in x_axis]
    fig = go.Figure([go.Bar(x=x_axis, y=y_axis)])
    return fig


def _create_contributors_figure(contributors_data):
    cleaned_data = {}
    for item in contributors_data:
        cleaned_data.update(item)

    x_axis = [key for key in cleaned_data.keys()]
    y_axis = [cleaned_data[key] for key in x_axis]
    fig = go.Figure([go.Bar(x=x_axis, y=y_axis)])
    return fig

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

'''
Stars and Forks Data: {'example-repo': {'forks_count': 0, 'stargazers_count': 0}, 'finalproject': {'forks_count': 0, 'stargazers_count': 0}, 'githubdash-excercise': {'forks_count': 0, 'stargazers_count': 0}, 'King-s-Courses': {'forks_count': 0, 'stargazers_count': 1}, 'spark': {'forks_count': 0, 'stargazers_count': 0}}

Contributors Data: [{'example-repo': 1}, {'finalproject': 2}, {'githubdash-excercise': 0}, {'King-s-Courses': 2}, {'spark': 30}]
'''