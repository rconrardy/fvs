import src as fvs
import time
import copy
import cv2
import os

def testFoveated(file, growth, layers, size, resize):
    dev = fvs.Device(file)

    for i in range(layers):
        ratio = 2 ** i
        dev[i] = fvs.Vision(rat=copy.copy(ratio), pxl=size, itr=resize)
        dev[i].function(fvs.haarFaceDetectSetup, fvs.haarFaceDetectFunction)
        dev[i].function(fvs.naiveSearchSetup, fvs.naiveSearchFunction)
    numFrames = int(dev.get(cv2.CAP_PROP_FRAME_COUNT))
    detFrames = 0
    start = time.time()
    for i in range(numFrames):
        ret, frm, det = dev.imread()
        detFrames += det
    totalTime = time.time() - start
    dev.release()
    cv2.destroyAllWindows()
    return numFrames, detFrames, totalTime
