# -*- coding: utf-8 -*-

import requests
import json
from config import LINE_API_REPLY
from models.tmp_virus_corona import VirusCoronaModel
from typing import List
from datetime import datetime


def replyMsg(Reply_token: str = None, virus: List["VirusCoronaModel"] = None,
             totalCase: int = None,
             totalDeath: int = None,
             totalRecovered: int = None,
             line_Acees_Token: str = None):
    authorization = 'Bearer {}'.format(line_Acees_Token)
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': authorization
    }
    # print(virus)
    # print(totalCase, totalDeath)

    # Current Value
    new_contents = [
        {"type": "separator"},
        {"type": "box", "layout": "horizontal",
         "contents": [{"type": "text", "text": "Covid-19 Cases:", "size": "lg", "weight": "bold", "flex": 0},
                      {"type": "text", "text": f"{totalCase:,.0f}", "align": "end", "weight": "bold", "size": "xl",
                       "color": "#0074ff"}
                      ]
         },
        {"type": "box", "layout": "horizontal",
         "contents": [{"type": "text", "text": "Deaths:", "size": "lg", "weight": "bold", "flex": 0},
                      {"type": "text", "text": f"{totalDeath:,.0f}", "align": "end", "weight": "bold", "size": "xl",
                       "color": "#ff2400"}]
         },
        {"type": "box", "layout": "horizontal",
         "contents": [{"type": "text", "text": "Recovered:", "size": "lg", "weight": "bold", "flex": 0},
                      {"type": "text", "text": f"{totalRecovered:,.0f}", "align": "end", "weight": "bold", "size": "xl",
                       "color": "#8ACA2B"}]
         },
        {"type": "box", "layout": "baseline",  # Header
         "contents": [{"type": "text", "text": "Country", "size": "sm", "weight": "bold", "color": "#FFFFFF"},
                      {"type": "text", "text": "Total Case", "size": "sm", "weight": "bold", "align": "end",
                       "color": "#FFFFFF"},
                      {"type": "text", "text": "Today", "size": "sm", "weight": "bold", "align": "end",
                       "color": "#FFFFFF"},
                      {"type": "text", "text": "Deaths", "size": "sm", "align": "end", "weight": "bold",
                       "color": "#FFFFFF"}
                      ],
         "backgroundColor": "#76706f", "margin": "sm"
         },
    ]

    i_count_rec = 0
    for val in virus:
        new_contents.append(
            {"type": "box", "layout": "baseline",  # Detail
             "contents": [{"type": "text", "text": val.Country, "size": "xs"},
                          {"type": "text", "text": val.TotalCase, "align": "end", "size": "sm"},
                          {"type": "text", "text": val.TodayChange, "size": "xs", "align": "end"},
                          {"type": "text", "text": val.TotalDeath, "size": "xs", "align": "end"}],
             "backgroundColor": "#FAF5FF"
             }
        )
        i_count_rec += 1

    # print(new_contents)
    new_contents.append(
        {
            "type": "separator",
            "margin": "sm"
        }
    )

    new_contents.append(
        {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "text",
                    "text": "Remark : List of Country by Total Cases TOP 25",
                    "size": "xs",
                    "style": "italic"
                }
            ]
        }
    )

    type_msg = \
        {
            "type": "flex",
            "altText": "Flex Message",
            "contents":
                {
                    "type": "bubble",
                    "size": "giga",
                    "header": {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [ { "type": "text", "text": "Covid-19 (2019-nCoV)", "color": "#FFFFFF", "size": "lg", "weight": "bold", "flex": 0 },
                            { "type": "text", "text": " ", "align": "end", "color": "#FFFFFF", "weight": "bold" },
                            { "type": "text", "text": datetime.now().strftime("%d.%m.%Y, %H:%M:%S"), "position": "absolute", "color": "#FFFFFF", "size": "xs", "style": "italic", "offsetEnd": "17px", "offsetBottom": "2px" }
                        ]
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents":
                            new_contents
                        #     [
                        #     { "type": "separator" },
                        #     { "type": "box", "layout": "horizontal",
                        #         "contents": [ { "type": "text", "text": "Coronavirus Cases:", "size": "lg", "weight": "bold", "flex": 0 },
                        #             { "type": "text", "text": "13,830", "align": "end", "weight": "bold", "size": "xl", "color": "#0074ff" }
                        #         ]
                        #     },
                        #     { "type": "box", "layout": "horizontal", "contents": [ { "type": "text", "text": "Deaths:", "size": "lg", "weight": "bold", "flex": 0 },
                        #             { "type": "text", "text": "259", "align": "end", "weight": "bold", "size": "xl", "color": "#ff2400" } ]
                        #     },
                        #     { "type": "separator", "margin": "none" },
                        #     { "type": "box", "layout": "baseline",  # Header
                        #       "contents": [ { "type": "text", "text": "Country", "size": "sm", "weight": "bold", "color": "#FFFFFF" },
                        #             { "type": "text", "text": "Total Case", "size": "sm", "weight": "bold", "align": "end", "color": "#FFFFFF" },
                        #             { "type": "text", "text": "Today", "size": "sm", "weight": "bold", "align": "end", "color": "#FFFFFF" },
                        #             { "type": "text", "text": "Deaths", "size": "sm", "align": "end", "weight": "bold", "color": "#FFFFFF" }
                        #         ],
                        #         "backgroundColor": "#76706f", "margin": "sm"
                        #     },
                        #     { "type": "separator" },
                        #     { "type": "box", "layout": "baseline",  # Detail
                        #         "contents": [ { "type": "text", "text": "China", "size": "xs" },
                        #             { "type": "text", "text": "11,901", "align": "end", "size": "sm" },
                        #             { "type": "text", "text": "+110", "size": "xs", "align": "end" },
                        #             { "type": "text", "text": "259", "size": "xs", "align": "end" } ],
                        #         "backgroundColor": "#FAF5FF"
                        #     },
                        #     { "type": "box", "layout": "baseline",
                        #       "contents": [ { "type": "text", "text": "Japan", "size": "xs" },
                        #             { "type": "text", "text": "20", "align": "end", "size": "sm" },
                        #             { "type": "text", "text": "+3", "size": "xs", "align": "end" },
                        #             { "type": "text", "text": "0", "size": "xs", "align": "end" } ],
                        #         "backgroundColor": "#FAF5FF"
                        #     },
                        #     { "type": "box", "layout": "baseline",
                        #       "contents": [ { "type": "text", "text": "Thailand", "size": "xs" },
                        #             { "type": "text", "text": "19", "align": "end", "size": "sm" },
                        #             { "type": "text", "size": "xs", "align": "end", "text": "0" },
                        #             { "type": "text", "text": "0", "size": "xs", "align": "end" } ],
                        #         "backgroundColor": "#FAF5FF"
                        #     }
                        # ]
                    },
                    "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": "Copyright 2020",
                                "align": "center",
                                "size": "xs",
                                "color": "#FFFFFF"
                            }
                        ]
                    },
                    "styles": {
                        "header": {
                            "backgroundColor": "#008dc9"
                        },
                        "hero": {
                            "backgroundColor": "#000000"
                        },
                        "footer": {
                            "backgroundColor": "#008dc9"
                        }
                    }
                }
        }

    # print(type_msg)

    data = {
        "replyToken": Reply_token,
        "messages": [
            type_msg
        ]
    }

    session = requests.Session()
    response = session.post(LINE_API_REPLY, data=json.dumps(data), headers=headers)
    return 201
