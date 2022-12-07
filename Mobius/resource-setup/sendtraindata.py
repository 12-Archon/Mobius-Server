import mobiuslib as ml
import sys
import json
import time

if(__name__ == "__main__"):
    AEname = "ID_USER_" + sys.argv[1]
    INCSEurl = sys.argv[2]
    datalist = []
    index = int(time.time())
    for i in range(0, 8):
        data = int(input("input data for train(ecg data): "))
        datalist.append(data)
    data = int(input("input label for train(0 is normal 1 is abnormal): "))
    if data != 0 and data != 1:
        print("Wrong data")
    else:
        jsondata = {
            "index" : index,
            "ecg" : datalist,
            "abnormal" : data
        }
        ml.createContentInstance(AEname, "/deviceHealthData/adcData/train", jsondata, INCSEurl)