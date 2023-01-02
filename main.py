from clean_img_captcha.clean_img_26_12 import clean_img
from get_GIBDD.get_gibdd import *
from get_vin.get_vin import get_vin
from html_css.get_img_dtp import get_img_dtp

import cv2
from tensorflow import keras
import datetime
import os
from base64 import b64encode as enc64

def recognize_captcha(array_cut_img: list):
    answer = ''
    for i in array_cut_img:
        x = cv2.cvtColor(i, cv2.COLOR_GRAY2RGB)
        x = x / 255
        x = np.expand_dims(x, axis=0)
        res = model.predict(x, verbose=0)  # use verbose=1 for showing logs
        answer += str(np.argmax(res))
    return answer

def get_info_GIBDD(vin):
    counter = 0
    while 1:
        array_response = []
        counter += 1
        img, token = get_captcha()
        array_cut_img = clean_img(img)
        answer = recognize_captcha(array_cut_img)
        response = get_history(answer, token, vin)
        if response.get('code') == None:
            array_response = get_all_value(answer, token, vin)
            array_response.append({"ИСТОРИЯ": response})
            # Перевод изображения в Base64
            # for el in range(len(array_response[0]['ДТП']['RequestResult']['Accidents'])):
            #     get_img_dtp(array_response[0]['ДТП']['RequestResult']['Accidents'][el]['DamagePoints'])
                # with open("C:\\Users\\elen0\\OneDrive\\Документы\\GitHub\\gibdd_api\\img_dtp\\1.png", 'rb') as f:
                #     binary = enc64(f.read())  # open binary file in read mode
                # array_response[0]['ДТП']['RequestResult']['Accidents'][el]['DamagePoints'] = binary
                # f.close()
                #os.remove("C:\\Users\\elen0\\OneDrive\\Документы\\GitHub\\gibdd_api\\img_dtp\\1.png")
            print(f'Captcha was solved in {counter} attempts')
            print(array_response)
            break


if __name__ == '__main__':
    model = keras.models.load_model('model/model_80_30_loss_0_11_acc_0_97.h5')
    #vin = "XWEDH511AB0010069"
    vin = get_vin(str(input("Ведите номер: ")))
    time_start = datetime.datetime.now()
    get_info_GIBDD(vin)
    print(f"Time requiers: {datetime.datetime.now() - time_start}")