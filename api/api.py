# -*- coding: utf-8 -*-
import json
import requests

# VERIFICAR LOG
def getDeteccoes(idUser):
    try:
        Url             = "https://safetyflask.herokuapp.com/logs/"+idUser
        Headers         = { "Authorization": "Basic YWRtaW46c2VjcmV0" }
        Response        = requests.get(Url, headers=Headers)
        ResponseJson    = json.loads(Response.content)
        return ResponseJson
    except:
        return ["erro"]

# REALIZAR LOGIN
def loginUser(Email, Password):
    try:
        Url             = "https://safetyflask.herokuapp.com/login"
        Body            = { "email": Email, "password": Password }
        Headers         = { "Authorization": "Basic YWRtaW46c2VjcmV0" }
        Response        = requests.post(Url, data=Body, headers=Headers)
        ResponseJson    = json.loads(Response.content)
        return ResponseJson
    except:
        return ["erro"]
