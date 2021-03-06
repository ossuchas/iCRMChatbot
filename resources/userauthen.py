import traceback
from flask_restful import Resource
from flask import request
import json
from datetime import datetime

from libs.register_linkrichmenu import linkmenubyuser
from libs.ap_authen import APAuthen, APAuthenException
from models.chatbot_mst_user import MstUserModel

from config import RICH_MENU_MAIN


class UserAPRegister(Resource):
    @classmethod
    def post(cls):
        user_json = request.get_json()
        try:
            user_name = user_json["user_name"]
            password = user_json["password"]
            user_token_id = user_json["user_token_id"]
            # print(user_name, password)
            # print(user_token_id)
            # response = APAuthen.ap_authen(user_json["user_name"], user_json["password"], "APINTRANET")
            response = APAuthen.ap_authen(user_name, password, "APINTRANET")
            obj = json.loads(response.content)
            # print(obj)
            # print(obj["employeeID"], obj["displayName"], obj["email"])

            # Create Chatbot Master User
            mst_user = MstUserModel()

            mst_user.user_name = obj["employeeID"]
            mst_user.user_token_Id = user_token_id
            mst_user.user_full_name = obj["displayName"]
            mst_user.user_emp_id = obj["employeeID"]
            mst_user.user_status = 'A'
            mst_user.user_empcode = obj["employeeID"]
            mst_user.user_type = 'NOR'
            mst_user.user_position = 'AP'
            mst_user.createby = 'APIRegister'
            mst_user.createdate = datetime.now()
            mst_user.modifyby = 'APIRegister'
            mst_user.modifydate = datetime.now()

            mst_user.save_to_db()

            # Link Rich Menu
            rich_menu_link = RICH_MENU_MAIN
            response = linkmenubyuser(user_token_id, rich_menu_link)

            return {"message": "Successful Authentication"}, 200
            # return json.loads(response.content), 200
        except APAuthenException as e:
            return {"message": str(e)}, 401
        except:
            traceback.print_exc()
            return {"message": "Login Failed"}, 500
