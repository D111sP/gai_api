from clean_img_captcha.clean_img_26_12 import clean_img
from get_GIBDD.get_gibdd import *
from get_vin.get_vin import get_vin

import cv2
from tensorflow import keras
import datetime

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
        counter += 1
        img, token = get_captcha()
        array_cut_img = clean_img(img)
        answer = recognize_captcha(array_cut_img)
        response = get_history(answer, token, vin)
        if response.get('code') == None:
            print(response)
            print(f'Captcha was solved in {counter} attempts')
            break


if __name__ == '__main__':
    model = keras.models.load_model('model/model_80_30_loss_0_11_acc_0_97.h5')
    vin = "XWEDH511AB0010069" #get_vin(str(input("Введите номер авто: ")))
    time_start = datetime.datetime.now()
    get_info_GIBDD(vin)
    print(f"Time requiers: {datetime.datetime.now() - time_start}")