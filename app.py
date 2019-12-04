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
        res = requests.delete(self.baseURL + "/session/", data={
            "type": "logout",
            "clientid": clientid,
            "sessid": sessid
        }).json()

        if res["type"] == "error" or not res["is_succeed"]:
            raise Exception("Input Data Error")

        return

    def register(self, clientid, userid, pw, nickname = "User"):
        res = requests.post("/user/", {
            "type": "register",
            "clientid": clientid,
            "userid": userid,
            "nickname": nickname,
            "password": pw
        }).json()

        if res["type"] == "error" or not res["is_succeed"]:
            raise Exception("Input Data Error")

        return res["private_id"]

    def getUserNickname(self, clientid, sessid):
        res = requests.get('{}/{}/usname'.format(clientid, sessid))

        if res["type"] == 'error':
            raise Exception('Input Data Error')
        if not res["is_valid"]:
            return ''

        return res["response_data"]

    def loginCheck(self, target):
        raise NotImplementedError()

    def passwordCheck(self, clientid, sessid, pw):
        res = requests.post("/password/verify", {
            "type": "verify",
            "data": "password",
            "clientid": clientid,
            "sessid": sessid,
            "value": pw
        }).json()

        if res["type"] == "error" or not res["is_succeed"]:
            raise Exception("Input Data Error")

        return True

