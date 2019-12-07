# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import os
import re
import requests
import json
from config import LINE_API
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

    new_contents = [{
        "type": "separator"
    }, {
        "type": "box",
        "layout": "baseline",
        "contents": [
            {
                "type": "text",
                "text": "Project",
                "size": "sm",
                "weight": "bold"
            },
            {
                "type": "text",
                "text": "Total Unit",
                "align": "end",
                "size": "sm",
                "weight": "bold"
            },
            {
                "type": "text",
                "text": "Net (Excl FD)",
                "align": "end",
                "size": "sm",
                "weight": "bold"
            }
        ]
    }]
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
    total_u = 0
    total_p = 0.00
    for val in values:
        total_u = total_u + val.TotalUnit
        total_p = total_p + val.NetPriceExclFD
        new_contents.append(
            {
                "type": "box",
                "layout": "baseline",
                "contents": [
                    {
                        "type": "text",
                        "text": "{}:{}".format(val.ProductID, val.ProjectName),
                        "size": "xs",
                        "wrap": True
                    },
                    {
                        "type": "text",
                        "text": "{}".format(val.TotalUnit),
                        "size": "xs",
                        "align": "end"
                    },
                    {
                        "type": "text",
                        "text": f"{val.NetPriceExclFD:,.0f}",  # f"{actual_income.ap_bg1_total:,.0f}"
                        "size": "xs",
                        "align": "end"
                    }
                ]
            }
        )

    # print(total_u, total_p)
    new_contents.append(
        {
            "type": "box",
            "layout": "baseline",
            "contents": [
                {
                    "type": "text",
                    "text": "Grand Total",
                    "size": "sm",
                    "weight": "bold",
                    "offsetStart": "150%"
                },
                {
                    "type": "text",
                    "text": "{}".format(total_u),
                    "align": "end",
                    "size": "sm",
                    "weight": "bold"
                },
                {
                    "type": "text",
                    "text": f"{total_p:,.0f}",
                    "align": "end",
                    "size": "sm",
                    "weight": "bold"
                }
            ],
            "backgroundColor": "#7AFF97",
            "margin": "xs"
        }
    )

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
    flex_msg = {
        "type": "flex",
        "altText": "this is a flex message",
        "contents":
            {
                "type": "bubble",
                "size": "giga",
                "header": {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                        {
                            "type": "text",
                            "text": "Actual income",
                            "color": "#FFFFFF",
                            "size": "lg",
                            "weight": "bold"
                        },
                        {
                            "type": "text",
                            "text": "last update {}".format(datetime.now().strftime('%Y-%m-%dT%H:%M')),
                            "align": "end",
                            "size": "xs",
                            "color": "#FFFFFF",
                            "flex": 0,
                            "style": "italic"
                        }
                    ]
                },
                "hero": {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                        {
                            "type": "text",
                            "text": "Transfer Date At {}".format(date_val),
                            "align": "end",
                            "weight": "bold",
                            "offsetEnd": "20px",
                            "size": "sm",
                            "color": "#939393"
                        }
                    ]
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": new_contents
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "Copyright 2019 AP PCL.",
                            "size": "xs",
                            "align": "center",
                            "color": "#ffffff"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "image",
                                    "url": "https://i.ibb.co/fS0B4wP/AP-Logo-2018.png"
                                }
                            ],
                            "position": "absolute",
                            "width": "32px",
                            "height": "32px",
                            "offsetBottom": "2px"
                        }
                    ]
                },
                "styles": {
                    "header": {
                        "backgroundColor": "#000000"
                    },
                    "footer": {
                        "backgroundColor": "#000000"
                    }
                }
            }
    }

    data = {
        "replyToken": reply_token,
        "messages": [
            flex_msg
        ]
    }

    session = requests.Session()
    response = session.post(LINE_API, data=json.dumps(data), headers=headers)
    return 201
