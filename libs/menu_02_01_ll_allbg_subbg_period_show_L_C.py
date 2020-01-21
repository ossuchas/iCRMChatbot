# -*- coding: utf-8 -*-

import requests
import json
from config import LINE_API_REPLY
from models.crm_line_ll_data import LeadLagModel


def replyMsg(Reply_token: str = None, bg: str = None,
             subbg: str = None,
             ll: LeadLagModel = None,
             ll_l: LeadLagModel = None,
             line_Acees_Token: str = None):

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
                    "type": "carousel",
                    "contents": [
                        {
                            "type": "bubble",
                            "size": "giga",
                            "header": {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "Lead Lag",
                                        "color": "#FFFFFF",
                                        "size": "lg",
                                        "weight": "bold"
                                    },
                                    {
                                        "type": "text",
                                        "text": ll_l.text_msg_header,
                                        "align": "end",
                                        "color": "#FFFFFF",
                                        "weight": "bold"
                                    },
                                    {
                                        "type": "text",
                                        "text": ll_l.text_msg,
                                        "position": "absolute",
                                        "color": "#FFFFFF",
                                        "size": "xs",
                                        "style": "italic",
                                        "offsetEnd": "17px",
                                        "offsetBottom": "2px"
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
                                                "text": "รายการ",
                                                "size": "xs",
                                                "color": "#4FFFBD"
                                            },
                                            {
                                                "type": "text",
                                                "text": "Target",
                                                "size": "sm",
                                                "align": "end",
                                                "weight": "bold",
                                                "position": "absolute",
                                                "offsetBottom": "1px",
                                                "offsetStart": "59%"
                                            },
                                            {
                                                "type": "text",
                                                "text": "Actual",
                                                "size": "sm",
                                                "align": "end",
                                                "weight": "bold"
                                            },
                                            {
                                                "type": "icon",
                                                "url": "https://i.ibb.co/Ws37N5t/icon-tmp.png",
                                                "margin": "lg"
                                            }
                                        ],
                                        "backgroundColor": "#4FFFBD"
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
                                                "text": "โอน (MB)",
                                                "size": "xs",
                                                "flex": 0
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{ll_l.tg_transferamount:,.0f}",
                                                "size": "xs",
                                                "align": "end",
                                                "position": "absolute",
                                                "offsetBottom": "1px",
                                                "offsetEnd": "31%"
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{ll_l.at_transferamount:,.0f}",
                                                "size": "xs",
                                                "align": "end"
                                            },
                                            {
                                                "type": "icon",
                                                "url": ll_l.icon_transferamount,
                                                "margin": "lg",
                                                "offsetTop": "2px"
                                            }
                                        ],
                                        "backgroundColor": "#FAF5FF"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "โอน (Unit)",
                                                "size": "xs",
                                                "flex": 0
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{ll_l.tg_transferunit:,.0f}",
                                                "size": "xs",
                                                "align": "end",
                                                "position": "absolute",
                                                "offsetBottom": "1px",
                                                "offsetEnd": "31%"
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{ll_l.at_transferunit:,.0f}",
                                                "size": "xs",
                                                "align": "end"
                                            },
                                            {
                                                "type": "icon",
                                                "url": ll_l.icon_transferunit,
                                                "margin": "lg",
                                                "offsetTop": "2px"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "ห้องผ่าน QC",
                                                "size": "xs",
                                                "flex": 0
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{ll_l.tg_qcpass:,.0f}",
                                                "size": "xs",
                                                "position": "absolute",
                                                "offsetBottom": "1px",
                                                "align": "end",
                                                "offsetEnd": "31%"
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{ll_l.at_qcpass:,.0f}",
                                                "size": "xs",
                                                "align": "end"
                                            },
                                            {
                                                "type": "icon",
                                                "url": ll_l.icon_qcpass,
                                                "margin": "lg",
                                                "offsetTop": "2px"
                                            }
                                        ],
                                        "backgroundColor": "#FAF5FF"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "ลูกค้าเข้าตรวจ",
                                                "size": "xs",
                                                "flex": 0
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{ll_l.tg_checkunit:,.0f}",
                                                "size": "xs",
                                                "position": "absolute",
                                                "align": "end",
                                                "offsetBottom": "1px",
                                                "offsetEnd": "31%"
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{ll_l.at_checkunit:,.0f}",
                                                "size": "xs",
                                                "align": "end"
                                            },
                                            {
                                                "type": "icon",
                                                "url": ll_l.icon_checkunit,
                                                "margin": "lg"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "ลูกค้ารับห้อง",
                                                "size": "xs",
                                                "flex": 0
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{ll_l.tg_acceptunit:,.0f}",
                                                "size": "xs",
                                                "align": "end",
                                                "position": "absolute",
                                                "offsetBottom": "1px",
                                                "offsetEnd": "31%"
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{ll_l.at_acceptunit:,.0f}",
                                                "size": "xs",
                                                "align": "end"
                                            },
                                            {
                                                "type": "icon",
                                                "url": ll_l.icon_acceptunit,
                                                "margin": "lg"
                                            }
                                        ],
                                        "backgroundColor": "#FAF5FF"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "โอนสด + Bankอนุมัติ",
                                                "size": "xs",
                                                "wrap": True,
                                                "flex": 0
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{ll_l.tg_bankapprove:,.0f}",
                                                "size": "xs",
                                                "align": "end",
                                                "flex": 2,
                                                "position": "absolute",
                                                "offsetBottom": "1px",
                                                "offsetEnd": "31%"
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{ll_l.at_bankapprove:,.0f}",
                                                "size": "xs",
                                                "align": "end"
                                            },
                                            {
                                                "type": "icon",
                                                "url": ll_l.icon_bankapprove,
                                                "margin": "lg"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "Grs. Presale(MB)",
                                                "size": "xs",
                                                "wrap": True,
                                                "flex": 0
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{ll_l.tg_grosspresalesamount:,.0f}",
                                                "size": "xs",
                                                "align": "end",
                                                "position": "absolute",
                                                "offsetBottom": "1px",
                                                "offsetEnd": "31%"
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{ll_l.at_grosspresalesamount:,.0f}",
                                                "size": "xs",
                                                "align": "end"
                                            },
                                            {
                                                "type": "icon",
                                                "url": ll_l.icon_grosspresalesamount,
                                                "margin": "lg"
                                            }
                                        ],
                                        "backgroundColor": "#FAF5FF"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "Net Presale (MB)",
                                                "size": "xs",
                                                "flex": 0
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{ll_l.tg_netpresalesamount:,.0f}",
                                                "size": "xs",
                                                "align": "end",
                                                "position": "absolute",
                                                "offsetBottom": "1px",
                                                "offsetEnd": "31%"
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{ll_l.at_netpresalesamount:,.0f}",
                                                "size": "xs",
                                                "align": "end"
                                            },
                                            {
                                                "type": "icon",
                                                "url": ll_l.icon_netpresalesamount,
                                                "margin": "lg"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "Net Presale (MB) - รอยกเลิก",
                                                "size": "xs",
                                                "wrap": True,
                                                "flex": 0
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{ll_l.tg_netpresales_precancelamount:,.0f}",
                                                "size": "xs",
                                                "align": "end",
                                                "flex": 1,
                                                "margin": "xxl",
                                                "position": "absolute",
                                                "offsetBottom": "1px",
                                                "offsetEnd": "31%"
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{ll_l.at_netpresales_precancelamount:,.0f}",
                                                "size": "xs",
                                                "align": "end"
                                            },
                                            {
                                                "type": "icon",
                                                "url": ll_l.icon_netpresales_precancelamount,
                                                "margin": "lg"
                                            }
                                        ],
                                        "backgroundColor": "#FAF5FF"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "รอยกเลิก (MB)",
                                                "size": "xs",
                                                "flex": 0
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{ll_l.tg_precancelamount:,.0f}",
                                                "size": "xs",
                                                "align": "end",
                                                "position": "absolute",
                                                "offsetBottom": "1px",
                                                "offsetEnd": "31%"
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{ll_l.at_precancelamount:,.0f}",
                                                "size": "xs",
                                                "align": "end"
                                            },
                                            {
                                                "type": "icon",
                                                "url": ll_l.icon_precancelamount,
                                                "margin": "lg"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "Grs. Presale (Units)",
                                                "size": "xs",
                                                "flex": 0
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{ll_l.tg_grosspresalesunit:,.0f}",
                                                "size": "xs",
                                                "align": "end",
                                                "flex": 2,
                                                "position": "absolute",
                                                "offsetBottom": "1px",
                                                "offsetEnd": "31%"
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{ll_l.at_grosspresalesunit:,.0f}",
                                                "size": "xs",
                                                "align": "end"
                                            },
                                            {
                                                "type": "icon",
                                                "url": ll_l.icon_grosspresalesunit,
                                                "margin": "lg"
                                            }
                                        ],
                                        "backgroundColor": "#FAF5FF"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "Net Presale (Units)",
                                                "size": "xs",
                                                "wrap": True,
                                                "flex": 0
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{ll_l.tg_netpresalesunit:,.0f}",
                                                "size": "xs",
                                                "align": "end",
                                                "position": "absolute",
                                                "offsetBottom": "1px",
                                                "offsetEnd": "31%"
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{ll_l.at_netpresalesunit:,.0f}",
                                                "size": "xs",
                                                "align": "end"
                                            },
                                            {
                                                "type": "icon",
                                                "url": ll_l.icon_netpresalesunit,
                                                "margin": "lg"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "Net Presales (Unit) - รอยกเลิก",
                                                "size": "xs",
                                                "wrap": True,
                                                "flex": 0
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{ll_l.tg_netpresales_precancelunit:,.0f}",
                                                "size": "xs",
                                                "align": "end",
                                                "position": "absolute",
                                                "offsetBottom": "1px",
                                                "offsetEnd": "31%"
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{ll_l.at_netpresales_precancelunit:,.0f}",
                                                "size": "xs",
                                                "align": "end"
                                            },
                                            {
                                                "type": "icon",
                                                "url": ll_l.icon_netpresales_precancelunit,
                                                "margin": "lg"
                                            }
                                        ],
                                        "backgroundColor": "#FAF5FF"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "รอยกเลิก (Units)",
                                                "size": "xs",
                                                "flex": 0
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{ll_l.tg_precancelunit:,.0f}",
                                                "size": "xs",
                                                "align": "end",
                                                "position": "absolute",
                                                "offsetBottom": "1px",
                                                "offsetEnd": "31%"
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{ll_l.at_precancelunit:,.0f}",
                                                "size": "xs",
                                                "align": "end"
                                            },
                                            {
                                                "type": "icon",
                                                "url": ll_l.icon_precancelunit,
                                                "margin": "lg"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "Walk",
                                                "size": "xs",
                                                "flex": 0
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{ll_l.tg_walk:,.0f}",
                                                "size": "xs",
                                                "align": "end",
                                                "position": "absolute",
                                                "offsetBottom": "1px",
                                                "offsetEnd": "31%"
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{ll_l.at_walk:,.0f}",
                                                "size": "xs",
                                                "align": "end"
                                            },
                                            {
                                                "type": "icon",
                                                "url": ll_l.icon_walk,
                                                "margin": "lg"
                                            }
                                        ],
                                        "backgroundColor": "#FAF5FF"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "2nd Walk++",
                                                "size": "xs",
                                                "flex": 0
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{ll_l.tg_walk2:,.0f}",
                                                "size": "xs",
                                                "align": "end",
                                                "position": "absolute",
                                                "offsetBottom": "1px",
                                                "offsetEnd": "31%"
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{ll_l.at_walk2:,.0f}",
                                                "size": "xs",
                                                "align": "end"
                                            },
                                            {
                                                "type": "icon",
                                                "url": ll_l.icon_walk2,
                                                "margin": "lg"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "Conversion",
                                                "size": "xs",
                                                "flex": 0
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{ll_l.tg_conversion:,.0f}",
                                                "size": "xs",
                                                "align": "end",
                                                "position": "absolute",
                                                "offsetBottom": "1px",
                                                "offsetEnd": "31%"
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{ll_l.at_conversion:,.0f}",
                                                "size": "xs",
                                                "align": "end"
                                            },
                                            {
                                                "type": "icon",
                                                "url": ll_l.icon_conversion,
                                                "margin": "lg"
                                            }
                                        ],
                                        "backgroundColor": "#FAF5FF"
                                    },
                                    {
                                        "type": "separator"
                                    }
                                ]
                            },
                            "footer": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "Copyright 2019 AP (Thailand) PCL.",
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
                                ]
                            },
                            "styles": {
                                "header": {
                                    "backgroundColor": "#000000"
                                },
                                "hero": {
                                    "backgroundColor": "#000000"
                                },
                                "footer": {
                                    "backgroundColor": "#000000"
                                }
                            }
                        },
                        {
                            "type": "bubble",
                            "size": "giga",
                            "header": {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "Lead Lag",
                                        "color": "#FFFFFF",
                                        "size": "lg",
                                        "weight": "bold"
                                    },
                                    {
                                        "type": "text",
                                        "text": ll.text_msg_header,
                                        "align": "end",
                                        "color": "#FFFFFF",
                                        "weight": "bold"
                                    },
                                    {
                                        "type": "text",
                                        "text": ll.text_msg,
                                        "position": "absolute",
                                        "color": "#FFFFFF",
                                        "size": "xs",
                                        "style": "italic",
                                        "offsetEnd": "17px",
                                        "offsetBottom": "2px"
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
                                                "text": "รายการ",
                                                "size": "xs",
                                                "color": "#4FFFBD"
                                            },
                                            {
                                                "type": "text",
                                                "text": "Target",
                                                "size": "sm",
                                                "align": "end",
                                                "weight": "bold",
                                                "position": "absolute",
                                                "offsetBottom": "1px",
                                                "offsetStart": "59%"
                                            },
                                            {
                                                "type": "text",
                                                "text": "Actual",
                                                "size": "sm",
                                                "align": "end",
                                                "weight": "bold"
                                            },
                                            {
                                                "type": "icon",
                                                "url": "https://i.ibb.co/Ws37N5t/icon-tmp.png",
                                                "margin": "lg"
                                            }
                                        ],
                                        "backgroundColor": "#4FFFBD"
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
                                                "text": "โอน (MB)",
                                                "size": "xs",
                                                "flex": 0
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{ll.tg_transferamount:,.0f}",
                                                "size": "xs",
                                                "align": "end",
                                                "position": "absolute",
                                                "offsetBottom": "1px",
                                                "offsetEnd": "31%"
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{ll.at_transferamount:,.0f}",
                                                "size": "xs",
                                                "align": "end"
                                            },
                                            {
                                                "type": "icon",
                                                "url": ll.icon_transferamount,
                                                "margin": "lg",
                                                "offsetTop": "2px"
                                            }
                                        ],
                                        "backgroundColor": "#FAF5FF"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "โอน (Unit)",
                                                "size": "xs",
                                                "flex": 0
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{ll.tg_transferunit:,.0f}",
                                                "size": "xs",
                                                "align": "end",
                                                "position": "absolute",
                                                "offsetBottom": "1px",
                                                "offsetEnd": "31%"
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{ll.at_transferunit:,.0f}",
                                                "size": "xs",
                                                "align": "end"
                                            },
                                            {
                                                "type": "icon",
                                                "url": ll.icon_transferunit,
                                                "margin": "lg",
                                                "offsetTop": "2px"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "ห้องผ่าน QC",
                                                "size": "xs",
                                                "flex": 0
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{ll.tg_qcpass:,.0f}",
                                                "size": "xs",
                                                "position": "absolute",
                                                "offsetBottom": "1px",
                                                "align": "end",
                                                "offsetEnd": "31%"
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{ll.at_qcpass:,.0f}",
                                                "size": "xs",
                                                "align": "end"
                                            },
                                            {
                                                "type": "icon",
                                                "url": ll.icon_qcpass,
                                                "margin": "lg",
                                                "offsetTop": "2px"
                                            }
                                        ],
                                        "backgroundColor": "#FAF5FF"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "ลูกค้าเข้าตรวจ",
                                                "size": "xs",
                                                "flex": 0
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{ll.tg_checkunit:,.0f}",
                                                "size": "xs",
                                                "position": "absolute",
                                                "align": "end",
                                                "offsetBottom": "1px",
                                                "offsetEnd": "31%"
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{ll.at_checkunit:,.0f}",
                                                "size": "xs",
                                                "align": "end"
                                            },
                                            {
                                                "type": "icon",
                                                "url": ll.icon_checkunit,
                                                "margin": "lg"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "ลูกค้ารับห้อง",
                                                "size": "xs",
                                                "flex": 0
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{ll.tg_acceptunit:,.0f}",
                                                "size": "xs",
                                                "align": "end",
                                                "position": "absolute",
                                                "offsetBottom": "1px",
                                                "offsetEnd": "31%"
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{ll.at_acceptunit:,.0f}",
                                                "size": "xs",
                                                "align": "end"
                                            },
                                            {
                                                "type": "icon",
                                                "url": ll.icon_acceptunit,
                                                "margin": "lg"
                                            }
                                        ],
                                        "backgroundColor": "#FAF5FF"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "โอนสด + Bankอนุมัติ",
                                                "size": "xs",
                                                "wrap": True,
                                                "flex": 0
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{ll.tg_bankapprove:,.0f}",
                                                "size": "xs",
                                                "align": "end",
                                                "flex": 2,
                                                "position": "absolute",
                                                "offsetBottom": "1px",
                                                "offsetEnd": "31%"
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{ll.at_bankapprove:,.0f}",
                                                "size": "xs",
                                                "align": "end"
                                            },
                                            {
                                                "type": "icon",
                                                "url": ll.icon_bankapprove,
                                                "margin": "lg"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "Grs. Presale(MB)",
                                                "size": "xs",
                                                "wrap": True,
                                                "flex": 0
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{ll.tg_grosspresalesamount:,.0f}",
                                                "size": "xs",
                                                "align": "end",
                                                "position": "absolute",
                                                "offsetBottom": "1px",
                                                "offsetEnd": "31%"
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{ll.at_grosspresalesamount:,.0f}",
                                                "size": "xs",
                                                "align": "end"
                                            },
                                            {
                                                "type": "icon",
                                                "url": ll.icon_grosspresalesamount,
                                                "margin": "lg"
                                            }
                                        ],
                                        "backgroundColor": "#FAF5FF"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "Net Presale (MB)",
                                                "size": "xs",
                                                "flex": 0
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{ll.tg_netpresalesamount:,.0f}",
                                                "size": "xs",
                                                "align": "end",
                                                "position": "absolute",
                                                "offsetBottom": "1px",
                                                "offsetEnd": "31%"
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{ll.at_netpresalesamount:,.0f}",
                                                "size": "xs",
                                                "align": "end"
                                            },
                                            {
                                                "type": "icon",
                                                "url": ll.icon_netpresalesamount,
                                                "margin": "lg"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "Net Presale (MB) - รอยกเลิก",
                                                "size": "xs",
                                                "wrap": True,
                                                "flex": 0
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{ll.tg_netpresales_precancelamount:,.0f}",
                                                "size": "xs",
                                                "align": "end",
                                                "flex": 1,
                                                "margin": "xxl",
                                                "position": "absolute",
                                                "offsetBottom": "1px",
                                                "offsetEnd": "31%"
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{ll.at_netpresales_precancelamount:,.0f}",
                                                "size": "xs",
                                                "align": "end"
                                            },
                                            {
                                                "type": "icon",
                                                "url": ll.icon_netpresales_precancelamount,
                                                "margin": "lg"
                                            }
                                        ],
                                        "backgroundColor": "#FAF5FF"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "รอยกเลิก (MB)",
                                                "size": "xs",
                                                "flex": 0
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{ll.tg_precancelamount:,.0f}",
                                                "size": "xs",
                                                "align": "end",
                                                "position": "absolute",
                                                "offsetBottom": "1px",
                                                "offsetEnd": "31%"
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{ll.at_precancelamount:,.0f}",
                                                "size": "xs",
                                                "align": "end"
                                            },
                                            {
                                                "type": "icon",
                                                "url": ll.icon_precancelamount,
                                                "margin": "lg"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "Grs. Presale (Units)",
                                                "size": "xs",
                                                "flex": 0
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{ll.tg_grosspresalesunit:,.0f}",
                                                "size": "xs",
                                                "align": "end",
                                                "flex": 2,
                                                "position": "absolute",
                                                "offsetBottom": "1px",
                                                "offsetEnd": "31%"
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{ll.at_grosspresalesunit:,.0f}",
                                                "size": "xs",
                                                "align": "end"
                                            },
                                            {
                                                "type": "icon",
                                                "url": ll.icon_grosspresalesunit,
                                                "margin": "lg"
                                            }
                                        ],
                                        "backgroundColor": "#FAF5FF"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "Net Presale (Units)",
                                                "size": "xs",
                                                "wrap": True,
                                                "flex": 0
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{ll.tg_netpresalesunit:,.0f}",
                                                "size": "xs",
                                                "align": "end",
                                                "position": "absolute",
                                                "offsetBottom": "1px",
                                                "offsetEnd": "31%"
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{ll.at_netpresalesunit:,.0f}",
                                                "size": "xs",
                                                "align": "end"
                                            },
                                            {
                                                "type": "icon",
                                                "url": ll.icon_netpresalesunit,
                                                "margin": "lg"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "Net Presales (Unit) - รอยกเลิก",
                                                "size": "xs",
                                                "wrap": True,
                                                "flex": 0
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{ll.tg_netpresales_precancelunit:,.0f}",
                                                "size": "xs",
                                                "align": "end",
                                                "position": "absolute",
                                                "offsetBottom": "1px",
                                                "offsetEnd": "31%"
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{ll.at_netpresales_precancelunit:,.0f}",
                                                "size": "xs",
                                                "align": "end"
                                            },
                                            {
                                                "type": "icon",
                                                "url": ll.icon_netpresales_precancelunit,
                                                "margin": "lg"
                                            }
                                        ],
                                        "backgroundColor": "#FAF5FF"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "รอยกเลิก (Units)",
                                                "size": "xs",
                                                "flex": 0
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{ll.tg_precancelunit:,.0f}",
                                                "size": "xs",
                                                "align": "end",
                                                "position": "absolute",
                                                "offsetBottom": "1px",
                                                "offsetEnd": "31%"
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{ll.at_precancelunit:,.0f}",
                                                "size": "xs",
                                                "align": "end"
                                            },
                                            {
                                                "type": "icon",
                                                "url": ll.icon_precancelunit,
                                                "margin": "lg"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "Walk",
                                                "size": "xs",
                                                "flex": 0
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{ll.tg_walk:,.0f}",
                                                "size": "xs",
                                                "align": "end",
                                                "position": "absolute",
                                                "offsetBottom": "1px",
                                                "offsetEnd": "31%"
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{ll.at_walk:,.0f}",
                                                "size": "xs",
                                                "align": "end"
                                            },
                                            {
                                                "type": "icon",
                                                "url": ll.icon_walk,
                                                "margin": "lg"
                                            }
                                        ],
                                        "backgroundColor": "#FAF5FF"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "2nd Walk++",
                                                "size": "xs",
                                                "flex": 0
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{ll.tg_walk2:,.0f}",
                                                "size": "xs",
                                                "align": "end",
                                                "position": "absolute",
                                                "offsetBottom": "1px",
                                                "offsetEnd": "31%"
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{ll.at_walk2:,.0f}",
                                                "size": "xs",
                                                "align": "end"
                                            },
                                            {
                                                "type": "icon",
                                                "url": ll.icon_walk2,
                                                "margin": "lg"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "Conversion",
                                                "size": "xs",
                                                "flex": 0
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{ll.tg_conversion:,.0f}",
                                                "size": "xs",
                                                "align": "end",
                                                "position": "absolute",
                                                "offsetBottom": "1px",
                                                "offsetEnd": "31%"
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{ll.at_conversion:,.0f}",
                                                "size": "xs",
                                                "align": "end"
                                            },
                                            {
                                                "type": "icon",
                                                "url": ll.icon_conversion,
                                                "margin": "lg"
                                            }
                                        ],
                                        "backgroundColor": "#FAF5FF"
                                    },
                                    {
                                        "type": "separator"
                                    }
                                ]
                            },
                            "footer": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "Copyright 2019 AP (Thailand) PCL.",
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
                                ]
                            },
                            "styles": {
                                "header": {
                                    "backgroundColor": "#000000"
                                },
                                "hero": {
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

    data = {
        "replyToken": Reply_token,
        "messages": [
            type_msg
        ]
    }

    session = requests.Session()
    response = session.post(LINE_API_REPLY, data=json.dumps(data), headers=headers)
    return 201
