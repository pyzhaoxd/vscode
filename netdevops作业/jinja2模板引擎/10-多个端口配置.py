from jinja2 import Template
from jinja2.nodes import InternalName
from utils import get_jinja2_template

if __name__ == '__main__':
   
    template = get_jinja2_template('10-多个端口配置.j2')

    intf = {
        'name': 'eth1/1',
        'shutdown': True,
        'description': 'jinja2 configure',

    }


    output = template.render(interfaces=intf)
    print(output)
   