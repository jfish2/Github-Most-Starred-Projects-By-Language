import requests
import pygal
from pygal.style import DarkSolarizedStyle as DSS, LightenStyle as LS

url = 'https://api.github.com/search/repositories?q=language:java&sort=stars'
r = requests.get(url)

#Status code of 200 == Success
print("Status code: ", r.status_code)

response_dict = r.json()
print("Total repositories:", response_dict['total_count'])
repo_dicts = response_dict['items']
print("Repositories returned:", len(repo_dicts))

names, plot_dicts = [], []


for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    description = repo_dict['description']
    if not description:
        description = 'No description provided.'

    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': description,
        'xlink': repo_dict['html_url']
    }

    plot_dicts.append(plot_dict)




my_style = DSS(base_style=LS)
my_style.title_font_size = 24
my_style.label_font_size = 14
my_style.major_label_font_size = 18

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, stlye=my_style)
chart.title = 'Most Starred/Popular Java Projects on Github'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('java_repos.svg')
