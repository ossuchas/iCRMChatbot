import os
import re
import requests
import json
from config import LINE_API_RICHMENU


def replyMsg(userId: str = None, richMenuId: str = None, line_aceess_token: str = None):

    authorization = f"Bearer {line_aceess_token}"
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': authorization
    }

    url = f"{LINE_API_RICHMENU}/{userId}/richmenu/{richMenuId}"

    session = requests.Session()
    response = session.post(url, headers=headers)
    return 201
