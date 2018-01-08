from jinja2 import Environment, FileSystemLoader

a_env = Environment(loader=FileSystemLoader('./', encoding='utf8'))
tpl = a_env.get_template('login.html')