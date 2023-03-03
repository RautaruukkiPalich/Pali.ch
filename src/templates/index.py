from fastapi.templating import Jinja2Templates

# env = Environment(loader=FileSystemLoader(searchpath='html/'))
# # index_template = env.get_template('index.html')


def get_templates(path):
    templates = Jinja2Templates(directory=path)
    return templates


