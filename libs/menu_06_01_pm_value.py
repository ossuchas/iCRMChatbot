# -*- coding: utf-8 -*-

import requests
import json
from config import LINE_API_REPLY


def replyMsg(Reply_token: str = None, head_title: str = None, pm_val: str = None, line_Acees_Token: str = None):
    authorization = 'Bearer {}'.format(line_Acees_Token)
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': authorization
    }
    # print(pm_val)
    pm_int = int(pm_val)

    # Good -> 0 - 50 Green
    # Moderate -> 51 - 100 yellow
    # Unhealthy Sensitive Groups -> 101 - 150 Orange
    # Unhealthy -> 151 - 200 Red
    # Very Unhealthy -> 201 - 300
    status = None
    sub_status = None
    color_box = None
    face_url = None
    # pm_int = 50
    if 0 <= pm_int <= 50:  # Green
        status = "Good"
        sub_status = " "
        color_box = "#a8e05f"
        face_url = "https://i.ibb.co/yyHZMM9/ic-face-green.png"
    elif 51 <= pm_int <= 100:  # Yellow
        status = "Moderate"
        sub_status = " "
        color_box = "#ffdf58"
        face_url = "https://i.ibb.co/6t6P757/ic-face-yellow.png"
    elif 101 <= pm_int <= 150:  # Orange
        status = "Unhealthy"
        sub_status = "Sensitive Groups"
        color_box = "#ffa968"
        face_url = "https://i.ibb.co/QJvPR0W/ic-face-orange.png"
    elif 151 <= pm_int <= 200:  # Red
        status = "Unhealthy"
        sub_status = " "
        color_box = "#fe6a69"
        face_url = "https://i.ibb.co/GnqV4Wr/ic-face-red.png"
    elif 201 <= pm_int <= 300:  #
        status = "Very Unhealthy"
        sub_status = " "
        color_box = "#fe6a69"
        face_url = "https://i.ibb.co/GnqV4Wr/ic-face-red.png"

    # print(color_box, status, face_url)

    type_msg = \
        {
            "type": "flex",
            "altText": "Flex Message",
            "contents":
                {
                    "type": "bubble",
                    "size": "giga",
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                # "text": "Akoke, Bankgok, Thailand",
                                "text": head_title,
                                "gravity": "center",
                                "align": "start",
                                "size": "lg",
                                "color": "#808080"
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                    {
                                        "type": "image",
                                        # "url": "https://i.ibb.co/GnqV4Wr/ic-face-red.png",
                                        "url": f"{face_url}",
                                        "align": "start",
                                        "size": "sm",
                                        "margin": "xs",
                                        "gravity": "center"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": f"{pm_val}",
                                                "weight": "bold",
                                                "align": "center",
                                                "gravity": "center",
                                                "size": "3xl"
                                            },
                                            {
                                                "type": "text",
                                                "text": "AQI us",
                                                "align": "center",
                                                "gravity": "center"
                                            }
                                        ],
                                        "margin": "none"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": ".",
                                                # "color": "#fe6a69",
                                                "color": f"{color_box}"
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{status}",
                                                "gravity": "center",
                                                "weight": "bold",
                                                "align": "center",
                                                "size": "lg"
                                            },
                                            {
                                                "type": "text",
                                                # "text": "Sensitive Group",
                                                "text": f"{sub_status}",
                                                "size": "xs",
                                                "align": "center",
                                                "gravity": "center"
                                            }
                                        ],
                                        "margin": "md"
                                    }
                                ],
                                "backgroundColor": f"{color_box}",
                                "cornerRadius": "10px"
                            },
                            {
                                "type": "text",
                                "text": "last updated: 21/01/2020 07:36AM",
                                "align": "end",
                                "size": "xxs",
                                "style": "italic",
                                "color": "#A0A0A0"
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
