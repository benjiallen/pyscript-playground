from jinja2 import Environment, FileSystemLoader, select_autoescape
from js import document

# useful way to understand what gets copied over to the browser
# import os

# print('Current Working Directory:')
# print(os.getcwd())

# print('Current directory contents:')
# files = os.listdir('.')
# if len(files) == 0:
#         print('Directory is empty')
# else:
#     for file in files:
#         print(file)

env = Environment(
    loader = FileSystemLoader("./"),
    autoescape=select_autoescape()
)
template = env.get_template("hello.jinja")
document.querySelector("main").innerHTML = template.render(name='Ben', test='', test1='not empty')
