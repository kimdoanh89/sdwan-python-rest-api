import requests
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class Authentication:

    @staticmethod
    def get_jsessionid(vmanage):
        api = "/j_security_check"
        base_url = "https://" + f'{vmanage["host"]}:{vmanage["port"]}'
        url = base_url + api
        payload = {
            "j_username": vmanage["username"],
            "j_password": vmanage["password"]
        }
        response = requests.post(url=url, data=payload, verify=False)
        if response.status_code == 200:
            cookies = response.headers["Set-Cookie"]
            jsessionid = cookies.split(";")
            return(jsessionid[0])
        else:
            print("Login Failed")
            sys.exit(0)

    @staticmethod
    def get_token(vmanage, jsessionid):
        headers = {'Cookie': jsessionid}
        base_url = "https://" + f'{vmanage["host"]}:{vmanage["port"]}'
        api = "/dataservice/client/token"
        url = base_url + api
        response = requests.get(url=url, headers=headers, verify=False)
        if response.status_code == 200:
            return(response.text)
        else:
            return None


def authentication(vmanage):
    Auth = Authentication()
    jsessionid = Auth.get_jsessionid(vmanage)
    token = Auth.get_token(vmanage, jsessionid)

    if token is not None:
        header = {
            'Content-Type': "application/json",
            'Cookie': jsessionid,
            'X-XSRF-TOKEN': token}
    else:
        header = {'Content-Type': "application/json", 'Cookie': jsessionid}
    return header
