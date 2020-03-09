# -*- coding: utf-8 -*-

import requests
import json
from config import LINE_API_REPLY
from models.vw_jobhelpdesk import JobHelpdeskModel
from typing import List
from datetime import datetime


def replyMsg(Reply_token: str = None, jobs: List["JobHelpdeskModel"] = None, line_Acees_Token: str = None):

    authorization = f'Bearer {line_Acees_Token}'
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': authorization
    }

    new_contents = [
        { "type": "separator", "margin": "sm" },
        { "type": "box", "layout": "baseline", "contents": [
            { "type": "text", "text": "วันที่แจ้งปัญหา", "size": "sm", "weight": "bold" },
            { "type": "text", "text": "Job No.", "size": "sm", "align": "end", "weight": "bold" },
            { "type": "text", "text": "ดูรายละเอียด", "align": "end", "size": "sm", "weight": "bold" }
        ], "backgroundColor": "#00FF9F" },
    ]

    i_count_rec = 0
    for job in jobs:

        if i_count_rec % 2 == 0:
            bg_color_row = "#FFFFFF"
        else:
            # bg_color_row = "#EBEDEF"
            bg_color_row = "#FAF5FF"

        img_search = "https://i.ibb.co/nkJRv9n/search.png"
        action = f"req_no={job.ticketnumber}"

        new_contents.append(
            {"type": "box", "layout": "horizontal",
             "contents": [{"type": "text", "text": job.requestdatetimetxt, "size": "sm", "gravity": "center"},
                          {"type": "text", "text": job.ticketnumber, "size": "sm", "wrap": True, "align": "end", "gravity": "center"},
                          {"type": "image", "url": img_search,
                           "action": {"type": "message", "label": "action", "text": action}, "size": "sm",
                           "aspectMode": "fit", "aspectRatio": "27:14", "align": "end"}
                          ],
             "backgroundColor": bg_color_row,
             "margin": "sm"
             },
        )
        i_count_rec += 1

    new_contents.append(
        {"type": "separator", "margin": "sm"},
    )
    new_contents.append(
        {"type": "text", "text": "10.03.2020 18:02 (GMT+0700)", "size": "xs", "align": "end", "color": "#8c8c8c"},
    )

    # print(i_count_rec)
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
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "Job Helpdesk",
                                        "color": "#fffffff6",
                                        "size": "xl",
                                        "weight": "bold"
                                    },
                                    {
                                        "type": "separator"
                                    },
                                    {
                                        "type": "text",
                                        "text": "Status : Open",
                                        "size": "md",
                                        "weight": "bold",
                                        "color": "#fffffff6"
                                    }
                                ]
                            }
                        ],
                        "paddingAll": "20px",
                        "backgroundColor": "#c92028",
                        "spacing": "md",
                        "height": "80px",
                        "paddingTop": "22px"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": new_contents
                        #     [
                        #     {
                        #         "type": "separator",
                        #         "margin": "sm"
                        #     },
                        #     {
                        #         "type": "box",
                        #         "layout": "baseline",
                        #         "contents": [
                        #             {
                        #                 "type": "text",
                        #                 "text": "วันที่แจ้งปัญหา",
                        #                 "size": "sm",
                        #                 "weight": "bold"
                        #             },
                        #             {
                        #                 "type": "text",
                        #                 "text": "Job No.",
                        #                 "size": "sm",
                        #                 "align": "end",
                        #                 "weight": "bold"
                        #             },
                        #             {
                        #                 "type": "text",
                        #                 "text": "ดูรายละเอียด",
                        #                 "align": "end",
                        #                 "size": "sm",
                        #                 "weight": "bold"
                        #             }
                        #         ],
                        #         "backgroundColor": "#00FF9F"
                        #     },
                        #     {
                        #         "type": "separator",
                        #         "margin": "sm"
                        #     },
                        #     {
                        #         "type": "box",
                        #         "layout": "horizontal",
                        #         "contents": [
                        #             {
                        #                 "type": "text",
                        #                 "text": "14.02.2020 13:30",
                        #                 "size": "sm"
                        #             },
                        #             {
                        #                 "type": "text",
                        #                 "text": "REQ2020002253",
                        #                 "size": "sm",
                        #                 "wrap": True,
                        #                 "align": "end"
                        #             },
                        #             {
                        #                 "type": "image",
                        #                 "url": "https://i.ibb.co/nkJRv9n/search.png",
                        #                 "action": {
                        #                     "type": "message",
                        #                     "label": "action",
                        #                     "text": "req_no=REQ2020002255"
                        #                 },
                        #                 "size": "sm",
                        #                 "aspectMode": "fit",
                        #                 "aspectRatio": "27:14",
                        #                 "align": "end"
                        #             }
                        #         ],
                        #         "margin": "sm"
                        #     },
                        #     {
                        #         "type": "box",
                        #         "layout": "horizontal",
                        #         "contents": [
                        #             {
                        #                 "type": "text",
                        #                 "text": "11.02.2020 08:13",
                        #                 "size": "sm"
                        #             },
                        #             {
                        #                 "type": "text",
                        #                 "text": "REQ2020002246",
                        #                 "size": "sm",
                        #                 "wrap": True,
                        #                 "align": "end"
                        #             },
                        #             {
                        #                 "type": "image",
                        #                 "url": "https://i.ibb.co/nkJRv9n/search.png",
                        #                 "action": {
                        #                     "type": "message",
                        #                     "label": "action",
                        #                     "text": "req_no=REQ2020002246"
                        #                 },
                        #                 "size": "sm",
                        #                 "aspectMode": "fit",
                        #                 "aspectRatio": "27:14",
                        #                 "align": "end"
                        #             }
                        #         ],
                        #         "backgroundColor": "#FAF5FF",
                        #         "margin": "sm"
                        #     },
                        #     {
                        #         "type": "separator",
                        #         "margin": "sm"
                        #     },
                        #     {
                        #         "type": "text",
                        #         "text": "10.03.2020 18:02 (GMT+0700)",
                        #         "size": "xs",
                        #         "align": "end",
                        #         "color": "#8c8c8c"
                        #     }
                        # ]
                    },
                    "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": "Copyright 2020 AP (Thailand) PCL.",
                                "align": "center",
                                "size": "xs",
                                "color": "#FFFFFF"
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
                                "height": "30px",
                                "width": "32px",
                                "offsetBottom": "3px"
                            }
                        ],
                        "backgroundColor": "#000000"
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
    # return 201
