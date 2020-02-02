# -*- coding: utf-8 -*-

import requests
import json
from config import LINE_API_REPLY


def replyMsg(Reply_token: str =None, bg: str = None, line_Acees_Token: str = None):
    authorization = 'Bearer {}'.format(line_Acees_Token)
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': authorization
    }

    type_msg = \
        {
            "type": "flex",
            "altText": "Flex Message",
            "contents": {
                "type": "bubble",
                "direction": "ltr",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "button",
                            "action": {
                                "type": "message",
                                "label": "ตรวจสอบ PM 2.5",
                                "text": "ตรวจสอบค่า PM 2.5"
                            },
                            "color": "#7B76B4",
                            "style": "primary"
                        },
                        {
                            "type": "button",
                            "action": {
                                "type": "message",
                                "label": "ไวรัส โคโรนา",
                                "text": "ไวรัสโคโรนา"
                            },
                            "color": "#B62121",
                            "margin": "sm",
                            "style": "primary"
                        }
                    ]
                }
            }
        }

    data = {
        "replyToken": Reply_token,
        "messages": [
            type_msg
        ]
    }

    session = requests.Session()
    response = session.post(LINE_API_REPLY, data=json.dumps(data), headers=headers)
    return 201
