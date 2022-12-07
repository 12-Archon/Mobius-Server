import mobiuslib as ml
import sys
import json

#serverURL = "http://server.dochoon.com:7579"
#webserver = "http://123.123.123.123:8080"
'''
usage: python3 main.py AEname dserverurl INCSEurl
'''

def makeResource(AEname, dserverurl, INCSEurl):
    ml.createApplicationEntity(AEname, INCSEurl)

    ml.createContainer(AEname, "/deviceHealthData", INCSEurl)
    ml.createContainer(AEname, "/deviceHealthData/adcData", INCSEurl)
    ml.createContainer(AEname, "/deviceHealthData/adcData/highValue", INCSEurl)
    ml.createContainer(AEname, "/deviceHealthData/adcData/lowValue", INCSEurl)
    ml.createContainer(AEname, "/deviceHealthData/adcData/rawValue", INCSEurl)
    ml.createContainer(AEname, "/deviceHealthData/adcData/rawValue/AI", INCSEurl)
    ml.createContainer(AEname, "/deviceHealthData/adcData/rawValue/UI", INCSEurl)
    ml.createContainer(AEname, "/deviceHealthData/adcData/train", INCSEurl)

    ml.createContainer(AEname, "/deviceHealthData/result", INCSEurl)
    ml.createSubscription(AEname, "/deviceHealthData/result", dserverurl, INCSEurl)

    ml.createContainer(AEname, "/deviceSecurityStatus", INCSEurl)
    ml.createContainer(AEname, "/deviceSecurityStatus/nTimes", INCSEurl)
    ml.createContainer(AEname, "/deviceSecurityStatus/powerSecurity", INCSEurl)

    ml.createContainer(AEname, "/deviceStatus", INCSEurl)
    ml.createContainer(AEname, "/deviceStatus/batteryLevel", INCSEurl)
    ml.createContainer(AEname, "/deviceStatus/realMotorSpeed", INCSEurl)
    ml.createContainer(AEname, "/deviceStatus/settedMotorSpeed", INCSEurl)

    ml.createContainer(AEname, "/monitoringDeviceStatus", INCSEurl)
    ml.createContainer(AEname, "/monitoringDeviceStatus/cpuUsage", INCSEurl)
    ml.createContainer(AEname, "/monitoringDeviceStatus/diskIO", INCSEurl)
    ml.createContainer(AEname, "/monitoringDeviceStatus/memory", INCSEurl)

    ml.createContainer(AEname, "/modelFile", INCSEurl)
    ml.createContainer(AEname, "/modelFile/yyyymmdd", INCSEurl)
    #ml.createSubscription(AEname, "/modelFile/yyyymmdd", serverurl, INCSEurl) -> AI use

    #[a, b, c, d, e, f, g, h], x  ->  fixing Resource form
    ml.createContainer(AEname, "/learningDataForm", INCSEurl)
    ml.createContainer(AEname, "/learningDataForm/idx1", INCSEurl) #[
    ml.createContainer(AEname, "/learningDataForm/idx2_8", INCSEurl) #, 
    ml.createContainer(AEname, "/learningDataForm/idx9", INCSEurl) #]
    ml.createContainer(AEname, "/learningDataForm/idx10", INCSEurl) #, 
    ml.createContainer(AEname, "/learningDataForm/wholeform", INCSEurl) #[a, b, c, d, e, f, g, h], x
    ml.createContainer(AEname, "/learningDataForm/data", INCSEurl)
    ml.createContainer(AEname, "/learningDataForm/label", INCSEurl)

def sendFixedData(AEname, INCSEurl):
    idx1 = {
        'description': 'Start of rawdata list',
        'symbol': '['
    }
    idx2_8 = {
        'description': 'Distinguisher of rawdata',
        'symbol': ', '
    }
    idx9 = {
        'description': 'End of rawdata list',
        'symbol': ']'
    }
    idx10 = {
        'description': 'Distinguisher between rawdatalist and label',
        'symbol': ', '
    }
    ml.createContentInstance(AEname, "/learningDataForm/idx1", idx1, INCSEurl)
    ml.createContentInstance(AEname, "/learningDataForm/idx2_8", idx2_8, INCSEurl)
    ml.createContentInstance(AEname, "/learningDataForm/idx9", idx9, INCSEurl)
    ml.createContentInstance(AEname, "/learningDataForm/idx10", idx10, INCSEurl)
    ml.createContentInstance(AEname, "/learningDataForm/wholeform", '[a, b, c, d, e, f, g, h], x', INCSEurl)
    MLdata = {
        'type': 'list',
        'data length': 8,
        'description': 'list have 8 of raw ECG data'
    }
    MLlabel = {
        'type': 'bool',
        'data length': 1,
        'description': '0 means normal, 1 means abnormal'
    }
    ml.createContentInstance(AEname, "/learningDataForm/data", MLdata, INCSEurl)
    ml.createContentInstance(AEname, "/learningDataForm/label", MLlabel, INCSEurl)

if(__name__ == "__main__"):
    AEname = "ID_USER_"+sys.argv[1]
    dserverurl = sys.argv[2] #device server
    INCSEurl = sys.argv[3]
    makeResource(AEname, dserverurl, INCSEurl)
    sendFixedData(AEname, INCSEurl)