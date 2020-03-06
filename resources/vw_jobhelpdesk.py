import traceback
from flask_restful import Resource
from flask import request
import re

from models.vw_jobhelpdesk import JobHelpdeskModel
from schemas.vw_jobhelpdesk import JobHelpdeskSchema

job_schema = JobHelpdeskSchema()
job_list_schema = JobHelpdeskSchema(many=True)


class JobHelpDesk(Resource):
    @classmethod
    def get(cls, _job_id: str):
        job = JobHelpdeskModel().find_by_id(_job_id)
        if job:
            return job_schema.dump(job), 200

        return {"message": "No Data Found"}, 404
