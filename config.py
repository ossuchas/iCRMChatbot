import os
import urllib

DEBUG = True
DATABASE_HOST = os.environ.get("DATABASE_HOST")
DATABASE_NAME = os.environ.get("DATABASE_NAME")
DATABASE_USER = os.environ.get("DATABASE_USER")
DATABASE_PASS = os.environ.get("DATABASE_PASS")

params = 'Driver={ODBC Driver 17 for SQL Server};' \
             f"Server=" + f"{DATABASE_HOST};" \
             f"Database=" + f"{DATABASE_NAME};" \
             f"uid=" + f"{DATABASE_USER};" \
             f"pwd=" + f"{DATABASE_PASS};"

params = urllib.parse.quote_plus(params)

SQLALCHEMY_DATABASE_URI = "mssql+pyodbc:///?odbc_connect=%s" % params
SQLALCHEMY_TRACK_MODIFICATIONS = False
PROPAGATE_EXCEPTIONS = True
JWT_BLACKLIST_ENABLED = True
JWT_BLACKLIST_TOKEN_CHECKS = ["access", "refresh"]

CHANNEL_ACCESS_TOKEN = os.environ.get("CHANNEL_ACCESS_TOKEN")
LINE_API_RICHMENU=os.environ.get("LINE_API_RICHMENU")
LINE_API_REPLY = os.environ.get("LINE_API_REPLY")
LINE_API_PUSH = os.environ.get("LINE_API_PUSH")

DEFAULT_REPLY_WORDING = "เจ้านายกำลังฝึกผมให้เข้าใจในเรื่องอื่นๆอยู่นะครับ ขอโทษทีตอนนี้ยังไม่พร้อมตอบเรื่องที่ถามมานะครับ"
REPLY_WORDING = ["99999", "00000", "เสี่ยจัสติน", "เสี่ย"]
TEST_WORDING = ["test", "Test"]


# Peroid Select Gross incomde
GROSS_INCOME = "Gross Income Period Y2D"

MENU_02_VIP_BG = "LL BY SubBG"

RICH_MENU_MAIN = "richmenu-8624d4c0b62fae0f3a1fead4b5b4b045"
RICH_MENU_SECOND = "richmenu-e6c9778d91e8a69484f6ae6853663bcf"
# Register => richmenu-b3ce1866f8ef334ab1ab3bc30a54d669

CHECK_PM = "ตรวจสอบค่า PM 2.5"

# Virus Corona
VIRUS = ["ไวรัสโคโรนา", "โคโรนา", "virus", "corona", "อู่ฮั่น", "ไวรัสจีน", "ไวรัส"]

# Hit Features
HIT_FEATURES = "Hit Features"

JOB_HELPDESK_OPEN = "Job=Open"
JOB_HELPDESK_INQUIRY = "inquiry=>system:"
JOB_HELPDESK_KPI = "Job=KPI"
JOB_HELPDESK_Request = "Job=Request"
JOB_HELPDESK_NO = "REQ"
JOB_HELPDESK_FIND = "req_no="
JOB_HELPDESK_COPY_NOTIFY = "CRMLineNotify"

# Covid-19
COVID19 = "covid-19"