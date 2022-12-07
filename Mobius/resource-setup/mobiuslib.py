import requests

def createApplicationEntity(AEname, serverURL):
    header = {
        "Accept":"application/json",
        "X-M2M-RI":"12345",
        "X-M2M-Origin":"S",
        "Content-Type":"application/json;ty=2"
    }
    body = {
        "m2m:ae":{
            "rn":AEname,
            "api":"0.2.481.2.0001.001.000111",
            "lbl":["key1","key2"],
            "rr": True,
            "poa":["http://203.254.173.104:9727"]
        }
    }
    res = requests.post(serverURL+"/Mobius", headers=header, json=body)
    print(res.json())


def getApplicationEntity(AEname, serverURL):
    header = {
        "Accept":"application/json",
        "X-M2M-RI":"12345",
        "X-M2M-Origin":"S",
    }
    res = requests.get(serverURL+"/Mobius/"+AEname, headers=header, data="")
    print(res.json())


def createContainer(AEname,  dir, serverURL):
    dir = addSlash(dir)
    header = {
        "Accept": "application/json",
        "X-M2M-RI":"12345",
        "X-M2M-Origin":AEname,
        "Content-Type":"application/vnd.onem2m-res+json; ty=3"
    }
    name = dir.split('/')[-1]
    udir = '/'.join(dir.split('/')[0:-1])
    print("udir:", udir)
    print("name:", name)
    body = {
        "m2m:cnt":{
            "rn":name,
            "lbl":[name],
            "mbs":16384
        }
    }
    res = requests.post(serverURL+"/Mobius/"+AEname+udir, headers=header, json=body)
    print(res.json())


def getContainer(AEname, dir, serverURL):
    dir = addSlash(dir)
    header = {
        "Accept":"application/json",
        "X-M2M-RI":"12345",
        "X-M2M-Origin":AEname,
    }
    res = requests.get(serverURL+"/Mobius/"+AEname+dir, headers=header, data="")
    print(res.json())


def deleteContainer(AEname, dir, serverURL):
    dir = addSlash(dir)
    header = {
        "Accept": "application/json",
        "locale":"ko",
        "X-M2M-RI":"12345",
        "X-M2M-Origin":AEname
    }
    res = requests.delete(serverURL+"/Mobius/"+AEname+dir, headers=header, data = "")
    print(res.json())


#have to make COMMAND
def createSubscription(AEname, dir, webserver, serverURL):
    dir = addSlash(dir)
    header = {
        "X-M2M-Origin": AEname,
        "X-M2M-RI": "12345",
        "Content-Type": "application/json;ty=23"
    }
    body = {
        "m2m:sub": {
            "rn": "sub",
            "nu": [webserver + "?ct=json"],
            "nct": 1,
            "enc": {
                "net": [3]
            }
        }
    }
    res = requests.post(serverURL+"/Mobius/"+AEname+dir, headers=header, json=body)
    print(res.json())


def createContentInstance(AEname, dir, con, serverURL):
    dir = addSlash(dir)
    header = {
        "Accept": "application/json",
        "X-M2M-Origin": AEname,
        "X-M2M-RI": "12345",
        "Content-Type": "application/json;ty=4"
    }
    body = {
        "m2m:cin":{
            "con": con
        }
    }
    res = requests.post(serverURL+"/Mobius/"+AEname+dir, headers=header, json=body)
    print(res.json())

def addSlash(string):
    if string[0] != '/':
        string = '/' + string
    return string