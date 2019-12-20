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


def replyMsg(reply_token: str = None, text_msg: str = None, line_aceess_token: str = None) -> int:
    authorization = 'Bearer {}'.format(line_aceess_token)
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': authorization
    }
    # print(values)
    # value = [(100, 10), (200, 20), (300, 30)]

    flex_msg = {
        "type": "flex",
        "altText": "this is a flex message",
        "contents":
            {
                "type": "carousel",
                "contents": [
                    {
                        "type": "bubble",
                        "header": {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                        {
                                            "type": "image",
                                            "url": "https://apthai.cdnboost.com/stocks/project/o0x0/57/yj/fif557yjpw/gallery_img_1.jpg",
                                            "size": "full",
                                            "aspectMode": "cover",
                                            "aspectRatio": "150:196",
                                            "gravity": "center",
                                            "flex": 1
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [
                                                {
                                                    "type": "image",
                                                    "url": "https://apthai.cdnboost.com/stocks/project/o0x0/36/mc/fif536mcff/gallery_img_1.jpg",
                                                    "size": "full",
                                                    "aspectMode": "cover",
                                                    "aspectRatio": "150:98",
                                                    "gravity": "center"
                                                },
                                                {
                                                    "type": "image",
                                                    "url": "https://apthai.cdnboost.com/stocks/project/o0x0/zg/bc/fifyzgbcs0/de-beers.jpg",
                                                    "size": "full",
                                                    "aspectMode": "cover",
                                                    "aspectRatio": "150:98",
                                                    "gravity": "center"
                                                }
                                            ],
                                            "flex": 1
                                        },
                                        {
                                            "type": "box",
                                            "layout": "horizontal",
                                            "contents": [
                                                {
                                                    "type": "text",
                                                    "text": "NEW",
                                                    "size": "xs",
                                                    "color": "#ffffff",
                                                    "align": "center",
                                                    "gravity": "center"
                                                }
                                            ],
                                            "backgroundColor": "#EC3D44",
                                            "paddingAll": "2px",
                                            "paddingStart": "4px",
                                            "paddingEnd": "4px",
                                            "flex": 0,
                                            "position": "absolute",
                                            "offsetStart": "18px",
                                            "offsetTop": "18px",
                                            "cornerRadius": "100px",
                                            "width": "48px",
                                            "height": "25px"
                                        }
                                    ]
                                }
                            ],
                            "paddingAll": "0px"
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
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [
                                                {
                                                    "type": "text",
                                                    "contents": [
                                                    ],
                                                    "size": "xl",
                                                    "wrap": True,
                                                    "text": "The City สะพานมหาเจษฎาบดินทร์ฯ",
                                                    "color": "#ffffff",
                                                    "weight": "bold"
                                                }
                                            ],
                                            "spacing": "sm"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [
                                                {
                                                    "type": "box",
                                                    "layout": "vertical",
                                                    "contents": [
                                                        {
                                                            "type": "text",
                                                            "contents": [
                                                            ],
                                                            "size": "sm",
                                                            "wrap": True,
                                                            "margin": "lg",
                                                            "color": "#ffffffde",
                                                            "text": "เปิดจองบ้านหรู 5 นอน 380ตรม. โครงการใหม่ล่าสุด บนทำเลเชื่อมศักยภาพ 20 น.ถึงจตุจักร* ใกล้รถไฟฟ้าสีม่วง เริ่ม 15.9-25.9ลบ"
                                                        }
                                                    ]
                                                }
                                            ],
                                            "paddingAll": "13px",
                                            "backgroundColor": "#ffffff1A",
                                            "cornerRadius": "2px",
                                            "margin": "xl"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "horizontal",
                                            "contents": [
                                                {
                                                    "type": "button",
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "แผนที่",
                                                        "uri": "https://goo.gl/maps/VXRYuWGtvWHdm98e6"
                                                    },
                                                    "color": "#ffffffde",
                                                    "flex": 0
                                                },
                                                {
                                                    "type": "button",
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "สนใจโครงการ",
                                                        "uri": "https://www.apthai.com/th/%E0%B8%9A%E0%B9%89%E0%B8%B2%E0%B8%99%E0%B9%80%E0%B8%94%E0%B8%B5%E0%B9%88%E0%B8%A2%E0%B8%A7/the-city/the-city-%E0%B8%AA%E0%B8%B0%E0%B8%9E%E0%B8%B2%E0%B8%99%E0%B8%A1%E0%B8%AB%E0%B8%B2%E0%B9%80%E0%B8%88%E0%B8%A9%E0%B8%8E%E0%B8%B2%E0%B8%9A%E0%B8%94%E0%B8%B4%E0%B8%99%E0%B8%97%E0%B8%A3%E0%B9%8C%E0%B8%AF"
                                                    },
                                                    "color": "#ffffffde"
                                                }
                                            ]
                                        }
                                    ]
                                }
                            ],
                            "paddingAll": "20px",
                            "backgroundColor": "#464F69"
                        }
                    },
                    {
                        "type": "bubble",
                        "header": {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                        {
                                            "type": "image",
                                            "url": "https://apthai.cdnboost.com/stocks/project/o0x0/xu/j3/fhdlxuj3qu/Shine.jpg",
                                            "size": "full",
                                            "aspectMode": "cover",
                                            "aspectRatio": "150:196",
                                            "gravity": "center",
                                            "flex": 1
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [
                                                {
                                                    "type": "image",
                                                    "url": "https://apthai.cdnboost.com/stocks/project/o0x0/ck/zg/fhdlckzg6t/gallery_img_2.jpg",
                                                    "size": "full",
                                                    "aspectMode": "cover",
                                                    "aspectRatio": "150:98",
                                                    "gravity": "center"
                                                },
                                                {
                                                    "type": "image",
                                                    "url": "https://apthai.cdnboost.com/stocks/project/o0x0/ex/4f/fhdlex4fsu/gallery_img_1.jpg",
                                                    "size": "full",
                                                    "aspectMode": "cover",
                                                    "aspectRatio": "150:98",
                                                    "gravity": "center"
                                                }
                                            ],
                                            "flex": 1
                                        },
                                        {
                                            "type": "box",
                                            "layout": "horizontal",
                                            "contents": [
                                                {
                                                    "type": "text",
                                                    "text": "NEW",
                                                    "size": "xs",
                                                    "color": "#ffffff",
                                                    "align": "center",
                                                    "gravity": "center"
                                                }
                                            ],
                                            "backgroundColor": "#EC3D44",
                                            "paddingAll": "2px",
                                            "paddingStart": "4px",
                                            "paddingEnd": "4px",
                                            "flex": 0,
                                            "position": "absolute",
                                            "offsetStart": "18px",
                                            "offsetTop": "18px",
                                            "cornerRadius": "100px",
                                            "width": "48px",
                                            "height": "25px"
                                        }
                                    ]
                                }
                            ],
                            "paddingAll": "0px"
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
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [
                                                {
                                                    "type": "text",
                                                    "contents": [
                                                    ],
                                                    "size": "xl",
                                                    "wrap": True,
                                                    "text": "Centro วงแหวน - จตุโชติ",
                                                    "color": "#ffffff",
                                                    "weight": "bold"
                                                }
                                            ],
                                            "spacing": "sm"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [
                                                {
                                                    "type": "box",
                                                    "layout": "vertical",
                                                    "contents": [
                                                        {
                                                            "type": "text",
                                                            "contents": [
                                                            ],
                                                            "size": "sm",
                                                            "wrap": True,
                                                            "margin": "lg",
                                                            "color": "#ffffffde",
                                                            "text": "พบโปรไฮบริดส่งท้ายปี บ้านพร้อมเฟอร์ฯ 500,000* กับบ้านเดี่ยว 255 ตร.ม. 4นอน 3จอด 5นาทีถึงทางด่วนรามอินทรา* รับเฟอร์นิเจอร์+สมาร์ทโฮม+แอร์* พร้อมเข้าอยู่ทันที เริ่ม 5.49-9 ล้าน* ลงทะเบียนรับสิทธิ์ภายในปี 2562 เท่านั้น"
                                                        }
                                                    ]
                                                }
                                            ],
                                            "paddingAll": "13px",
                                            "backgroundColor": "#ffffff1A",
                                            "cornerRadius": "2px",
                                            "margin": "xl"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "horizontal",
                                            "contents": [
                                                {
                                                    "type": "button",
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "แผนที่",
                                                        "uri": "https://goo.gl/maps/ZrGKmSjLegR5y25R8"
                                                    },
                                                    "color": "#ffffffde",
                                                    "flex": 0
                                                },
                                                {
                                                    "type": "button",
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "สนใจโครงการ",
                                                        "uri": "https://www.apthai.com/th/%E0%B8%9A%E0%B9%89%E0%B8%B2%E0%B8%99%E0%B9%80%E0%B8%94%E0%B8%B5%E0%B9%88%E0%B8%A2%E0%B8%A7/centro/centro-%E0%B8%A7%E0%B8%87%E0%B9%81%E0%B8%AB%E0%B8%A7%E0%B8%99-%E0%B8%88%E0%B8%95%E0%B8%B8%E0%B9%82%E0%B8%8A%E0%B8%95%E0%B8%B4"
                                                    },
                                                    "color": "#ffffffde"
                                                }
                                            ]
                                        }
                                    ]
                                }
                            ],
                            "paddingAll": "20px",
                            "backgroundColor": "#464F69"
                        }
                    },
                    {
                        "type": "bubble",
                        "header": {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                        {
                                            "type": "image",
                                            "url": "https://apthai.cdnboost.com/stocks/project/o0x0/7i/h4/fdy47ih4pl/2.jpg",
                                            "size": "full",
                                            "aspectMode": "cover",
                                            "aspectRatio": "150:196",
                                            "gravity": "center",
                                            "flex": 1
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [
                                                {
                                                    "type": "image",
                                                    "url": "https://apthai.cdnboost.com/stocks/project/o0x0/eb/q6/fdy4ebq6ga/21.jpg",
                                                    "size": "full",
                                                    "aspectMode": "cover",
                                                    "aspectRatio": "150:98",
                                                    "gravity": "center"
                                                },
                                                {
                                                    "type": "image",
                                                    "url": "https://apthai.cdnboost.com/stocks/project/o0x0/ib/l2/fajtibl26r/City_Spacious.jpg",
                                                    "size": "full",
                                                    "aspectMode": "cover",
                                                    "aspectRatio": "150:98",
                                                    "gravity": "center"
                                                }
                                            ],
                                            "flex": 1
                                        },
                                        {
                                            "type": "box",
                                            "layout": "horizontal",
                                            "contents": [
                                                {
                                                    "type": "text",
                                                    "text": "NEW",
                                                    "size": "xs",
                                                    "color": "#ffffff",
                                                    "align": "center",
                                                    "gravity": "center"
                                                }
                                            ],
                                            "backgroundColor": "#EC3D44",
                                            "paddingAll": "2px",
                                            "paddingStart": "4px",
                                            "paddingEnd": "4px",
                                            "flex": 0,
                                            "position": "absolute",
                                            "offsetStart": "18px",
                                            "offsetTop": "18px",
                                            "cornerRadius": "100px",
                                            "width": "48px",
                                            "height": "25px"
                                        }
                                    ]
                                }
                            ],
                            "paddingAll": "0px"
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
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [
                                                {
                                                    "type": "text",
                                                    "contents": [
                                                    ],
                                                    "size": "xl",
                                                    "wrap": True,
                                                    "text": "THE CITY ราชพฤกษ์ - สวนผัก",
                                                    "color": "#ffffff",
                                                    "weight": "bold"
                                                }
                                            ],
                                            "spacing": "sm"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [
                                                {
                                                    "type": "box",
                                                    "layout": "vertical",
                                                    "contents": [
                                                        {
                                                            "type": "text",
                                                            "contents": [
                                                            ],
                                                            "size": "sm",
                                                            "wrap": True,
                                                            "margin": "lg",
                                                            "color": "#ffffffde",
                                                            "text": "'โปรส่งท้ายปี' บ้านหรูพร้อมนวัตกรรมใหม่ ลดทันที! 1,000,000 บ* บ้านเดี่ยวหลังใหญ่ แปลงมุม 100 ตร.วา. บนโซนส่วนตัวที่สุด ใจกลางราชพฤกษ์ พร้อมทางลัดส่วนตัว 5 นาที ถึงทางด่วนศรีรัชฯ* เริ่ม 12.99 - 24 ล้าน*"
                                                        }
                                                    ]
                                                }
                                            ],
                                            "paddingAll": "13px",
                                            "backgroundColor": "#ffffff1A",
                                            "cornerRadius": "2px",
                                            "margin": "xl"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "horizontal",
                                            "contents": [
                                                {
                                                    "type": "button",
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "แผนที่",
                                                        "uri": "https://goo.gl/maps/frBHvLcNvBVGGRWN8"
                                                    },
                                                    "color": "#ffffffde",
                                                    "flex": 0
                                                },
                                                {
                                                    "type": "button",
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "สนใจโครงการ",
                                                        "uri": "https://www.apthai.com/th/%E0%B8%9A%E0%B9%89%E0%B8%B2%E0%B8%99%E0%B9%80%E0%B8%94%E0%B8%B5%E0%B9%88%E0%B8%A2%E0%B8%A7/the-city/the-city-%E0%B8%A3%E0%B8%B2%E0%B8%8A%E0%B8%9E%E0%B8%A4%E0%B8%81%E0%B8%A9%E0%B9%8C-%E0%B8%AA%E0%B8%A7%E0%B8%99%E0%B8%9C%E0%B8%B1%E0%B8%81"
                                                    },
                                                    "color": "#ffffffde"
                                                }
                                            ]
                                        }
                                    ]
                                }
                            ],
                            "paddingAll": "20px",
                            "backgroundColor": "#464F69"
                        }
                    }
                ]
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
