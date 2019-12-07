import traceback
from flask_restful import Resource
from flask import request
import re


from config import CHANNEL_ACCESS_TOKEN, REPLY_WORDING, DEFAULT_REPLY_WORDING, \
    TEST_WORDING

from libs import chatbot_helper, test
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
        else:
            msg_type = 'beacon'

        reply_msg = None

        if msg_type == 'text':
            msg_text = payload['events'][0]['message']['text']
            message = msg_text

            if message in REPLY_WORDING:
                reply_msg = DEFAULT_REPLY_WORDING
                # Reply Message Default Post API
                chatbot_helper.replyMsg(reply_token, reply_msg, CHANNEL_ACCESS_TOKEN)
            elif message in TEST_WORDING:
                values = ActualIncomeByProjModel().find_by_date()
                # print(datas)
                test.replyMsg(reply_token, None, values, CHANNEL_ACCESS_TOKEN)
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
