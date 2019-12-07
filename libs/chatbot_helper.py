import os
import re
import requests
import json
from config import LINE_API


def replyMsg(reply_token, text_msg, line_aceess_token):
    authorization = 'Bearer {}'.format(line_aceess_token)
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': authorization
    }

    # print(type(test_dict))

    type_msg = {
            "type": "flex",
            "altText": "Flex Message",
            "contents":
                {
                    "type": "bubble",
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": "hello, world",
                                "action": {
                                    "type": "datetimepicker",
                                    "label": "action",
                                    "data": "storeId=12345",
                                    "mode": "date"
                                }
                            },
                            {
                                "type": "button",
                                "action": {
                                    "type": "datetimepicker",
                                    "label": "action",
                                    "data": "actual_income",
                                    "mode": "date"
                                }
                            }
                        ]
                    }
                }
        }
    # type_msg = {
    #     "type": "text",
    #     "text": text_msg
    # }

    data = {
        "replyToken": reply_token,
        "messages": [
            type_msg
        ]
    }

    session = requests.Session()
    response = session.post(LINE_API, data=json.dumps(data), headers=headers)
    return 201
