import requests
# import json


class Robot:
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    data = {
        "msgtype": "text",
        "text": {"content": ""},
        "at": {
            "atMobiles": [],
            "atUserIds": [],
            "isAtAll": False
        }
    }

    def __init__(self, webhook, keyword=None):
        self.webhook = webhook
        self.keyword = keyword

    def send_text(self, content, is_at_all=False, at_mobiles_list=[], atUserIds_list=[]):
        # set data
        if self.keyword:
            Robot.data["text"]["content"] = self.keyword + ": " + content
        else:
            Robot.data["text"]["content"] = content
        Robot.data["at"]["isAtAll"] = is_at_all
        Robot.data["at"]["atMobiles"] = at_mobiles_list
        Robot.data["at"]["atUserIds"] = atUserIds_list

        # # post data use data
        # post_data = json.dumps(Robot.data)
        # r = requests.post(url=self.webhook, headers=Robot.headers, data=post_data)

        # post data use json
        r = requests.post(url=self.webhook, json=Robot.data)  # json传入字典，data传入json数据,且要加headers
        print(r.text)
        return r.text
