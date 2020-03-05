from db import db
from typing import List


class JobHelpdeskModel(db.Model):
    __tablename__ = "vw_CRM_JobHelpDesk"

    requestid = db.Column(db.Integer, primary_key=True)
    ticketnumber = db.Column(db.String(50))
    ticketsystem = db.Column(db.String(50))
    requestdatetime = db.Column(db.DateTime)
    startdatetime = db.Column(db.DateTime)
    estimatedatetime = db.Column(db.DateTime)
    acutalfinishdatetime = db.Column(db.DateTime)
    overdueflag = db.Column(db.String(2))
    priority = db.Column(db.String(2))
    requestdate = db.Column(db.String(20))
    reqyear = db.Column(db.Integer)
    reqmonthname = db.Column(db.String(30))
    reqmonth = db.Column(db.Integer)
    reqweekdw = db.Column(db.Integer)
    reqweekday = db.Column(db.String(3))
    requestby = db.Column(db.String(255))
    requestdept = db.Column(db.String(500))
    status = db.Column(db.String(500))
    requestsubject = db.Column(db.String(500))
    requestnote = db.Column(db.String(1000))
    jobtype = db.Column(db.String(500))
    categoryid = db.Column(db.Integer)
    category = db.Column(db.String(500))
    crmconsult = db.Column(db.String(10))
    crmconsultname = db.Column(db.String(255))
    devempcode = db.Column(db.String(10))
    devname = db.Column(db.String(255))
    devcompletedate = db.Column(db.DateTime)
    infraempcode = db.Column(db.String(10))
    infraname = db.Column(db.String(255))
    infracompletedate = db.Column(db.DateTime)
    approvecomment = db.Column(db.String(1000))

    @classmethod
    def find_all(cls) -> List["JobHelpdeskModel"]:
        return cls.query.all()

    @classmethod
    def find_by_id(cls, _job_id: str) -> "JobHelpdeskModel":
        return cls.query.filter_by(ticketnumber=_job_id).first()

    # @classmethod
    # def get_TotalCase(cls) -> int:
    #     sql_statement = """
    #        SELECT SUM(CAST(REPLACE(TotalCase,',','') AS INT)) AS TotalCase
    #        ,SUM(CASE WHEN LEN(TotalDeath) = 0 THEN 0 ELSE CAST(TotalDeath AS FLOAT) END)AS Death
    #        FROM dbo.tmp_virus_corona WITH(NOLOCK)
    #        """
    #     return db.session.execute(sql_statement).fetchone()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
