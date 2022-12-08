import mobiuslib as ml
import sys
import json
import serial
import psutil
import random as r

arduino = serial.Serial('/dev/ttyUSB0', 9600)
#ttyUSB* naming

def sendMonitoringDeviceStatus(AEname, INCSEurl):
    ml.createContentInstance(AEname, "/monitoringDeviceStatus/cpuUsage", psutil.cpu_percent(interval=None), INCSEurl)
    ml.createContentInstance(AEname, "/monitoringDeviceStatus/diskIO", psutil.disk_usage('/').percent, INCSEurl)
    ml.createContentInstance(AEname, "/monitoringDeviceStatus/memory", psutil.virtual_memory().percent, INCSEurl)

def sendFakeDatatoSecStat(AEname, INCSEurl):
    fakebatteryLevel = 100
    fakeRealMotorSpeed = r.randint(25, 35)
    fakeSettedMotorSpeed = r.randint(27, 33)
    ml.createContentInstance(AEname, "/deviceStatus/batteryLevel", fakebatteryLevel, INCSEurl)
    ml.createContentInstance(AEname, "/deviceStatus/realMotorSpeed", fakeRealMotorSpeed, INCSEurl)
    ml.createContentInstance(AEname, "/deviceStatus/settedMotorSpeed", fakeSettedMotorSpeed, INCSEurl)
    fakenTimes = r.randint(0, 100)
    fakepowerSecurity = r.randint(0, 100)
    ml.createContentInstance(AEname, "/deviceSecurityStatus/nTimes", fakenTimes, INCSEurl)
    ml.createContentInstance(AEname, "/deviceSecurityStatus/powerSecurity", fakepowerSecurity, INCSEurl)

def sendData(AEname, INCSEurl):
    highValue = -32768
    lowValue = 32767
    index = 1
    rawdatalist = []
    while True:
        sendMonitoringDeviceStatus(AEname, INCSEurl)
        sendFakeDatatoSecStat(AEname, INCSEurl)
        serialrecvdata = arduino.readline()
        serialrecvdata = serialrecvdata[:-2].decode() #~\r\n
        print(serialrecvdata) #ECG Data: (%d) or (NO SENSOR)
        splitstr = serialrecvdata.split('ECG Data: ')
        rawdata = splitstr[1]
        if rawdata == 'NO SENSOR':
            continue
        else:
            intrawdata = int(rawdata)
            ml.createContentInstance(AEname, "/deviceHealthData/adcData/rawValue/UI", intrawdata, INCSEurl)
            rawdatalist.append(intrawdata)
            if highValue < intrawdata:
                highValue = intrawdata
                ml.createContentInstance(AEname, "/deviceHealthData/adcData/highValue", highValue, INCSEurl)
            if lowValue > intrawdata:
                lowValue = intrawdata
                ml.createContentInstance(AEname, "/deviceHealthData/adcData/lowValue", lowValue, INCSEurl)

            if len(rawdatalist) == 8:
                jsonrawdata = {
                    "index": str(index),
                    "rawdatalist": str(rawdatalist)
                }
                ml.createContentInstance(AEname, "/deviceHealthData/adcData/rawValue/AI", jsonrawdata, INCSEurl)
                index += 1
                rawdatalist = []

if(__name__ == "__main__"):
    AEname = "ID_USER_" + sys.argv[1]
    INCSEurl = sys.argv[2]
    sendData(AEname, INCSEurl)