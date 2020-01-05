# -*- coding: utf-8 -*-

import requests
import json
from config import LINE_API_REPLY
from models.crm_line_gross_income import GrossIncomeModel


def replyMsg(Reply_token: str = None, actual_income: GrossIncomeModel = None, line_Acees_Token: str = None):

    authorization = f"Bearer {line_Acees_Token}"
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': authorization
    }
    # print(f"{actual_income.ap_bg1_q2:,.0f}")
    # f"{actual_income.ap_bg1_q1:,.0f}"
    # f"{actual_income.ap_bg1_q2:,.0f}"
    # f"{actual_income.ap_bg1_q3:,.0f}"
    # f"{actual_income.ap_bg1_q4:,.0f}"
    # f"{actual_income.ap_bg1_total:,.0f}"
    # f"{actual_income.ap_bg2_q1:,.0f}"
    # f"{actual_income.ap_bg2_q2:,.0f}"
    # f"{actual_income.ap_bg2_q3:,.0f}"
    # f"{actual_income.ap_bg2_q4:,.0f}"
    # f"{actual_income.ap_bg2_total:,.0f}"
    # f"{actual_income.ap_bg3_q1:,.0f}"
    # f"{actual_income.ap_bg3_q2:,.0f}"
    # f"{actual_income.ap_bg3_q3:,.0f}"
    # f"{actual_income.ap_bg3_q4:,.0f}"
    # f"{actual_income.ap_bg3_total:,.0f}"
    # f"{actual_income.ap_bg4_q1:,.0f}"
    # f"{actual_income.ap_bg4_q2:,.0f}"
    # f"{actual_income.ap_bg4_q3:,.0f}"
    # f"{actual_income.ap_bg4_q4:,.0f}"
    # f"{actual_income.ap_bg4_total:,.0f}"
    # f"{actual_income.ap_total_q1:,.0f}"
    # f"{actual_income.ap_total_q2:,.0f}"
    # f"{actual_income.ap_total_q3:,.0f}"
    # f"{actual_income.ap_total_q4:,.0f}"
    # f"{actual_income.ap_total:,.0f}"
    # f"{actual_income.jv_bg3_q1:,.0f}"
    # f"{actual_income.jv_bg3_q2:,.0f}"
    # f"{actual_income.jv_bg3_q3:,.0f}"
    # f"{actual_income.jv_bg3_q4:,.0f}"
    # f"{actual_income.jv_bg3_total:,.0f}"
    # f"{actual_income.jv_bg4_q1:,.0f}"
    # f"{actual_income.jv_bg4_q2:,.0f}"
    # f"{actual_income.jv_bg4_q3:,.0f}"
    # f"{actual_income.jv_bg4_q4:,.0f}"
    # f"{actual_income.jv_bg4_total:,.0f}"
    # f"{actual_income.jv_total_q1:,.0f}"
    # f"{actual_income.jv_total_q2:,.0f}"
    # f"{actual_income.jv_total_q3:,.0f}"
    # f"{actual_income.jv_total_q4:,.0f}"
    # f"{actual_income.jv_total:,.0f}"
    # f"{actual_income.grant_total_q2:,.0f}"
    # f"{actual_income.grant_total_q3:,.0f}"
    # f"{actual_income.grant_total_q4:,.0f}"
    # f"{actual_income.grant_total:,.0f}"

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
                            "size": "kilo",
                            "hero": {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "Gross Income",
                                        "align": "start",
                                        "color": "#FFFFFF",
                                        "offsetStart": "5%",
                                        "offsetTop": "2px"
                                    },
                                    {
                                        "type": "text",
                                        "text": "Year to date",
                                        "align": "end",
                                        "color": "#FFFFFF",
                                        "size": "xs",
                                        "gravity": "bottom",
                                        # "style": "italic",
                                        "offsetEnd": "15px",
                                        "offsetTop": "2px"
                                    }
                                ],
                                "height": "25px"
                            },
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "AP",
                                                "weight": "bold",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": "Vol. (MB)",
                                                "align": "end",
                                                "size": "sm",
                                                "weight": "bold"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "BG1 - SHD",
                                                "align": "start",
                                                "offsetStart": "5%",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{actual_income.ap_bg1_total:,.0f}",
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
                                                "text": "BG2 - TH",
                                                "align": "start",
                                                "offsetStart": "5%",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{actual_income.ap_bg2_total:,.0f}",
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
                                                "text": "BG3 - CONDO 1",
                                                "align": "start",
                                                "offsetStart": "5%",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{actual_income.ap_bg3_total:,.0f}",
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
                                                "text": "BG4 - CONDO 2",
                                                "offsetStart": "5%",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{actual_income.ap_bg4_total:,.0f}",
                                                "align": "end",
                                                "size": "sm"
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
                                                "text": "AP Total :",
                                                "size": "sm",
                                                "align": "end",
                                                "weight": "bold",
                                                # "style": "italic"
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{actual_income.ap_total:,.0f}",
                                                "align": "end",
                                                "size": "sm",
                                                "weight": "bold",
                                                # "style": "italic"
                                            }
                                        ],
                                        "backgroundColor": "#E8E16F"
                                    },
                                    {
                                        "type": "separator"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "JV",
                                                "size": "sm",
                                                "weight": "bold"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "BG3 - JV (100%)",
                                                "align": "start",
                                                "offsetStart": "5%",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{actual_income.jv_bg3_total:,.0f}",
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
                                                "text": "BG4 - JV (100%)",
                                                "align": "start",
                                                "offsetStart": "5%",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{actual_income.jv_bg4_total:,.0f}",
                                                "align": "end",
                                                "size": "sm"
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
                                                "text": "JV Total :",
                                                "size": "sm",
                                                "align": "end",
                                                "weight": "bold",
                                                # "style": "italic"
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{actual_income.jv_total:,.0f}",
                                                "align": "end",
                                                "size": "sm",
                                                "weight": "bold",
                                                # "style": "italic"
                                            }
                                        ],
                                        "backgroundColor": "#E8E16F"
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
                                                "text": "Grand Total",
                                                "size": "sm",
                                                "weight": "bold"
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{actual_income.grant_total:,.0f}",
                                                "size": "sm",
                                                "align": "end",
                                                "weight": "bold"
                                            }
                                        ],
                                        "margin": "sm",
                                        "backgroundColor": "#7AFF97"
                                    },
                                    {
                                        "type": "separator"
                                    },
                                    {
                                        "type": "separator",
                                        "margin": "sm"
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
                        },  # Year to Date
                        {
                            "type": "bubble",
                            "size": "kilo",
                            "hero": {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "Gross Income",
                                        "align": "start",
                                        "color": "#FFFFFF",
                                        "offsetStart": "5%",
                                        "offsetTop": "2px"
                                    },
                                    {
                                        "type": "text",
                                        "text": "Quarter#1",
                                        "align": "end",
                                        "color": "#FFFFFF",
                                        "size": "xs",
                                        "gravity": "bottom",
                                        # "style": "italic",
                                        "offsetEnd": "15px",
                                        "offsetTop": "2px"
                                    }
                                ],
                                "height": "25px"
                            },
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "AP",
                                                "weight": "bold",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": "Vol. (MB)",
                                                "align": "end",
                                                "size": "sm",
                                                "weight": "bold"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "BG1 - SHD",
                                                "align": "start",
                                                "offsetStart": "5%",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{actual_income.ap_bg1_q1:,.0f}",
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
                                                "text": "BG2 - TH",
                                                "align": "start",
                                                "offsetStart": "5%",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{actual_income.ap_bg2_q1:,.0f}",
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
                                                "text": "BG3 - CONDO 1",
                                                "align": "start",
                                                "offsetStart": "5%",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{actual_income.ap_bg3_q1:,.0f}",
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
                                                "text": "BG4 - CONDO 2",
                                                "offsetStart": "5%",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{actual_income.ap_bg4_q1:,.0f}",
                                                "align": "end",
                                                "size": "sm"
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
                                                "text": "AP Total :",
                                                "size": "sm",
                                                "align": "end",
                                                "weight": "bold",
                                                # "style": "italic"
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{actual_income.ap_total_q1:,.0f}",
                                                "align": "end",
                                                "size": "sm",
                                                "weight": "bold",
                                                # "style": "italic"
                                            }
                                        ],
                                        "backgroundColor": "#E8E16F"
                                    },
                                    {
                                        "type": "separator"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "JV",
                                                "size": "sm",
                                                "weight": "bold"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "BG3 - JV (100%)",
                                                "align": "start",
                                                "offsetStart": "5%",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{actual_income.jv_bg3_q1:,.0f}",
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
                                                "text": "BG4 - JV (100%)",
                                                "align": "start",
                                                "offsetStart": "5%",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{actual_income.jv_bg4_q1:,.0f}",
                                                "align": "end",
                                                "size": "sm"
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
                                                "text": "JV Total :",
                                                "size": "sm",
                                                "align": "end",
                                                "weight": "bold",
                                                # "style": "italic"
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{actual_income.jv_total_q1:,.0f}",
                                                "align": "end",
                                                "size": "sm",
                                                "weight": "bold",
                                                # "style": "italic"
                                            }
                                        ],
                                        "backgroundColor": "#E8E16F"
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
                                                "text": "Grand Total",
                                                "size": "sm",
                                                "weight": "bold"
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{actual_income.grant_total_q1:,.0f}",
                                                "size": "sm",
                                                "align": "end",
                                                "weight": "bold"
                                            }
                                        ],
                                        "margin": "sm",
                                        "backgroundColor": "#7AFF97"
                                    },
                                    {
                                        "type": "separator"
                                    },
                                    {
                                        "type": "separator",
                                        "margin": "sm"
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
                        },  # Quarter 1
                        {
                            "type": "bubble",
                            "size": "kilo",
                            "hero": {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "Gross Income",
                                        "align": "start",
                                        "color": "#FFFFFF",
                                        "offsetStart": "5%",
                                        "offsetTop": "2px"
                                    },
                                    {
                                        "type": "text",
                                        "text": "Quarter#2",
                                        "align": "end",
                                        "color": "#FFFFFF",
                                        "size": "xs",
                                        "gravity": "bottom",
                                        # "style": "italic",
                                        "offsetEnd": "15px",
                                        "offsetTop": "2px"
                                    }
                                ],
                                "height": "25px"
                            },
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "AP",
                                                "weight": "bold",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": "Vol. (MB)",
                                                "align": "end",
                                                "size": "sm",
                                                "weight": "bold"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "BG1 - SHD",
                                                "align": "start",
                                                "offsetStart": "5%",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{actual_income.ap_bg1_q2:,.0f}",
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
                                                "text": "BG2 - TH",
                                                "align": "start",
                                                "offsetStart": "5%",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{actual_income.ap_bg2_q2:,.0f}",
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
                                                "text": "BG3 - CONDO 1",
                                                "align": "start",
                                                "offsetStart": "5%",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{actual_income.ap_bg3_q2:,.0f}",
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
                                                "text": "BG4 - CONDO 2",
                                                "offsetStart": "5%",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{actual_income.ap_bg4_q2:,.0f}",
                                                "align": "end",
                                                "size": "sm"
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
                                                "text": "AP Total :",
                                                "size": "sm",
                                                "align": "end",
                                                "weight": "bold",
                                                # "style": "italic"
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{actual_income.ap_total_q2:,.0f}",
                                                "align": "end",
                                                "size": "sm",
                                                "weight": "bold",
                                                # "style": "italic"
                                            }
                                        ],
                                        "backgroundColor": "#E8E16F"
                                    },
                                    {
                                        "type": "separator"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "JV",
                                                "size": "sm",
                                                "weight": "bold"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "BG3 - JV (100%)",
                                                "align": "start",
                                                "offsetStart": "5%",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{actual_income.jv_bg3_q2:,.0f}",
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
                                                "text": "BG4 - JV (100%)",
                                                "align": "start",
                                                "offsetStart": "5%",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{actual_income.jv_bg4_q2:,.0f}",
                                                "align": "end",
                                                "size": "sm"
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
                                                "text": "JV Total :",
                                                "size": "sm",
                                                "align": "end",
                                                "weight": "bold",
                                                # "style": "italic"
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{actual_income.jv_total_q2:,.0f}",
                                                "align": "end",
                                                "size": "sm",
                                                "weight": "bold",
                                                # "style": "italic"
                                            }
                                        ],
                                        "backgroundColor": "#E8E16F"
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
                                                "text": "Grand Total",
                                                "size": "sm",
                                                "weight": "bold"
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{actual_income.grant_total_q2:,.0f}",
                                                "size": "sm",
                                                "align": "end",
                                                "weight": "bold"
                                            }
                                        ],
                                        "margin": "sm",
                                        "backgroundColor": "#7AFF97"
                                    },
                                    {
                                        "type": "separator"
                                    },
                                    {
                                        "type": "separator",
                                        "margin": "sm"
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
                        },  # Quarter 2
                        {
                            "type": "bubble",
                            "size": "kilo",
                            "hero": {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "Gross Income",
                                        "align": "start",
                                        "color": "#FFFFFF",
                                        "offsetStart": "5%",
                                        "offsetTop": "2px"
                                    },
                                    {
                                        "type": "text",
                                        "text": "Quarter#3",
                                        "align": "end",
                                        "color": "#FFFFFF",
                                        "size": "xs",
                                        "gravity": "bottom",
                                        # "style": "italic",
                                        "offsetEnd": "15px",
                                        "offsetTop": "2px"
                                    }
                                ],
                                "height": "25px"
                            },
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "AP",
                                                "weight": "bold",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": "Vol. (MB)",
                                                "align": "end",
                                                "size": "sm",
                                                "weight": "bold"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "BG1 - SHD",
                                                "align": "start",
                                                "offsetStart": "5%",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{actual_income.ap_bg1_q3:,.0f}",
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
                                                "text": "BG2 - TH",
                                                "align": "start",
                                                "offsetStart": "5%",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{actual_income.ap_bg2_q3:,.0f}",
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
                                                "text": "BG3 - CONDO 1",
                                                "align": "start",
                                                "offsetStart": "5%",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{actual_income.ap_bg3_q3:,.0f}",
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
                                                "text": "BG4 - CONDO 2",
                                                "offsetStart": "5%",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{actual_income.ap_bg4_q3:,.0f}",
                                                "align": "end",
                                                "size": "sm"
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
                                                "text": "AP Total :",
                                                "size": "sm",
                                                "align": "end",
                                                "weight": "bold",
                                                # "style": "italic"
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{actual_income.ap_total_q3:,.0f}",
                                                "align": "end",
                                                "size": "sm",
                                                "weight": "bold",
                                                # "style": "italic"
                                            }
                                        ],
                                        "backgroundColor": "#E8E16F"
                                    },
                                    {
                                        "type": "separator"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "JV",
                                                "size": "sm",
                                                "weight": "bold"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "BG3 - JV (100%)",
                                                "align": "start",
                                                "offsetStart": "5%",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{actual_income.jv_bg3_q3:,.0f}",
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
                                                "text": "BG4 - JV (100%)",
                                                "align": "start",
                                                "offsetStart": "5%",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{actual_income.jv_bg4_q3:,.0f}",
                                                "align": "end",
                                                "size": "sm"
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
                                                "text": "JV Total :",
                                                "size": "sm",
                                                "align": "end",
                                                "weight": "bold",
                                                # "style": "italic"
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{actual_income.jv_total_q3:,.0f}",
                                                "align": "end",
                                                "size": "sm",
                                                "weight": "bold",
                                                # "style": "italic"
                                            }
                                        ],
                                        "backgroundColor": "#E8E16F"
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
                                                "text": "Grand Total",
                                                "size": "sm",
                                                "weight": "bold"
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{actual_income.grant_total_q3:,.0f}",
                                                "size": "sm",
                                                "align": "end",
                                                "weight": "bold"
                                            }
                                        ],
                                        "margin": "sm",
                                        "backgroundColor": "#7AFF97"
                                    },
                                    {
                                        "type": "separator"
                                    },
                                    {
                                        "type": "separator",
                                        "margin": "sm"
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
                        },  # Quarter 3
                        {
                            "type": "bubble",
                            "size": "kilo",
                            "hero": {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "Gross Income",
                                        "align": "start",
                                        "color": "#FFFFFF",
                                        "offsetStart": "5%",
                                        "offsetTop": "2px"
                                    },
                                    {
                                        "type": "text",
                                        "text": "Quarter#4",
                                        "align": "end",
                                        "color": "#FFFFFF",
                                        "size": "xs",
                                        "gravity": "bottom",
                                        # "style": "italic",
                                        "offsetEnd": "15px",
                                        "offsetTop": "2px"
                                    }
                                ],
                                "height": "25px"
                            },
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "AP",
                                                "weight": "bold",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": "Vol. (MB)",
                                                "align": "end",
                                                "size": "sm",
                                                "weight": "bold"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "BG1 - SHD",
                                                "align": "start",
                                                "offsetStart": "5%",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{actual_income.ap_bg1_q4:,.0f}",
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
                                                "text": "BG2 - TH",
                                                "align": "start",
                                                "offsetStart": "5%",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{actual_income.ap_bg2_q4:,.0f}",
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
                                                "text": "BG3 - CONDO 1",
                                                "align": "start",
                                                "offsetStart": "5%",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{actual_income.ap_bg3_q4:,.0f}",
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
                                                "text": "BG4 - CONDO 2",
                                                "offsetStart": "5%",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{actual_income.ap_bg4_q4:,.0f}",
                                                "align": "end",
                                                "size": "sm"
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
                                                "text": "AP Total :",
                                                "size": "sm",
                                                "align": "end",
                                                "weight": "bold",
                                                # "style": "italic"
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{actual_income.ap_total_q4:,.0f}",
                                                "align": "end",
                                                "size": "sm",
                                                "weight": "bold",
                                                # "style": "italic"
                                            }
                                        ],
                                        "backgroundColor": "#E8E16F"
                                    },
                                    {
                                        "type": "separator"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "JV",
                                                "size": "sm",
                                                "weight": "bold"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "BG3 - JV (100%)",
                                                "align": "start",
                                                "offsetStart": "5%",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{actual_income.jv_bg3_q4:,.0f}",
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
                                                "text": "BG4 - JV (100%)",
                                                "align": "start",
                                                "offsetStart": "5%",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{actual_income.jv_bg4_q4:,.0f}",
                                                "align": "end",
                                                "size": "sm"
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
                                                "text": "JV Total :",
                                                "size": "sm",
                                                "align": "end",
                                                "weight": "bold",
                                                # "style": "italic"
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{actual_income.jv_total_q4:,.0f}",
                                                "align": "end",
                                                "size": "sm",
                                                "weight": "bold",
                                                # "style": "italic"
                                            }
                                        ],
                                        "backgroundColor": "#E8E16F"
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
                                                "text": "Grand Total",
                                                "size": "sm",
                                                "weight": "bold"
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{actual_income.grant_total_q4:,.0f}",
                                                "size": "sm",
                                                "align": "end",
                                                "weight": "bold"
                                            }
                                        ],
                                        "margin": "sm",
                                        "backgroundColor": "#7AFF97"
                                    },
                                    {
                                        "type": "separator"
                                    },
                                    {
                                        "type": "separator",
                                        "margin": "sm"
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
