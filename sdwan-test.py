import requests
import urllib3
from constants import vmanage
from login import sdwan_login
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

jsessionid, token, header = sdwan_login(vmanage)
print(jsessionid)
print(token)
print(header)
