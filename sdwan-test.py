import requests
import urllib3
from vmanage.constants import vmanage
from vmanage.authenticate import authentication
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

jsessionid, token, header = authentication(vmanage)
print(jsessionid)
print(token)
print(header)
