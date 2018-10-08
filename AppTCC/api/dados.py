# -*- coding: utf-8 -*-
import json
import requests

def get_deteccoes(id):
    try:
        url = 'https://safetycc.herokuapp.com/logs/'+id
        headers = {'Authorization': 'Basic YWRtaW46c2VjcmV0'}
        r = requests.get(url, headers=headers)
        dicionario = json.loads(r.content)
        return dicionario
    except:
        return ['erro']




def login(email, senha):
    try:
        url = 'https://safetycc.herokuapp.com/login'
        dados = {
            "email": email,
            "password": senha
        }

        headers = {'Authorization': 'Basic YWRtaW46c2VjcmV0'}
        r = requests.post(url, data=dados, headers=headers)
        print(r.content)
        dicionario = json.loads(r.content)
        return dicionario
    except:
        return ['erro']
