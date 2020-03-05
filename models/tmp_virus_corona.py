from db import db
from typing import List


class VirusCoronaModel(db.Model):
    __tablename__ = "tmp_virus_corona"

    Country = db.Column(db.String(255), primary_key=True)
    TotalCase = db.Column(db.String(255))
    TodayChange = db.Column(db.String(255))
    TotalDeath = db.Column(db.String(255))
    Location = db.Column(db.String(255))
    Datetime = db.Column(db.String(255))

    @classmethod
    def find_all(cls) -> List["VirusCoronaModel"]:
        return cls.query.limit(25).all()

    @classmethod
    def get_TotalCase(cls) -> int:
        sql_statement = """
           SELECT SUM(CAST(REPLACE(TotalCase,',','') AS INT)) AS TotalCase
           ,SUM(CASE WHEN LEN(TotalDeath) = 0 THEN 0 ELSE CAST(REPLACE(TotalDeath,',','') AS FLOAT) END)AS Death
           ,SUM(CASE WHEN LEN(TotalCured) = 0 THEN 0 ELSE CAST(REPLACE(TotalCured,',','') AS FLOAT) END)AS TotalCured
           FROM dbo.tmp_virus_corona WITH(NOLOCK)
           """
        return db.session.execute(sql_statement).fetchone()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
