import pyamf
import requests
from pyamf.flex import messaging
from pyamf import remoting
import amf
import json
from dataclasses import dataclass
from datetime import datetime
from MovieStarPlanet.Security.ChecksumCalculator import ChecksumCalculator

@dataclass
class CreateOsResult:
    RefId: str
    TjData: str
    
    
def GetEndpointForServer(Server):
        endpointresponse = requests.get("https://disco.mspapis.com/disco/v1/services/msp/" + Server + "?services=mspwebservice")
        return endpointresponse.json()["Services"][0]["Endpoint"]

def GetHisto(TjData):
    with open("yj5jmgn790mr.txt", "r") as f:
        lines = f.read()
        jsd = json.loads(lines)
        lght = len(jsd)
        for x in range(lght):
            if jsd[x]["TjData"] == TjData:
                return str(jsd[x]["Histogram"])
          
def createOs():
    msg = messaging.RemotingMessage(body=[])
    req = remoting.Request(target="MovieStarPlanet.WebService.Os.AMFOs.CreateOsRef")
    ev = remoting.Envelope(pyamf.AMF3)      
    ev.headers["sessionID"] = "NGEzNzBhYzcyZWIwNWUyODZmMGYyNGNhMzVlY2ViYTQ0NjM3NDdmMzUxMzgzMw=="
    ev.headers["needClassName"] = False 
    ev['/1'] = req      
    bin_msg = remoting.encode(ev)
    response = requests.post(GetEndpointForServer("FR") + "/Gateway.aspx?method=" + "MovieStarPlanet.WebService.Os.AMFOs.CreateOsRef", data=bin_msg.getvalue(), headers={
       "Content-Type": "application/x-amf",
      "Referer": "app:/cache/t1.bin/[[DYNAMIC]]/2"
    })
    resp_msg = remoting.decode(response.content)
    dd = str(resp_msg.bodies).replace("</Response>)]", "").replace("[('/1', <Response status=/onResult>", "")
    splited = dd.split(",", maxsplit=2)[2]
    response = dd.replace(splited, "")[:-1] + "}"
    response = str(response).replace("'", '"')
    fg = json.loads(response)
    return CreateOsResult(RefId=fg['RefId'], TjData=fg['TjData'])
    
def RunOs(RefId, TjData):
    d = [str(RefId), str(GetHisto(TjData))]
    msg = messaging.RemotingMessage(body=pyamf.encode(d, encoding=pyamf.AMF3).getvalue())
    req = remoting.Request(target="MovieStarPlanet.WebService.Os.AMFOs.RunOsCheck", body=[msg])
    ev = remoting.Envelope(pyamf.AMF3)      
    ev.headers["sessionID"] = "MzIyMzBmZTA3ZjNjZDkzYTZjNTJiNjU2MTRmM2JlNjUyMGEyNGFlMzNlZjZjZQ=="
    ev.headers["needClassName"] = True
    ev['/1'] = req      
    bin_msg = remoting.encode(ev)
    response = requests.post(GetEndpointForServer("FR") + "/Gateway.aspx?method=MovieStarPlanet.WebService.Os.AMFOs.RunOsCheck", data=bin_msg.getvalue(), headers={
       "Content-Type": "application/x-amf",
      "Referer": "app:/cache/t1.bin/[[DYNAMIC]]/2"
    })
    print(response.content)
   
       
    

ds = createOs()
RunOs(ds.RefId, ds.TjData)

    
    
