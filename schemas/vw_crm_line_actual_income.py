from ma import ma
from models.vw_crm_line_actual_income import ActualIncomeByProjModel


class ActualIncomeByProjSchema(ma.ModelSchema):
    class Meta:
        model = ActualIncomeByProjModel

