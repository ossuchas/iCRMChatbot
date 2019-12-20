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
             last_values: List["ActualIncomeByProjModel"] = None,
             before_last_values: List["ActualIncomeByProjModel"] = None,
             date_val: str = None,
             date_val_last: str = None,
             date_val_b_last: str = None,
             line_aceess_token: str = None) -> int:
    authorization = 'Bearer {}'.format(line_aceess_token)
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': authorization
    }
    print("Current ", values)
    print("Last ", last_values)

    # Current Value
    new_contents = [
        {"type": "separator"},
        {"type": "box", "layout": "baseline", "contents":
            [{"type": "text", "text": "Project", "size": "sm", "weight": "bold"},
             {"type": "text", "text": "Total Unit", "align": "end", "size": "sm", "weight": "bold"},
             {"type": "text", "text": "Net (Excl FD)", "align": "end", "size": "sm", "weight": "bold"}]
         }]

    total_u = 0
    total_p = 0.00
    i_count_rec = 0
    for val in values:
        total_u = total_u + val.TotalUnit
        total_p = total_p + val.NetPriceExclFD
        if i_count_rec % 2 == 0:
            bg_color_row = "#FFFFFF"
        else:
            bg_color_row = "#EBEDEF"

        new_contents.append({
            "type": "box", "layout": "baseline", "contents":
                [{"type": "text", "text": "{}:{}".format(val.ProductID, val.ProjectName), "size": "xs", "wrap": True},
                 {"type": "text", "text": "{}".format(val.TotalUnit), "size": "xs", "align": "end"},
                 {"type": "text", "text": f"{val.NetPriceExclFD:,.0f}", "size": "xs", "align": "end"}],
            "backgroundColor": bg_color_row
        })
        i_count_rec += 1

    # print(i_count_rec)

    new_contents.append({
        "type": "box", "layout": "baseline", "contents":
            [{"type": "text", "text": "Grand Total", "size": "sm", "weight": "bold", "offsetStart": "150%"},
             {"type": "text", "text": "{}".format(total_u), "align": "end", "size": "sm", "weight": "bold"},
             {"type": "text", "text": f"{total_p:,.0f}", "align": "end", "size": "sm", "weight": "bold"}],
        "backgroundColor": "#7AFF97", "margin": "xs"})

    # last Value
    last_new_contents = [
        {"type": "separator"},
        {"type": "box", "layout": "baseline", "contents":
            [{"type": "text", "text": "Project", "size": "sm", "weight": "bold"},
             {"type": "text", "text": "Total Unit", "align": "end", "size": "sm", "weight": "bold"},
             {"type": "text", "text": "Net (Excl FD)", "align": "end", "size": "sm", "weight": "bold"}]
         }]

    total_u = 0
    total_p = 0.00
    i_count_rec = 0
    for val in last_values:
        total_u = total_u + val.TotalUnit
        total_p = total_p + val.NetPriceExclFD
        if i_count_rec % 2 == 0:
            bg_color_row = "#FFFFFF"
        else:
            bg_color_row = "#EBEDEF"

        last_new_contents.append({
            "type": "box", "layout": "baseline", "contents":
                [{"type": "text", "text": "{}:{}".format(val.ProductID, val.ProjectName), "size": "xs", "wrap": True},
                 {"type": "text", "text": "{}".format(val.TotalUnit), "size": "xs", "align": "end"},
                 {"type": "text", "text": f"{val.NetPriceExclFD:,.0f}", "size": "xs", "align": "end"}],
            "backgroundColor": bg_color_row
        })
        i_count_rec += 1

    # print(i_count_rec)

    last_new_contents.append({
        "type": "box", "layout": "baseline", "contents":
            [{"type": "text", "text": "Grand Total", "size": "sm", "weight": "bold", "offsetStart": "150%"},
             {"type": "text", "text": "{}".format(total_u), "align": "end", "size": "sm", "weight": "bold"},
             {"type": "text", "text": f"{total_p:,.0f}", "align": "end", "size": "sm", "weight": "bold"}],
        "backgroundColor": "#7AFF97", "margin": "xs"})

    # Before Last Value
    before_last_new_contents = [
        {"type": "separator"},
        {"type": "box", "layout": "baseline", "contents":
            [{"type": "text", "text": "Project", "size": "sm", "weight": "bold"},
             {"type": "text", "text": "Total Unit", "align": "end", "size": "sm", "weight": "bold"},
             {"type": "text", "text": "Net (Excl FD)", "align": "end", "size": "sm", "weight": "bold"}]
         }]

    total_u = 0
    total_p = 0.00
    i_count_rec = 0
    for val in before_last_values:
        total_u = total_u + val.TotalUnit
        total_p = total_p + val.NetPriceExclFD
        if i_count_rec % 2 == 0:
            bg_color_row = "#FFFFFF"
        else:
            bg_color_row = "#EBEDEF"

        before_last_new_contents.append({
            "type": "box", "layout": "baseline", "contents":
                [{"type": "text", "text": "{}:{}".format(val.ProductID, val.ProjectName), "size": "xs", "wrap": True},
                 {"type": "text", "text": "{}".format(val.TotalUnit), "size": "xs", "align": "end"},
                 {"type": "text", "text": f"{val.NetPriceExclFD:,.0f}", "size": "xs", "align": "end"}],
            "backgroundColor": bg_color_row
        })
        i_count_rec += 1

    # print(i_count_rec)

    before_last_new_contents.append({
        "type": "box", "layout": "baseline", "contents":
            [{"type": "text", "text": "Grand Total", "size": "sm", "weight": "bold", "offsetStart": "150%"},
             {"type": "text", "text": "{}".format(total_u), "align": "end", "size": "sm", "weight": "bold"},
             {"type": "text", "text": f"{total_p:,.0f}", "align": "end", "size": "sm", "weight": "bold"}],
        "backgroundColor": "#7AFF97", "margin": "xs"})

    flex_msg = {
        "type": "flex", "altText": "this is a flex message", "contents": {
            "type": "carousel",
            "contents": [
                {"type": "bubble", "size": "giga", "header":
                    {"type": "box", "layout": "baseline", "contents":
                        [{"type": "text", "text": "Actual income", "color": "#FFFFFF", "size": "lg", "weight": "bold"},
                         {"type": "text", "text": "Today",
                          "align": "end", "size": "xs", "color": "#FFFFFF", "flex": 0, "style": "italic"}
                         ]
                     },
                 "hero": {"type": "box", "layout": "baseline", "contents":
                     [{"type": "text", "text": "Transfer Date At {}".format(date_val), "align": "end", "weight": "bold",
                       "offsetEnd": "20px", "size": "sm", "color": "#939393"}]},
                 "body": {"type": "box", "layout": "vertical", "contents": new_contents},
                 "footer": {"type": "box", "layout": "vertical", "contents":
                     [{"type": "text", "text": "Copyright 2019 AP PCL.", "size": "xs", "align": "center",
                       "color": "#ffffff"},
                      {"type": "box", "layout": "vertical", "contents":
                          [{"type": "image", "url": "https://i.ibb.co/fS0B4wP/AP-Logo-2018.png"}],
                       "position": "absolute",
                       "width": "32px", "height": "32px", "offsetBottom": "2px"}]},
                 "styles": {"header": {"backgroundColor": "#000000"},
                            "footer": {"backgroundColor": "#000000"}}
                 },
                {"type": "bubble", "size": "giga", "header":
                    {"type": "box", "layout": "baseline", "contents":
                        [{"type": "text", "text": "Actual income", "color": "#FFFFFF", "size": "lg", "weight": "bold"},
                         {"type": "text", "text": "Yesterday",
                          "align": "end", "size": "xs", "color": "#FFFFFF", "flex": 0, "style": "italic"}
                         ]
                     },
                 "hero": {"type": "box", "layout": "baseline", "contents":
                     [{"type": "text", "text": "Transfer Date At {}".format(date_val_last), "align": "end", "weight": "bold",
                       "offsetEnd": "20px", "size": "sm", "color": "#939393"}]},
                 "body": {"type": "box", "layout": "vertical", "contents": last_new_contents},
                 "footer": {"type": "box", "layout": "vertical", "contents":
                     [{"type": "text", "text": "Copyright 2019 AP PCL.", "size": "xs", "align": "center",
                       "color": "#ffffff"},
                      {"type": "box", "layout": "vertical", "contents":
                          [{"type": "image", "url": "https://i.ibb.co/fS0B4wP/AP-Logo-2018.png"}],
                       "position": "absolute",
                       "width": "32px", "height": "32px", "offsetBottom": "2px"}]},
                 "styles": {"header": {"backgroundColor": "#000000"},
                            "footer": {"backgroundColor": "#000000"}}
                 },
                {"type": "bubble", "size": "giga", "header":
                    {"type": "box", "layout": "baseline", "contents":
                        [{"type": "text", "text": "Actual income", "color": "#FFFFFF", "size": "lg", "weight": "bold"},
                         {"type": "text", "text": "Before Yesterday",
                          "align": "end", "size": "xs", "color": "#FFFFFF", "flex": 0, "style": "italic"}
                         ]
                     },
                 "hero": {"type": "box", "layout": "baseline", "contents":
                     [{"type": "text", "text": "Transfer Date At {}".format(date_val_b_last), "align": "end",
                       "weight": "bold",
                       "offsetEnd": "20px", "size": "sm", "color": "#939393"}]},
                 "body": {"type": "box", "layout": "vertical", "contents": before_last_new_contents},
                 "footer": {"type": "box", "layout": "vertical", "contents":
                     [{"type": "text", "text": "Copyright 2019 AP PCL.", "size": "xs", "align": "center",
                       "color": "#ffffff"},
                      {"type": "box", "layout": "vertical", "contents":
                          [{"type": "image", "url": "https://i.ibb.co/fS0B4wP/AP-Logo-2018.png"}],
                       "position": "absolute",
                       "width": "32px", "height": "32px", "offsetBottom": "2px"}]},
                 "styles": {"header": {"backgroundColor": "#000000"},
                            "footer": {"backgroundColor": "#000000"}}
                 }
            ]
        }
    }

    data = {"replyToken": reply_token, "messages": [flex_msg]}

    session = requests.Session()
    response = session.post(LINE_API, data=json.dumps(data), headers=headers)
    return 201
