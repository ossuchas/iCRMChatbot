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

# Bot Test
#CHANNEL_ACCESS_TOKEN="wXjIZWvNNerxSVIpFVomPA4baBMaXhZtSJdJT11Uw4E8IOqzoJ+DGo++h/TPthxBM2LbrPCpiWiZX0GkXXENi9FE0DccFs0d6fSgntVhbj7Kf1iWp3hwXtJUOYSm5Dib7jC121/2bDpT1b0bIP1N4wdB04t89/1O/w1cDnyilFU="

# IT@APTHAI BOT
# CHANNEL_ACCESS_TOKEN="yzEGLNrzFPgkRW113hBPayMP+4Z6nmGa3gDQNAxNxYQR7jqj9Vo6w3YwfOLnpzPr48+GB9j4rgTlcWKyRPMgY0f+e0FuX5tizSVzLrd/o3gkaniObBMudbWZXrHL3CD9IZ2SQXUE7GeDp76UVNpG+gdB04t89/1O/w1cDnyilFU="
CHANNEL_ACCESS_TOKEN = os.environ.get("CHANNEL_ACCESS_TOKEN")
# LINE_API="https://api.line.me/v2/bot/message/reply"
LINE_API = os.environ.get("LINE_API")

DEFAULT_REPLY_WORDING = "เจ้านายกำลังฝึกผมให้เข้าใจในเรื่องอื่นๆอยู่นะครับ ขอโทษทีตอนนี้ยังไม่พร้อมตอบเรื่องที่ถามมานะครับ"
REPLY_WORDING = ["99999", "00000", "เสี่ยจัสติน", "เสี่ย"]

REPLY_SALCE_ACCM_B_M_WORDING = ["ยอดเดือนที่แล้ว", "ยอดขายเดือนที่แล้ว", "สอบถามยอดขายเดือนที่แล้วหน่อยครับ", "ส่งยอดเดือนที่แล้วมาดูหน่อย",
                 "ขอยอดขายเดือนที่แล้ว", "ส่งยอดขายเดือนที่แล้วหน่อย"]

REPLY_SALCE_ACCM_C_M_WORDING = ["ยอดเดือนนี้", "ยอดขายเดือนนี้", "สอบถามยอดขายเดือนนี้หน่อยครับ", "ส่งยอดเดือนนี้มาดูหน่อย",
                              "ขอยอดขายเดือนนี้", "ส่งยอดขายเดือนนี้หน่อย"]

MENU_01_VIP = "LL BY BG"
MENU_01_VIP_BG = "LL BY BG"
MENU_02_VIP = "LL BY SubBG"
MENU_02_VIP_BG = "LL BY SubBG"
# MENU_02 = ['ยอดขาย2']
# MENU_03 = ['ยอดขาย3']
# MENU_04 = ['ยอดขาย4']
# MENU_05 = ['menu_ยอดขาย5']
# MENU_06 = ['menu_ยอดขาย6']

# MENU_01_01_SDH = ['ยอดขายบ้านเดี่ยว']
# MENU_02_01_TH = ['ยอดขายบ้านเดี่ยว']
# MENU_03_01_CD1 = ['ยอดขายบ้านเดี่ยว']
# MENU_04_01_CD2 = ['ยอดขายบ้านเดี่ยว']

# Main Menu
LL_MSG_All = "LL SDH All"
LL_MSG_PROJ = "proj:"

# Select Sub BG SDH
LL_MSG_SUB_PERIOD = "LL SDH Sub"

# Peroid Select All BG
LL_MSG_ALLBG_PERIOD = "LL Period BY BG"

# Peroid Select All Sub BG
LL_MSG_ALLSUBBG_PERIOD = "LL Period BY SubBG"

# AP Phone Book
LL_MSG_APPHONEBOOK = "AP"
LL_MSG_APPHONEBOOK2 = "ap"
AC_ACTUAL_INCOME = "Actual Income"
EXECUTIVE_REPORT = "Executive Report"
