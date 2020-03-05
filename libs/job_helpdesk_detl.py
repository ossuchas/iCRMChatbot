# -*- coding: utf-8 -*-

import requests
import json
from config import LINE_API_REPLY
from models.vw_jobhelpdesk import JobHelpdeskModel
from typing import List
from datetime import datetime


def replyMsg(Reply_token: str = None, jobOjb: JobHelpdeskModel = None, line_Acees_Token: str = None):

    authorization = f'Bearer {line_Acees_Token}'
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': authorization
    }

    type_msg = \
        {
            "type": "flex",
            "altText": "Flex Message",
            "contents":
                {
                    "type": "bubble",
                    "size": "giga",
                    "header": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "Job Number",
                                        "color": "#fffffff6",
                                        "size": "sm"
                                    },
                                    {
                                        "type": "separator"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": jobOjb.ticketnumber,
                                                "color": "#ffffff",
                                                "size": "xl",
                                                "flex": 5,
                                                "weight": "bold"
                                            },
                                            {
                                                "type": "text",
                                                "text": "In Process",
                                                "size": "md",
                                                "flex": 2,
                                                "weight": "bold",
                                                "color": "#ffffff"
                                            }
                                        ]
                                    }
                                ]
                            }
                        ],
                        "paddingAll": "20px",
                        "backgroundColor": "#c92028",
                        "spacing": "md",
                        "height": "80px",
                        "paddingTop": "22px"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "RequestBy",
                                        "size": "sm",
                                        "flex": 2,
                                        "weight": "bold",
                                        "color": "#8c8c8c"
                                    },
                                    {
                                        "type": "text",
                                        "text": f":{jobOjb.requestby}",
                                        "size": "sm",
                                        "flex": 3,
                                        "wrap": True,
                                        "color": "#696969"
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "RequestDept",
                                        "size": "sm",
                                        "flex": 2,
                                        "weight": "bold",
                                        "color": "#8c8c8c"
                                    },
                                    {
                                        "type": "text",
                                        "text": f":{jobOjb.requestdept}",
                                        "size": "sm",
                                        "flex": 3,
                                        "wrap": True,
                                        "color": "#696969"
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "RequestSubject",
                                        "size": "sm",
                                        "flex": 2,
                                        "weight": "bold",
                                        "color": "#8c8c8c"
                                    },
                                    {
                                        "type": "text",
                                        "text": f":{jobOjb.requestsubject}",
                                        "size": "sm",
                                        "flex": 3,
                                        "wrap": True,
                                        "color": "#696969"
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "Priority",
                                        "size": "sm",
                                        "flex": 2,
                                        "weight": "bold",
                                        "color": "#8c8c8c"
                                    },
                                    {
                                        "type": "text",
                                        "text": f":{jobOjb.priority}",
                                        "size": "sm",
                                        "flex": 3,
                                        "wrap": True,
                                        "color": "#696969"
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "JobType",
                                        "size": "sm",
                                        "flex": 2,
                                        "weight": "bold",
                                        "color": "#8c8c8c"
                                    },
                                    {
                                        "type": "text",
                                        "text": f":{jobOjb.jobtype}",
                                        "size": "sm",
                                        "flex": 3,
                                        "wrap": True,
                                        "color": "#696969"
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "Category",
                                        "size": "sm",
                                        "flex": 2,
                                        "weight": "bold",
                                        "color": "#8c8c8c"
                                    },
                                    {
                                        "type": "text",
                                        "text": f":{jobOjb.category}",
                                        "size": "sm",
                                        "flex": 3,
                                        "wrap": True,
                                        "color": "#696969"
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "Consult",
                                        "size": "sm",
                                        "flex": 2,
                                        "weight": "bold",
                                        "color": "#8c8c8c"
                                    },
                                    {
                                        "type": "text",
                                        "text": f":{jobOjb.crmconsultname}",
                                        "size": "sm",
                                        "flex": 3,
                                        "wrap": True,
                                        "color": "#696969"
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "Developer",
                                        "size": "sm",
                                        "flex": 2,
                                        "weight": "bold",
                                        "color": "#8c8c8c"
                                    },
                                    {
                                        "type": "text",
                                        "text": f":{jobOjb.devname}",
                                        "size": "sm",
                                        "flex": 3,
                                        "wrap": True,
                                        "color": "#696969"
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "Infrastructure",
                                        "size": "sm",
                                        "flex": 2,
                                        "weight": "bold",
                                        "color": "#8c8c8c"
                                    },
                                    {
                                        "type": "text",
                                        "text": f":{jobOjb.infraname}",
                                        "size": "sm",
                                        "flex": 3,
                                        "wrap": True,
                                        "color": "#696969"
                                    }
                                ]
                            },
                            {
                                "type": "button",
                                "action": {
                                    "type": "uri",
                                    "label": "Detail",
                                    "uri": "https://liff.line.me/1653377835-2lm05AzB"
                                },
                                "style": "secondary",
                                "height": "sm",
                                "margin": "sm",
                                "gravity": "center"
                            },
                            {
                                "type": "separator",
                                "margin": "sm"
                            },
                            {
                                "type": "separator",
                                "margin": "sm"
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": f"{jobOjb.estimatedatetimetxt}",
                                        "size": "sm",
                                        "gravity": "center",
                                        "flex": 0
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "filler"
                                            },
                                            {
                                                "type": "box",
                                                "layout": "vertical",
                                                "contents": [
                                                    {
                                                        "type": "filler"
                                                    }
                                                ],
                                                "cornerRadius": "30px",
                                                "height": "12px",
                                                "width": "12px",
                                                "borderColor": "#EF454D",
                                                "borderWidth": "2px"
                                            },
                                            {
                                                "type": "filler"
                                            }
                                        ],
                                        "flex": 0
                                    },
                                    {
                                        "type": "text",
                                        "text": "วัน/เวลา ที่คาดว่าจะแล้วเสร็จ",
                                        "gravity": "center",
                                        "flex": 4,
                                        "size": "xs",
                                        "color": "#807671",
                                        "weight": "bold"
                                    }
                                ],
                                "spacing": "lg",
                                "cornerRadius": "30px",
                                "margin": "md"
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "filler"
                                            }
                                        ],
                                        "flex": 3
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "box",
                                                "layout": "horizontal",
                                                "contents": [
                                                    {
                                                        "type": "filler"
                                                    },
                                                    {
                                                        "type": "box",
                                                        "layout": "vertical",
                                                        "contents": [
                                                            {
                                                                "type": "filler"
                                                            }
                                                        ],
                                                        "width": "2px",
                                                        "backgroundColor": "#B7B7B7"
                                                    },
                                                    {
                                                        "type": "filler"
                                                    }
                                                ],
                                                "flex": 1
                                            }
                                        ],
                                        "width": "12px"
                                    },
                                    {
                                        "type": "text",
                                        "text": "38 min",
                                        "gravity": "center",
                                        "flex": 4,
                                        "size": "xs",
                                        "color": "#8c8c8c"
                                    }
                                ],
                                "spacing": "lg",
                                "height": "40px",
                                "width": "250px"
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": f"{jobOjb.acutalfinishdatetimetxt}",
                                        "size": "sm",
                                        "gravity": "center",
                                        "flex": 0
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "filler"
                                            },
                                            {
                                                "type": "box",
                                                "layout": "vertical",
                                                "contents": [
                                                    {
                                                        "type": "filler"
                                                    }
                                                ],
                                                "cornerRadius": "30px",
                                                "height": "12px",
                                                "width": "12px",
                                                "borderColor": "#6486E3",
                                                "borderWidth": "2px"
                                            },
                                            {
                                                "type": "filler"
                                            }
                                        ],
                                        "flex": 0
                                    },
                                    {
                                        "type": "text",
                                        "text": "วัน/เวลา ที่ดำเนินการเสร็จ",
                                        "gravity": "center",
                                        "flex": 4,
                                        "size": "xs",
                                        "weight": "bold",
                                        "color": "#807671",
                                        "wrap": True
                                    }
                                ],
                                "spacing": "lg",
                                "cornerRadius": "30px",
                                "margin": "xs"
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "filler"
                                            }
                                        ],
                                        "flex": 3
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "box",
                                                "layout": "horizontal",
                                                "contents": [
                                                    {
                                                        "type": "filler"
                                                    },
                                                    {
                                                        "type": "box",
                                                        "layout": "vertical",
                                                        "contents": [
                                                            {
                                                                "type": "filler"
                                                            }
                                                        ],
                                                        "width": "2px",
                                                        "backgroundColor": "#B7B7B7"
                                                    },
                                                    {
                                                        "type": "filler"
                                                    }
                                                ],
                                                "flex": 1
                                            }
                                        ],
                                        "width": "12px"
                                    },
                                    {
                                        "type": "text",
                                        "text": "5 min",
                                        "gravity": "center",
                                        "flex": 4,
                                        "size": "xs",
                                        "color": "#8c8c8c"
                                    }
                                ],
                                "spacing": "lg",
                                "height": "40px",
                                "width": "250px"
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": f"{jobOjb.infracompletedatetxt}",
                                        "size": "sm",
                                        "gravity": "center",
                                        "flex": 0
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "filler"
                                            },
                                            {
                                                "type": "box",
                                                "layout": "vertical",
                                                "contents": [
                                                    {
                                                        "type": "filler"
                                                    }
                                                ],
                                                "cornerRadius": "30px",
                                                "height": "12px",
                                                "width": "12px",
                                                "borderColor": "#6486E3",
                                                "borderWidth": "2px"
                                            },
                                            {
                                                "type": "filler"
                                            }
                                        ],
                                        "flex": 0
                                    },
                                    {
                                        "type": "text",
                                        "text": "Infra. ดำเนินการเสร็จ",
                                        "gravity": "center",
                                        "flex": 4,
                                        "size": "xs",
                                        "weight": "bold",
                                        "color": "#807671",
                                        "wrap": True
                                    }
                                ],
                                "spacing": "lg",
                                "cornerRadius": "30px",
                                "margin": "xs"
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "filler"
                                            }
                                        ],
                                        "flex": 3
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "box",
                                                "layout": "horizontal",
                                                "contents": [
                                                    {
                                                        "type": "filler"
                                                    },
                                                    {
                                                        "type": "box",
                                                        "layout": "vertical",
                                                        "contents": [
                                                            {
                                                                "type": "filler"
                                                            }
                                                        ],
                                                        "width": "2px",
                                                        "backgroundColor": "#B7B7B7"
                                                    },
                                                    {
                                                        "type": "filler"
                                                    }
                                                ],
                                                "flex": 1
                                            }
                                        ],
                                        "width": "12px"
                                    },
                                    {
                                        "type": "text",
                                        "text": "24H32mins",
                                        "gravity": "center",
                                        "flex": 4,
                                        "size": "xs",
                                        "color": "#8c8c8c"
                                    }
                                ],
                                "spacing": "lg",
                                "height": "40px",
                                "width": "250px"
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": f"{jobOjb.devcompletedatetxt}",
                                        "size": "sm",
                                        "gravity": "center",
                                        "flex": 0
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "filler"
                                            },
                                            {
                                                "type": "box",
                                                "layout": "vertical",
                                                "contents": [
                                                    {
                                                        "type": "filler"
                                                    }
                                                ],
                                                "cornerRadius": "30px",
                                                "height": "12px",
                                                "width": "12px",
                                                "borderColor": "#6486E3",
                                                "borderWidth": "2px"
                                            },
                                            {
                                                "type": "filler"
                                            }
                                        ],
                                        "flex": 0
                                    },
                                    {
                                        "type": "text",
                                        "text": "Dev. ดำเนินการเสร็จ",
                                        "gravity": "center",
                                        "flex": 4,
                                        "size": "xs",
                                        "weight": "bold",
                                        "color": "#807671",
                                        "wrap": True
                                    }
                                ],
                                "spacing": "lg",
                                "cornerRadius": "30px",
                                "margin": "xs"
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "filler"
                                            }
                                        ],
                                        "flex": 3
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "box",
                                                "layout": "horizontal",
                                                "contents": [
                                                    {
                                                        "type": "filler"
                                                    },
                                                    {
                                                        "type": "box",
                                                        "layout": "vertical",
                                                        "contents": [
                                                            {
                                                                "type": "filler"
                                                            }
                                                        ],
                                                        "width": "2px",
                                                        "backgroundColor": "#B7B7B7"
                                                    },
                                                    {
                                                        "type": "filler"
                                                    }
                                                ],
                                                "flex": 1
                                            }
                                        ],
                                        "width": "12px"
                                    },
                                    {
                                        "type": "text",
                                        "text": "55 min",
                                        "gravity": "center",
                                        "flex": 4,
                                        "size": "xs",
                                        "color": "#8c8c8c"
                                    }
                                ],
                                "spacing": "lg",
                                "height": "40px",
                                "width": "250px"
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": f"{jobOjb.startdatetimetxt}",
                                        "size": "sm",
                                        "gravity": "center",
                                        "flex": 0
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "filler"
                                            },
                                            {
                                                "type": "box",
                                                "layout": "vertical",
                                                "contents": [
                                                    {
                                                        "type": "filler"
                                                    }
                                                ],
                                                "cornerRadius": "30px",
                                                "height": "12px",
                                                "width": "12px",
                                                "borderColor": "#6486E3",
                                                "borderWidth": "2px"
                                            },
                                            {
                                                "type": "filler"
                                            }
                                        ],
                                        "flex": 0
                                    },
                                    {
                                        "type": "text",
                                        "text": "วัน/เวลา ที่เริ่มงาน",
                                        "gravity": "center",
                                        "flex": 4,
                                        "size": "xs",
                                        "weight": "bold",
                                        "color": "#807671",
                                        "wrap": True
                                    }
                                ],
                                "spacing": "lg",
                                "cornerRadius": "30px",
                                "margin": "xs"
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "filler"
                                            }
                                        ],
                                        "flex": 3
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "box",
                                                "layout": "horizontal",
                                                "contents": [
                                                    {
                                                        "type": "filler"
                                                    },
                                                    {
                                                        "type": "box",
                                                        "layout": "vertical",
                                                        "contents": [
                                                            {
                                                                "type": "filler"
                                                            }
                                                        ],
                                                        "width": "2px",
                                                        "backgroundColor": "#B7B7B7"
                                                    },
                                                    {
                                                        "type": "filler"
                                                    }
                                                ],
                                                "flex": 1
                                            }
                                        ],
                                        "width": "12px"
                                    },
                                    {
                                        "type": "text",
                                        "text": "55 min",
                                        "gravity": "center",
                                        "flex": 4,
                                        "size": "xs",
                                        "color": "#8c8c8c"
                                    }
                                ],
                                "spacing": "lg",
                                "height": "40px",
                                "width": "250px"
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": f"{jobOjb.requestdatetimetxt}",
                                        "size": "sm",
                                        "gravity": "center",
                                        "flex": 0
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "filler"
                                            },
                                            {
                                                "type": "box",
                                                "layout": "vertical",
                                                "contents": [
                                                    {
                                                        "type": "filler"
                                                    }
                                                ],
                                                "cornerRadius": "30px",
                                                "height": "12px",
                                                "width": "12px",
                                                "borderColor": "#6486E3",
                                                "borderWidth": "2px"
                                            },
                                            {
                                                "type": "filler"
                                            }
                                        ],
                                        "flex": 0
                                    },
                                    {
                                        "type": "text",
                                        "text": "วัน/เวลา ที่แจ้งปัญหา",
                                        "gravity": "center",
                                        "flex": 4,
                                        "size": "xs",
                                        "weight": "bold",
                                        "color": "#807671",
                                        "wrap": True
                                    }
                                ],
                                "spacing": "lg",
                                "cornerRadius": "30px",
                                "margin": "xs"
                            },
                            {
                                "type": "separator",
                                "margin": "sm"
                            }
                        ]
                    },
                    "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": "Copyright 2020 AP (Thailand) PCL.",
                                "align": "center",
                                "size": "xs",
                                "color": "#FFFFFF"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "image",
                                        "url": "https://i.ibb.co/fS0B4wP/AP-Logo-2018.png"
                                    }
                                ],
                                "position": "absolute",
                                "height": "30px",
                                "width": "32px",
                                "offsetBottom": "3px"
                            }
                        ],
                        "backgroundColor": "#000000"
                    }
                }
        }

    data = {
        "replyToken": Reply_token,
        "messages": [
            type_msg
        ]
    }

    session = requests.Session()
    response = session.post(LINE_API_REPLY, data=json.dumps(data), headers=headers)
    return 201
