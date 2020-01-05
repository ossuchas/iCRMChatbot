import traceback
from flask_restful import Resource
from flask import request
import re

from datetime import datetime, timedelta

import requests
import json
from config import LINE_API_REPLY


from config import CHANNEL_ACCESS_TOKEN, REPLY_WORDING, DEFAULT_REPLY_WORDING, \
    TEST_WORDING, RICH_MENU_MAIN, RICH_MENU_SECOND

from libs import chatbot_helper, test, menu_04_01_ac_period, menu_04_01_actual_income_show_daily, \
    quick_reply, menu_project_sdh, chatbot_push_helper, chatbot_rich_menu, menu_04_01_acgrs_period
from models.vw_crm_line_actual_income import ActualIncomeByProjModel


class ChatBot(Resource):
    @classmethod
    def get(cls):
        return {"message": "Hello World"}, 200


class ChatBotRegister(Resource):
    @classmethod
    def post(cls):
        payload = request.get_json()
        print(payload)

        reply_token = payload['events'][0]['replyToken']
        source_type = payload['events'][0]['source']['type']
        timestamps = payload['events'][0]['timestamp']

        # get event type beacon or message
        events_type = payload['events'][0]['type']
        # print(events_type)

        groupId = None
        userId = None
        stickerId = None
        packageId = None
        msg_text = None
        name = None
        beacon_hwid = None
        beacon_dm = None
        beacon_type = None

        try:
            groupId = payload['events'][0]['source']['groupId']
            userId = payload['events'][0]['source']['userId']
            # print(userId, groupId)
        except:
            userId = payload['events'][0]['source']['userId']

        if events_type == 'message':
            msg_type = payload['events'][0]['message']['type']
        elif events_type == 'postback':
            msg_type = 'postback'
            # msg_type = payload['events'][0]['postback']['type']
        else:
            msg_type = 'beacon'

        reply_msg = None

        if msg_type == 'text':
            msg_text = payload['events'][0]['message']['text']
            message = msg_text

            if message in REPLY_WORDING:
                reply_msg = DEFAULT_REPLY_WORDING
                # Reply Message Default Post API
                # chatbot_helper.replyMsg(reply_token, reply_msg, CHANNEL_ACCESS_TOKEN)
                quick_reply.quickreplymsg(reply_token, reply_msg, CHANNEL_ACCESS_TOKEN)
            elif message in TEST_WORDING:
                menu_04_01_acgrs_period.replyMsg(reply_token, None, CHANNEL_ACCESS_TOKEN)
                # menu_project_sdh.replyMsg(reply_token, None, CHANNEL_ACCESS_TOKEN)
                # chatbot_push_helper.pushMsg(reply_token, CHANNEL_ACCESS_TOKEN)
                # values = ActualIncomeByProjModel().find_by_datetest("2")[0]
                # print(values)

        elif msg_type == 'postback':
            # print('kai')
            param_data = payload['events'][0]['postback']['data']
            # print(param_data)
            richmenuId = None
            if param_data == 'next':
                richmenuId = RICH_MENU_SECOND
            elif param_data == 'back':
                richmenuId = RICH_MENU_MAIN
            else:
                pass

            chatbot_rich_menu.replyMsg(userId=userId,
                                       richMenuId=richmenuId,
                                       line_aceess_token=CHANNEL_ACCESS_TOKEN)

            # param_date = payload['events'][0]['postback']['params']['date']
            # date_val = param_date.replace("-", "").strip()
            # print(param_data, date_val)
            # reply_msg = "{}={}".format(param_data, date_val)
            # values = ActualIncomeByProjModel().find_by_date(date_val)
            # test.replyMsg(reply_token, None, values, param_date, CHANNEL_ACCESS_TOKEN)
            # chatbot_helper.replyMsg(reply_token, reply_msg, CHANNEL_ACCESS_TOKEN)
        elif msg_type == 'beacon':
            beacon_hwid = payload['events'][0]['beacon']['hwid']
            beacon_dm = payload['events'][0]['beacon']['dm']
            beacon_type = payload['events'][0]['beacon']['type']
            stickerId = None
            packageId = None
            msg_text = None
        else:
            if msg_type == 'sticker':
                stickerId = payload['events'][0]['message']['stickerId']
                packageId = payload['events'][0]['message']['packageId']
            else:
                stickerId = None
                packageId = None
                msg_text = None

        # Save Log to DB
        # logs.savechatlog2db(reply_token, groupId,
        #                     userId, source_type,
        #                     timestamps, msg_type,
        #                     msg_text, stickerId, packageId,
        #                     beacon_hwid, beacon_dm, beacon_type)

        return {"message": "Register Line Push and Reply Message Successful"}, 201
