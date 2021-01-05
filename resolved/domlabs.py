import requests
import json
import datetime
import time
import random
import traceback


BASE_URL = "https://tasks.resolved.gg/api/v1"


class Resolved:
    def __init__(self, company_api_key, user_api_key):
        self.company_api_key = company_api_key
        self.user_api_key = user_api_key

    def createTask(self, site_key, site_url, captcha_type, captcha_version, session_clone, smart_movement, proxy, cookies=[], headers={}):
        try:
            self.site_key = site_key
            self.site_url = site_url
            self.captcha_type = captcha_type
            self.captcha_version = captcha_version
            self.session_clone = session_clone
            self.cookies = cookies
            self.headers = headers
            self.smart_movement = smart_movement
            self.proxy = proxy

            if self.session_clone == False:
                payload = {
                    "proxy": self.proxy,
                    "company_api_key": self.company_api_key,
                    "user_api_key": self.user_api_key,
                    "site_key": self.site_key,
                    "site_url": self.site_url,
                    "captcha_type": self.captcha_type,
                    "captcha_version": self.captcha_version,
                    "session_clone": self.session_clone,
                    "smart_movement": self.smart_movement
                }
            else:
                payload = {
                    "proxy": self.proxy,
                    "company_api_key": self.company_api_key,
                    "user_api_key": self.user_api_key,
                    "site_key": self.site_key,
                    "site_url": self.site_url,
                    "captcha_type": self.captcha_type,
                    "captcha_version": self.captcha_version,
                    "session_clone": self.session_clone,
                    "cookies": self.cookies,
                    "headers": self.headers,
                    "smart_movement": self.smart_movement
                }

            res = requests.post(f"{BASE_URL}/recaptcha/new-task", json=payload)
            if res.status_code != 200:
                return {"status": "error", "message": "Failed to send task to API", "data": res.json()}
            else:
                self.taskID = res.json()['data']['task_id']
                return {"status": "success", "message": "Successfully created and sent to API", "data": {"taskID": res.json()['data']['task_id']}}
        except:
            return {"status": "error", "message": "Failed to create task", "data": {"error": traceback.format_exc()}}

    def getToken(self):
        payload = {
            "company_api_key": self.company_api_key,
            "user_api_key": self.user_api_key,
            "task_id": self.taskID
        }

        processed = False
        while not processed:
            response, code = self.getResult(payload)
            if response and code == 200:
                processed = True
                return {"status": "success", "message": "Successfully solved reCaptcha", "data": {"token": response}}
            elif response and code == 500:
                return {"status": "error", "message": "Failed to send task to API", "data": response.json()}, 500
            else:
                print("Waiting to solve reCaptcha")
            time.sleep(0.5)

        
    def getResult(self, payload):
        res = requests.post(f"{BASE_URL}/get-task-by-id", json=payload)
        if res.status_code != 200:
            return {"status": "error", "message": "Failed to send task to API", "data": res.json()}, 500
        else:
            data = res.json()['data']['task']
            if data["tokenValue"] != None:
                token = data['tokenValue']
                return token, 200
            else:
                return None, None
