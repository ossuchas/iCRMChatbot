from db import db
from typing import List


class ActualIncomeModel(db.Model):
    __tablename__ = "crm_line_actual_income"

    trans_id = db.Column(db.Integer, primary_key=True)
    ap_bg1_q1 = db.Column(db.Float)
    ap_bg1_q2 = db.Column(db.Float)
    ap_bg1_q3 = db.Column(db.Float)
    ap_bg1_q4 = db.Column(db.Float)
    ap_bg1_total = db.Column(db.Float)
    ap_bg2_q1 = db.Column(db.Float)
    ap_bg2_q2 = db.Column(db.Float)
    ap_bg2_q3 = db.Column(db.Float)
    ap_bg2_q4 = db.Column(db.Float)
    ap_bg2_total = db.Column(db.Float)
    ap_bg3_q1 = db.Column(db.Float)
    ap_bg3_q2 = db.Column(db.Float)
    ap_bg3_q3 = db.Column(db.Float)
    ap_bg3_q4 = db.Column(db.Float)
    ap_bg3_total = db.Column(db.Float)
    ap_bg4_q1 = db.Column(db.Float)
    ap_bg4_q2 = db.Column(db.Float)
    ap_bg4_q3 = db.Column(db.Float)
    ap_bg4_q4 = db.Column(db.Float)
    ap_bg4_total = db.Column(db.Float)
    ap_total_q1 = db.Column(db.Float)
    ap_total_q2 = db.Column(db.Float)
    ap_total_q3 = db.Column(db.Float)
    ap_total_q4 = db.Column(db.Float)
    ap_total = db.Column(db.Float)
    jv_bg3_q1 = db.Column(db.Float)
    jv_bg3_q2 = db.Column(db.Float)
    jv_bg3_q3 = db.Column(db.Float)
    jv_bg3_q4 = db.Column(db.Float)
    jv_bg3_total = db.Column(db.Float)
    jv_bg4_q1 = db.Column(db.Float)
    jv_bg4_q2 = db.Column(db.Float)
    jv_bg4_q3 = db.Column(db.Float)
    jv_bg4_q4 = db.Column(db.Float)
    jv_bg4_total = db.Column(db.Float)
    jv_total_q1 = db.Column(db.Float)
    jv_total_q2 = db.Column(db.Float)
    jv_total_q3 = db.Column(db.Float)
    jv_total_q4 = db.Column(db.Float)
    jv_total = db.Column(db.Float)
    grant_total_q1 = db.Column(db.Float)
    grant_total_q2 = db.Column(db.Float)
    grant_total_q3 = db.Column(db.Float)
    grant_total_q4 = db.Column(db.Float)
    grant_total = db.Column(db.Float)

    # @classmethod
    # def find_by_id(cls, _user_id: int) -> "MstUserModel":
    #     return cls.query.filter_by(user_id=_user_id).first()

    @classmethod
    def find_all(cls) -> "ActualIncomeModel":
        return cls.query.filter_by(trans_id=1).first()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
