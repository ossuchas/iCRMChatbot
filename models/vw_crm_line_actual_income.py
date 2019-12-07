from db import db
from typing import List


class ActualIncomeByProjModel(db.Model):
    __tablename__ = "vw_crm_line_actual_income"

    keys_id = db.Column(db.String(200), primary_key=True)
    AP_JV = db.Column(db.String(2))
    PType = db.Column(db.String(3))
    ProjectType = db.Column(db.String(50))
    ProductID = db.Column(db.String(15))
    ProjectName = db.Column(db.String(255))
    TransferDateApprove = db.Column(db.String(200))
    TotalUnit = db.Column(db.Integer)
    NetPrice = db.Column(db.Float)
    FreeDownAmount = db.Column(db.Float)
    NetPriceExclFD = db.Column(db.Float)

    @classmethod
    def find_by_current(cls) -> List["ActualIncomeByProjModel"]:
        return cls.query.filter_by(TransferDateApprove='20191206').all()

    @classmethod
    def find_by_date(cls, _date: str) -> List["ActualIncomeByProjModel"]:
        return cls.query.filter_by(TransferDateApprove=_date).all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
