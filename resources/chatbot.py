import traceback
from flask_restful import Resource
from flask import request
import re

from datetime import datetime, timedelta

from config import CHANNEL_ACCESS_TOKEN, REPLY_WORDING, DEFAULT_REPLY_WORDING, \
    TEST_WORDING, RICH_MENU_MAIN, RICH_MENU_SECOND, \
    CHECK_PM, VIRUS, HIT_FEATURES, JOB_HELPDESK_NO

from libs import quick_reply, chatbot_rich_menu, \
    share_location, check_pm_airvisual, menu_06_01_features, \
    virus_corona_stat, menu_06_01_pm_value, job_helpdesk_detl

from models.chatbot_mst_user import MstUserModel
from models.tmp_virus_corona import VirusCoronaModel
from models.vw_jobhelpdesk import JobHelpdeskModel


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
                quick_reply.quickreplymsg(reply_token, reply_msg, CHANNEL_ACCESS_TOKEN)
            elif message in VIRUS:
                virus = VirusCoronaModel().find_all()
                virus_totl = VirusCoronaModel().get_TotalCase()
                virus_corona_stat.replyMsg(reply_token, virus,
                                           virus_totl[0],
                                           virus_totl[1],
                                           virus_totl[2],
                                           CHANNEL_ACCESS_TOKEN)
            elif message in CHECK_PM:  # Check PM 2.5
                share_location.quickreplymsg(reply_token, reply_msg, CHANNEL_ACCESS_TOKEN)
            elif re.match(HIT_FEATURES, message):
                menu_06_01_features.replyMsg(reply_token, None, CHANNEL_ACCESS_TOKEN)
            elif re.match(JOB_HELPDESK_NO, message):
                jobObj = JobHelpdeskModel().find_by_id(message)
                # print(jobObj)
                job_helpdesk_detl.replyMsg(reply_token, jobObj, CHANNEL_ACCESS_TOKEN)
            else:
                pass
        elif msg_type == 'image':
            image_id = payload['events'][0]['message']['id']
            contentProvider = payload['events'][0]['message']['contentProvider']['type']
            print(f"{image_id} , {contentProvider}")
        elif msg_type == 'location':
            location_id = payload['events'][0]['message']['id']
            address = payload['events'][0]['message']['address']
            latitude = payload['events'][0]['message']['latitude']
            longitude = payload['events'][0]['message']['longitude']
            print(f"{location_id}, {latitude}, {longitude}")

            # GET PM2.5 Value from API
            city, state, country, pm_val, temperature, icon_weather = check_pm_airvisual.getpm(latitude, longitude)
            # print(city, state, country, pm_val, temperature, icon_weather)
            header = "{0}, {1}, {2}".format(city, state, country)
            menu_06_01_pm_value.replyMsg(reply_token, header, pm_val, CHANNEL_ACCESS_TOKEN)
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
