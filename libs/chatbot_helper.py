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
                    "type": "carousel",
                    "contents": [
                        {
                            "type": "bubble",
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
                                    }
                                ]
                            },
                            "hero": {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "Transfer Date At 11/12/2019",
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
                                "contents": [
                                    {
                                        "type": "separator"
                                    },
                                    {
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
                                                "text": "Unit",
                                                "align": "end",
                                                "size": "sm",
                                                "weight": "bold"
                                            },
                                            {
                                                "type": "text",
                                                "text": "Net",
                                                "align": "end",
                                                "size": "sm",
                                                "weight": "bold"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "separator"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "10077 : บ้านกลางเมือง The Era ปิ่นเกล้า-จรัญฯ",
                                                "size": "sm",
                                                "wrap": True
                                            },
                                            {
                                                "type": "text",
                                                "text": "51",
                                                "align": "end",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": "323,990,000",
                                                "align": "end",
                                                "size": "sm"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "RHYTHM สาทร",
                                                "size": "sm",
                                                "wrap": True
                                            },
                                            {
                                                "type": "text",
                                                "text": "17",
                                                "size": "sm",
                                                "align": "end"
                                            },
                                            {
                                                "type": "text",
                                                "text": "120,007,773",
                                                "size": "sm",
                                                "align": "end"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "Aspire งามวงศ์วาน",
                                                "size": "sm",
                                                "wrap": True
                                            },
                                            {
                                                "type": "text",
                                                "text": "152",
                                                "align": "end",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": "317,485,138",
                                                "align": "end",
                                                "size": "sm"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "separator",
                                        "margin": "sm"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "Grand Total",
                                                "size": "sm",
                                                "weight": "bold",
                                                "offsetStart": "10%"
                                            },
                                            {
                                                "type": "text",
                                                "text": "152",
                                                "align": "end",
                                                "size": "sm",
                                                "weight": "bold"
                                            },
                                            {
                                                "type": "text",
                                                "text": "317,485,138",
                                                "align": "end",
                                                "size": "sm",
                                                "weight": "bold"
                                            }
                                        ],
                                        "backgroundColor": "#7AFF97",
                                        "margin": "xs"
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
                                        "size": "xs",
                                        "color": "#FFFFFF",
                                        "align": "center"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "image",
                                                "url": "https://i.ibb.co/fS0B4wP/AP-Logo-2018.png",
                                                "size": "sm"
                                            }
                                        ],
                                        "position": "absolute",
                                        "width": "25px",
                                        "offsetTop": "2px"
                                    }
                                ],
                                "height": "30px"
                            },
                            "size": "giga",
                            "styles": {
                                "header": {
                                    "backgroundColor": "#000000"
                                },
                                "footer": {
                                    "backgroundColor": "#000000"
                                }
                            }
                        },
                        {
                            "type": "bubble",
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
                                    }
                                ]
                            },
                            "hero": {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "Transfer Date At 10/12/2019",
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
                                "contents": [
                                    {
                                        "type": "separator"
                                    },
                                    {
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
                                                "text": "Unit",
                                                "align": "end",
                                                "size": "sm",
                                                "weight": "bold"
                                            },
                                            {
                                                "type": "text",
                                                "text": "Net",
                                                "align": "end",
                                                "size": "sm",
                                                "weight": "bold"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "separator"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "10077 : บ้านกลางเมือง The Era ปิ่นเกล้า-จรัญฯ",
                                                "size": "sm",
                                                "wrap": True
                                            },
                                            {
                                                "type": "text",
                                                "text": "51",
                                                "align": "end",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": "323,990,000",
                                                "align": "end",
                                                "size": "sm"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "RHYTHM สาทร",
                                                "size": "sm",
                                                "wrap": True
                                            },
                                            {
                                                "type": "text",
                                                "text": "17",
                                                "size": "sm",
                                                "align": "end"
                                            },
                                            {
                                                "type": "text",
                                                "text": "120,007,773",
                                                "size": "sm",
                                                "align": "end"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "Aspire งามวงศ์วาน",
                                                "size": "sm",
                                                "wrap": True
                                            },
                                            {
                                                "type": "text",
                                                "text": "152",
                                                "align": "end",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": "317,485,138",
                                                "align": "end",
                                                "size": "sm"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "separator",
                                        "margin": "sm"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "Grand Total",
                                                "size": "sm",
                                                "weight": "bold",
                                                "offsetStart": "10%"
                                            },
                                            {
                                                "type": "text",
                                                "text": "152",
                                                "align": "end",
                                                "size": "sm",
                                                "weight": "bold"
                                            },
                                            {
                                                "type": "text",
                                                "text": "317,485,138",
                                                "align": "end",
                                                "size": "sm",
                                                "weight": "bold"
                                            }
                                        ],
                                        "backgroundColor": "#7AFF97",
                                        "margin": "xs"
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
                                        "size": "xs",
                                        "color": "#FFFFFF",
                                        "align": "center"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "image",
                                                "url": "https://i.ibb.co/fS0B4wP/AP-Logo-2018.png",
                                                "size": "sm"
                                            }
                                        ],
                                        "position": "absolute",
                                        "width": "25px",
                                        "offsetTop": "2px"
                                    }
                                ],
                                "height": "30px"
                            },
                            "size": "giga",
                            "styles": {
                                "header": {
                                    "backgroundColor": "#000000"
                                },
                                "footer": {
                                    "backgroundColor": "#000000"
                                }
                            }
                        }
                    ]
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
