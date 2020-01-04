# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import os
import re
import requests
import json
from config import LINE_API_REPLY
from models.vw_crm_line_actual_income import ActualIncomeByProjModel
from datetime import datetime
from typing import List


def replyMsg(reply_token: str = None, text_msg: str = None,
             values: List["ActualIncomeByProjModel"] = None,
             date_val: str = None,
             line_aceess_token: str = None) -> int:
    authorization = 'Bearer {}'.format(line_aceess_token)
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': authorization
    }
    print(values)
    # value = [(100, 10), (200, 20), (300, 30)]

    # header
    # for i in value:
    #     print(i[0], i[1])
    #     new_contents.append(
    #         {
    #             "type": "box",
    #             "layout": "baseline",
    #             "contents": [
    #                 {
    #                     "type": "text",
    #                     "text": "{}".format(i[0]),
    #                     "align": "start"
    #                 },
    #                 {
    #                     "type": "text",
    #                     "text": "{}".format(i[1]),
    #                     "align": "end"
    #                 }
    #             ]
    #         }
    #     )

    # flex_msg = {
    #     "type": "flex",
    #     "altText": "this is a flex message",
    #     "contents": {
    #         "type": "bubble",
    #         "body": {
    #             "type": "box",
    #             "layout": "vertical",
    #             # "contents": [ { "type": "text", "text": "hello" }, { "type": "text", "text": "world" } ]
    #             "contents": new_contents
    #         }
    #     }
    # }

    data = {
        "replyToken": reply_token,
        "messages": [
            flex_msg
        ]
    }

    session = requests.Session()
    response = session.post(LINE_API_REPLY, data=json.dumps(data), headers=headers)
    return 201
