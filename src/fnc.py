import numpy as np
import copy
import cv2
import os

def haarFaceDetectSetup(self):
    haarcascades = os.path.abspath(os.path.join(os.path.dirname(__file__), 'cascade'))
    self.mod['haarFace'] = cv2.CascadeClassifier(haarcascades + "\\haarcascade_frontalface_default.xml")

def haarFaceDetectFunction(self, img, fpt):
    msg = {
        'key': 'face',
        'offset': [0, 0]
    }

    frm = copy.deepcopy(self.frm['cur'])
    gry = cv2.cvtColor(frm, cv2.COLOR_BGR2GRAY)
    faces = self.mod['haarFace'].detectMultiScale(gry, 1.1, 1)
    # faces = self.mod['haarFace'].detectMultiScale(gry, 1.1, 2)
    offset_x = 0
    offset_y = 0
    for (x, y, w, h) in faces:
        self.frm['cur'] = cv2.rectangle(self.frm['cur'], (x,y), (x+w,y+h), (255,0,0), 1)
        offset_x = (self.pxl//2 - (x + w//2)) * self.rat
        offset_y = (self.pxl//2 - (y + h//2)) * self.rat
    msg['offset'] = [-offset_x, offset_y]

    return msg

def naiveSearchSetup(self):
    pass

def naiveSearchFunction(self, img, fpt):
    msg = {
        'key': 'search',
        'offset': [0, 0]
    }

    if fpt[0] >= 1650:
        msg['offset'][0] = -1600
        if fpt[1] >= 930:
            msg['offset'][1] = 930
        else:
            msg['offset'][1] = -100
    else:
        msg['offset'][0] = 100

    return msg
