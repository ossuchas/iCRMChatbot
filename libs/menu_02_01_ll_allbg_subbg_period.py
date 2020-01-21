# -*- coding: utf-8 -*-

import requests
import json
from config import LINE_API_REPLY


def replyMsg(Reply_token: str = None, bg: str = None, subbg: str = None, line_Acees_Token: str = None):
    authorization = 'Bearer {}'.format(line_Acees_Token)
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': authorization
    }

    type_msg = \
        {
            "type": "flex",
            "altText": "Flex Message",
            "contents":
                {
                    "type": "bubble",
                    "hero": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": "Please select period",
                                "color": "#FFFFFF",
                                "offsetStart": "5%"
                            }
                        ]
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "image",
                                        "url": "https://i.ibb.co/1M4dwWq/calendar-y2d-v1-0.png",
                                        "size": "full",
                                        "aspectMode": "fit",
                                        "aspectRatio": "24:7",
                                        "action": {
                                            "type": "message",
                                            "label": "action",
                                            "text": "LL Period BY SubBG As of Current [{}-{}]".format(bg, subbg)
                                        }
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "image",
                                        "url": "https://i.ibb.co/HqSJg5W/calendar-q2d-v2-0.png",
                                        "size": "full",
                                        "aspectMode": "fit",
                                        "aspectRatio": "24:7",
                                        "action": {
                                            "type": "message",
                                            "label": "action",
                                            "text": "LL Period BY SubBG Quarter [{}-{}]".format(bg, subbg)
                                        }
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "image",
                                        "url": "https://i.ibb.co/JHr4d31/calendar-w2d-v1-0.png",
                                        "size": "full",
                                        "aspectMode": "fit",
                                        "aspectRatio": "24:7",
                                        "action": {
                                            "type": "message",
                                            "label": "action",
                                            "text": "LL Period BY SubBG Week [{}-{}]".format(bg, subbg)
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": "Copyright 2019 AP PCL.",
                                "size": "xxs",
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
                        "hero": {
                            "backgroundColor": "#000000"
                        },
                        "footer": {
                            "backgroundColor": "#000000"
                        }
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
