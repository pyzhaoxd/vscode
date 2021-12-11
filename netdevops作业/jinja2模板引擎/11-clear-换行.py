from jinja2 import Template
from utils import get_jinja2_template

if __name__ == '__main__':

    template = get_jinja2_template('11-去掉换行.j2')
  

    output = template.render(something=True)
    print(output)