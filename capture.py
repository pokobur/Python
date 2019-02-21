import requests
import json
import cv2
import datetime
import os
import shutil

today = str(datetime.date.today())
todaydir = "./images/" + today

if not os.path.exists(todaydir):
    os.makedirs(todaydir)

fileName = todaydir + "/pic" + datetime.datetime.today().strftime('%Y%m%d_%H%M%S') + ".png"
capture = cv2.VideoCapture(0) #数字はカメラの認識番号（外部接続は１～）
ret, image = capture.read()


if ret == True:
	cv2.imwrite(fileName, image)
"""
	files = {'file': open(fileName, 'rb')}
	param = {'token':'xoxb-348838103313-OYQUzG6JBsTCkS2r8V8KPmvw', 'channels':'C87G8M9EY'}
	res = requests.post(url="https://slack.com/api/files.upload",params=param, files=files)
"""
dirlist = os.listdir("./images/")
if len(dirlist) > 30:
	shutil.rmtree(dirlist[0])
