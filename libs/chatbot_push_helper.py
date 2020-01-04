import os
import re
import requests
import json
from config import LINE_API_PUSH, LINE_API_REPLY


def pushMsg(reply_token, line_aceess_token):
    authorization = 'Bearer {}'.format(line_aceess_token)
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': authorization
    }

    data = {
        "replyToken": reply_token,
        "messages": [
            {
                "type": "video",
                "originalContentUrl": "https://mokmoon.com/videos/Brown.mp4",
                "previewImageUrl": "https://linefriends.com/img/bangolufsen/img_og.jpg"
            }
        ]
    }

    session = requests.Session()
    response = session.post(LINE_API_REPLY, data=json.dumps(data), headers=headers)
    return 201
