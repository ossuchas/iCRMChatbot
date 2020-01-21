from db import db
from typing import List
from datetime import datetime


class MstUserModel(db.Model):
    __tablename__ = "chatbot_mst_user"

    user_id = db.Column(db.Integer, primary_key=True)
    user_token_Id = db.Column(db.String(255))
    user_name = db.Column(db.String(255))
    user_full_name = db.Column(db.String(255))
    user_type = db.Column(db.String(10))
    user_sub_no = db.Column(db.String(10))
    user_emp_id = db.Column(db.String(50))
    user_empcode = db.Column(db.String(50))
    user_status = db.Column(db.String(2))
    createby = db.Column(db.String(20))
    createdate = db.Column(db.DateTime)
    modifyby = db.Column(db.String(20))
    modifydate = db.Column(db.DateTime)

    @classmethod
    def find_by_id(cls, _user_id: int) -> "MstUserModel":
        return cls.query.filter_by(user_id=_user_id).first()

    @classmethod
    def find_by_token_id(cls, _user_token_id: int) -> "MstUserModel":
        return cls.query.filter_by(user_token_Id=_user_token_id).first()

    @classmethod
    def check_auth_by_token_id(cls, _user_token_id: int) -> "MstUserModel":
        return cls.query.filter_by(user_token_Id=_user_token_id, user_status='A').first()

    @classmethod
    def check_VIP_auth_by_token_id(cls, _user_token_id: int) -> "MstUserModel":
        return cls.query.filter_by(user_token_Id=_user_token_id, user_status='A', user_type='VIP').first()

    @classmethod
    def check_clevel_auth_by_token_id(cls, _user_token_id: int) -> "MstUserModel":
        return cls.query.filter(cls.user_token_Id == _user_token_id,
                                cls.user_status == 'A',
                                cls.user_type.like('VIP%')).first()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
