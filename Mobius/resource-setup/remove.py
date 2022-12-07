import requests, json

serverURL="http://server.dochoon.com:7579"

#get ae_list
def getApplicationEntityList(): # return AE name list
    header = {
        "Accept":"application/json",
        "X-M2M-RI":"12345",
        "X-M2M-Origin":"S",
    }
    res = requests.get(serverURL+"/Mobius?fu=1&ty=2&lim=20", headers=header, data="")

    #print(res.json())
    
    res = res.json()['m2m:uril']
    for i, s in enumerate(res): # make ae name list
        res[i] = s[7:]
    
    return res

#remove all_ae
def removeAllApplicationEntity():
    ae_list = getApplicationEntityList()
    for step in ae_list:
        removeApplicationEntity(step)

#get ae_ri
def getApplicationEntityRI(ae_name):
    header = {
        "Accept":"application/json",
        "X-M2M-RI":"12345",
        "X-M2M-Origin":"S",
    }
    res = requests.get(serverURL+"/Mobius/"+ae_name, headers=header, data="")
    res = res.json()
    ae_ri = res["m2m:ae"]["ri"]
    print(res)
    return ae_ri

#remove ae_name
def removeApplicationEntity(ae_name):
    ri = getApplicationEntityRI(ae_name)

    header = {
        "Accept":"application/json",
        "X-M2M-RI":"12345",
        "X-M2M-Origin":ri,
    }
    res = requests.delete(serverURL+"/Mobius/"+ae_name, headers=header, data="")
    res = res.json()
    print(res)


