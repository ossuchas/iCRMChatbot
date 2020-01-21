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
            "text": "กรุณา Share ตำแหน่งที่คุณอยู่เพื่อตรวจสอบค่า PM 2.5 ในตำแหน่งนั้น",
            "quickReply": {
                "items": [
                    {
                        "type": "action",
                        "action": {
                            "type": "location",
                            "label": "Share Location"
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
