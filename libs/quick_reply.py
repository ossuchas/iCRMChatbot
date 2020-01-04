# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import os
import re
import requests
import json
from config import LINE_API_REPLY
from models.vw_crm_line_actual_income import ActualIncomeByProjModel
from typing import List


def quickreplymsg(reply_token: str = None, text_msg: str = None,
             line_aceess_token: str = None) -> int:

    authorization = 'Bearer {}'.format(line_aceess_token)
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': authorization
    }

    quick_reply = \
        {
            "type": "text",
            "text": "Hello Quick Reply!",
            "quickReply": {
                "items": [
                    {
                        "type": "action",
                        "action": {
                            "type": "cameraRoll",
                            "label": "Camera Roll"
                        }
                    },
                    {
                        "type": "action",
                        "action": {
                            "type": "camera",
                            "label": "Camera"
                        }
                    },
                    {
                        "type": "action",
                        "action": {
                            "type": "location",
                            "label": "Location"
                        }
                    },
                    {
                        "type": "action",
                        "imageUrl": "https://cdn1.iconfinder.com/data/icons/mix-color-3/502/Untitled-1-512.png",
                        "action": {
                            "type": "message",
                            "label": "Message",
                            "text": "Hello World!"
                        }
                    },
                    {
                        "type": "action",
                        "action": {
                            "type": "postback",
                            "label": "Postback",
                            "data": "action=buy&itemid=123",
                            "displayText": "Buy"
                        }
                    },
                    {
                        "type": "action",
                        "imageUrl": "https://icla.org/wp-content/uploads/2018/02/blue-calendar-icon.png",
                        "action": {
                            "type": "datetimepicker",
                            "label": "Datetime Picker",
                            "data": "storeId=12345",
                            "mode": "datetime",
                            "initial": "2018-08-10t00:00",
                            "max": "2018-12-31t23:59",
                            "min": "2018-08-01t00:00"
                        }
                    }
                ]
            }
        }

    data = {
        "replyToken": reply_token,
        "messages": [ quick_reply ]
    }

    session = requests.Session()
    response = session.post(LINE_API_REPLY, data=json.dumps(data), headers=headers)
    return 201
