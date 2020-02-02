import traceback
from flask_restful import Resource
from flask import request
import re

from datetime import datetime, timedelta

import requests
import json
from config import LINE_API_REPLY


from config import CHANNEL_ACCESS_TOKEN, REPLY_WORDING, DEFAULT_REPLY_WORDING, \
    TEST_WORDING, RICH_MENU_MAIN, RICH_MENU_SECOND, GROSS_INCOME, LL_MSG_ALLSUBBG_PERIOD, \
    MENU_02_VIP_BG, BOOKING_INCOME, CHECK_PM, VIRUS, HIT_FEATURES

from libs import chatbot_helper, test, menu_04_01_ac_period, menu_04_01_actual_income_show_daily, \
    quick_reply, menu_project_sdh, chatbot_push_helper, chatbot_rich_menu, menu_04_01_acgrs_period, \
    menu_04_01_acgrs_income_show_y2d, menu_02_01_ll_allbg_subbg_period_show, \
    menu_02_01_ll_allbg_subbg_period_show_L_C, menu_02_01_ll_allbg_subbg_period, \
    share_location, check_pm_airvisual, menu_06_01_features, \
    virus_corona_stat, menu_06_01_pm_value

from models.crm_line_gross_income import GrossIncomeModel
from models.crm_line_ll_data import LeadLagModel
from models.chatbot_mst_user import MstUserModel
from models.tmp_virus_corona import VirusCoronaModel


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
                # print('kai')
                menu_04_01_acgrs_period.replyMsg(reply_token, None, CHANNEL_ACCESS_TOKEN)
                # menu_project_sdh.replyMsg(reply_token, None, CHANNEL_ACCESS_TOKEN)
                # chatbot_push_helper.pushMsg(reply_token, CHANNEL_ACCESS_TOKEN)
                # values = ActualIncomeByProjModel().find_by_datetest("2")[0]
                # print(values)
            elif message in VIRUS:
                virus = VirusCoronaModel().find_all()
                virus_totl = VirusCoronaModel().get_TotalCase()
                # print(virus_totl[0], virus_totl[1])
                virus_corona_stat.replyMsg(reply_token, virus, virus_totl[0], virus_totl[1], CHANNEL_ACCESS_TOKEN)
            elif message in GROSS_INCOME:
                # print(message)
                grs_model = GrossIncomeModel().find_all()
                menu_04_01_acgrs_income_show_y2d.replyMsg(reply_token, grs_model, CHANNEL_ACCESS_TOKEN)
            elif message in CHECK_PM:  # Check PM 2.5
                share_location.quickreplymsg(reply_token, reply_msg, CHANNEL_ACCESS_TOKEN)
            # elif message in BOOKING_INCOME:
            elif re.match(BOOKING_INCOME, message):
                vip = MstUserModel().check_clevel_auth_by_token_id(userId)
                print(vip)
                # print(message)
                grs_model = GrossIncomeModel().find_all()
                menu_04_01_acgrs_income_show_y2d.replyMsg(reply_token, grs_model, CHANNEL_ACCESS_TOKEN)
            elif re.match(HIT_FEATURES, message):
                menu_06_01_features.replyMsg(reply_token, None, CHANNEL_ACCESS_TOKEN)
            elif re.match(MENU_02_VIP_BG, message):  # Select Sub BG
                # LL[0] BY[1] SubBG[2] <1-4>[1.0][3]
                value = message.split(' ')[3]
                bg = value.split('[')[0]
                subbg = value.split('[')[1][:-1]
                prefix_bg = value.split('[')[1][:-3].strip()

                # vip = MstUserModel().check_VIP_auth_by_token_id(userId)
                vip = MstUserModel().check_clevel_auth_by_token_id(userId)
                print(vip)
                if vip:
                    menu_02_01_ll_allbg_subbg_period.replyMsg(reply_token, bg, subbg, CHANNEL_ACCESS_TOKEN)
                else:
                    userModel = MstUserModel().find_by_token_id(_user_token_id=userId)
                    if userModel.user_sub_no[0].strip() == prefix_bg:
                        menu_02_01_ll_allbg_subbg_period.replyMsg(reply_token, bg, subbg, CHANNEL_ACCESS_TOKEN)
                    else:
                        reply_msg = "You are not authorized to access this menu."
                        chatbot_helper.replyMsg(reply_token, reply_msg, CHANNEL_ACCESS_TOKEN)
            elif re.match(LL_MSG_ALLSUBBG_PERIOD, message):
                p_period = message.replace(LL_MSG_ALLSUBBG_PERIOD, "").strip()
                val = re.match(r"[^[]*\[([^]]*)\]", p_period).groups()[0]
                bg = val.split('-')[0].strip()
                subbg = val.split('-')[1].strip()
                period = None
                if p_period[0] == 'Q':  # Quarter
                    period = 'QTD'
                elif p_period[0] == 'W':  # Week
                    period = 'W'
                elif p_period[0] == 'A':  # As of Current
                    period = 'YTD'
                if p_period[0] != 'W':
                    ll_model = LeadLagModel().find_by_subbg_period('SUBBG', bg, subbg, period, 'Y')
                    menu_02_01_ll_allbg_subbg_period_show.replyMsg(reply_token, bg, subbg, ll_model,
                                                                   CHANNEL_ACCESS_TOKEN)
                else:
                    ll_model_current = LeadLagModel().find_by_subbg_period('SUBBG', bg, subbg, period, 'Y')
                    ll_model_last_week = LeadLagModel().find_by_subbg_period('SUBBG', bg, subbg, period, 'N')
                    menu_02_01_ll_allbg_subbg_period_show_L_C.replyMsg(reply_token, bg, subbg,ll_model_current,
                                                                       ll_model_last_week,
                                                                       CHANNEL_ACCESS_TOKEN)
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
            # print(header)
            # reply_msg = "{0} {1} {2} {3} {4} {5}".format(city, state, country, pm_val, temperature, icon_weather)
            # reply_msg = "{0} {1} {2} ค่า PM = {3}".format(city, state, country, pm_val)
            # chatbot_helper.replyMsg(reply_token, reply_msg, CHANNEL_ACCESS_TOKEN)
            # print(pm_val)
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
