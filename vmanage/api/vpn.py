from jinja2 import Template


class VPNFeatureTemplate():
    def __init__(self):
        pass

    def generate_dict_vpn_ip_nexthops(nexthops):
        """
        This function generates the block of configurtion for the VPN IP
        nexthops that will be used in CLI template to generate VPN Feature
        Template
        """
        pass


data = '''
{% raw %}
His name is {{ name }}
{% endraw %}
'''

tm = Template(data)
msg = tm.render(name='Peter')

print(msg)
