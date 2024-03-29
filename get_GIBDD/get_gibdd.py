import requests
import cv2
import base64
import numpy as np

def get_captcha():
    response = requests.get('https://check.gibdd.ru/captcha').json()
    #print(response)
    base_code = response['base64jpg']
    png_recover = base64.b64decode(base_code)
    np_data = np.frombuffer(png_recover, np.uint8)
    img = cv2.imdecode(np_data, cv2.IMREAD_UNCHANGED)
    token = response['token']

    return img, token

def get_history(answer: str, token: str, vin: str):
    url = 'https://xn--b1afk4ade.xn--90adear.xn--p1ai/proxy/check/auto/history'
    payload = {
        "vin": f"{vin}",
        "checkType": "history",
        "captchaWord": answer,
        "captchaToken": token
    }
    response = requests.post(url, data=payload).json()

    return response

def get_diagnostic(answer: str, token: str, vin: str):
    url = 'https://xn--b1afk4ade.xn--90adear.xn--p1ai/proxy/check/auto/diagnostic'
    payload = {
        "vin": f"{vin}",
        "checkType": "diagnostic",
        "captchaWord": answer,
        "captchaToken": token
    }
    response = requests.post(url, data=payload).json()

    return response

def get_restrict(answer: str, token: str, vin: str):
    url = 'https://xn--b1afk4ade.xn--90adear.xn--p1ai/proxy/check/auto/restrict'
    payload = {
        "vin": f"{vin}",
        "checkType": "restrict",
        "captchaWord": answer,
        "captchaToken": token
    }
    response = requests.post(url, data=payload).json()

    return response

def get_dtp(answer: str, token: str, vin: str):
    url = 'https://xn--b1afk4ade.xn--90adear.xn--p1ai/proxy/check/auto/dtp'
    payload = {
        "vin": f"{vin}",
        "checkType": "dtp",
        "captchaWord": answer,
        "captchaToken": token
    }
    response = requests.post(url, data=payload).json()

    return response

def get_wanted(answer: str, token: str, vin: str):
    url = 'https://xn--b1afk4ade.xn--90adear.xn--p1ai/proxy/check/auto/wanted'
    payload = {
        "vin": f"{vin}",
        "checkType": "wanted",
        "captchaWord": answer,
        "captchaToken": token
    }
    response = requests.post(url, data=payload).json()

    return response

def get_all_value(answer: str, token: str, vin: str):
    array_all_value = []

    array_all_value.append({"ДТП" : get_dtp(answer, token, vin)}) #ДТП
    array_all_value.append({"ОГРАНИЧЕНИЕ" : get_restrict(answer, token, vin)}) #
    array_all_value.append({"ДИАГНОСТИКА" : get_diagnostic(answer, token, vin)})
    array_all_value.append({"РОЗЫСК": get_wanted(answer, token, vin)})
    return array_all_value