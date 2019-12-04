import requests


class SID:
    baseURL = "http://sid.donote.co:3000/api/v1/"

    def __init__(self, client_name):
        self.client_name = client_name

    def login(self, clientid, id, pw, is_web=False):
        res = requests.post(self.baseURL + '/session/' , {
            "type": "login",
            "clientid": clientid,
            "userid": id,
            "password": pw,
            "isPermanent": False,
            "isWeb": is_web
        }).json()

        if res["type"] == "error":
            raise Exception("Input Data Error")
        return {
            "sessid": res["response_data"][0],
            "pid": res["response_data"][1],
            "nickname": res["response_data"][2],
            "expire": res["response_data"][3],
        }

    def loginAuth(self, clientid, sessid):
        res = requests.post(self.baseURL + '/session/', {
            "type": "login",
            "clientid": clientid,
            "sessid": sessid
        }).json()

        if res["type"] == "error":
            raise Exception("Input Data Error")
        return {
            "sessid": res["response_data"][0],
            "pid": res["response_data"][1],
            "nickname": res["response_data"][2],
            "expire": res["response_data"][3],
        }

    def logout(self, clientid, sessid):
        res = requests.post(self.baseURL + "/session/", {
            "type": "logout",
            "clientid": clientid,
            "sessid": sessid
        }).json()

        if res["type"] == "error" or not res["is_succeed"]:
            raise Exception("Input Data Error")

        return
