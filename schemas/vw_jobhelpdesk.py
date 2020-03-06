from ma import ma
from models.vw_jobhelpdesk import JobHelpdeskModel


class JobHelpdeskSchema(ma.ModelSchema):
    class Meta:
        model = JobHelpdeskModel

