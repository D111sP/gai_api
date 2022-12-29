import time

from selenium import webdriver
import os

html_file = os.getcwd() + "\\car.html"
browser = webdriver.Chrome(executable_path="C:\\Users\\elen0\\OneDrive\\Документы\\GitHub\\gibdd_api\\html_css\\chromedriver.exe")

browser.get("file:///" + html_file)
time.sleep(5)