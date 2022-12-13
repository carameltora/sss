import requests
import json
import pyamf
from pyamf import remoting
from pyamf.flex import messaging
from Security.ChecksumCalculator import ChecksumCalculator
from dataclasses import dataclass


@dataclass
class GetOsResult:
   RefId: str
   TjData: str
   tjParser: json.loads
    
    
class ActionFormat():
    
    listas = json.loads
    def initA():
        with open("yj5jmgn790mr.txt") as f:
            ds = json.loads(f.read())
            ActionFormat.listas = ds
                    
    
    def f(x):
        try:
            return json.loads(x)
        except:
            pass

    def AMF3(Endpoint, Method, Content, HashID: bool, SessionID=None):
        if Content is None:
            req = remoting.Request(target=Method)
        else:
            req = remoting.Request(target=Method, body=Content)
        ev = remoting.Envelope(pyamf.AMF3)
        if HashID:
            ev.headers["sessionID"] = SessionID
        if Content is not None:
            ev.headers["id"] = ChecksumCalculator.createChecksum(Content)
            
        ev.headers["needClassName"] = False
        ev['/1'] = req 

        # Encode request 
        bin_msg = remoting.encode(ev)
        headers = {
            'Content-Type': 'application/x-amf',
            'Referer': 'app:/cache/t1.bin/[[DYNAMIC]]/2',
            'X-Flash-Version': '32,0,0,100',
            'Accept': 'text/xml, application/xml, application/xhtml+xml, text/html;q=0.9, text/plain;q=0.8, text/css, image/png, image/jpeg, image/gif;q=0.8, application/x-shockwave-flash, video/mp4;q=0.9, flv-application/octet-stream;q=0.8, video/x-flv;q=0.7, audio/mp4, application/futuresplash, */*;q=0.5, application/x-mpegURL'
        }
        response = requests.post(Endpoint + "/Gateway.aspx?method=" + Method, data=bin_msg.getvalue(), headers=headers)      
        decoded = remoting.decode(response.content)
        return str(decoded.bodies).replace("[('/1', <Response status=/onResult>", "").replace("</Response>)]", "")
    
        
        
def GetEndpoint(Server):
    ds = requests.get("https://disco.mspapis.com/disco/v1/services/msp/" + Server + "?services=mspwebservice").text
    dss = json.loads(str(ds))
    return dss["Services"][0]["Endpoint"]

def GetOs():
    response = ActionFormat.AMF3(GetEndpoint("FR"), "MovieStarPlanet.WebService.Os.AMFOs.CreateOsRef", HashID=True, Content=None, SessionID="NGEzNzBhYzcyZWIwNWUyODZmMGYyNGNhMzVlY2ViYTQ0NjM3NDdmMzUxMzgzMw==")
    TjData = "eNqNVc1vG0UU33Umm8TGdS0rcqMoSmhUJCCR/BEnsVBFEztpLcVp6Doth1Iz9o7tSdc71szYsSsE3ZZKCITEiSv/AAf+Af6ESkhwgQsnLkh8HDgiwZtZ2zFphDqRMm8+dt7v997vPYefJSI7dcl47C7tVCjh1/TqDnGxpMwTLdoRMfsh9ex7+zF9VHISewNit7DDTuNFitvMc4TaKjCXcREBq+TE1H9J2svjq8FpcrwuOYtnNtyc28dtEttnXHY9ktznlHhOgXU9uTRhA8ZYSez1JceJAyzkAWtSL3JAesR9s0zaNcIV4AptE9aVRSxJoswcwjHAjpSZRwbJMhy0AiwxbQOdYFYYDgFD9JAJYBDXE2wuHLHOcceWAxd2E3cYax/Qh0QkVFD0Q6+PrZLXIx74GpSca3aHUwn8CJF3ARbEcqHCJHaBQhEPRNz2cEe0mFwYGTfB9/IhqXVdfMRZgyp3MxCiOQUkojG+qhNQcJlsEQEpEugfGKY13yBt7BIBOIIdZFjr6VRmLdVP6bGmjuoKIpozTH3HQOM/E5mmmq1r42tr6c2tdDqfzaEZw4Jzfc+K5XOZrXQqN3Jimmb4qX1wOVES9wjm1GsuFkkDd10ZRHgjXhK3qOMQb1ll65CcVnCzSZzb3qJaH3ccSBGskrdPPeIMFVLG1Ku0SBvoR1v64+mSE6ECvp4BEc7fIU0wjwXhiyP1HXFaJ1GVBripFwkBQmIcch+HgGuBLLljCEoZ80WOm8zbBVUkJ8CAokVdSW0GvouUlFdQnMaXsOHN2+rN9Z0epi6uUZfKAUh2iCd6E3RKIMQh01oqsx4lQmK+cpNyN2SqEId0FBeDbFXJgIhqBiHYNNGTNXQFGbPmLv/zxl83DCMEZvfbzc8yR8MkhYIJ4n14f/PBxvs1p9E6cb0Ol73+ow8+9A0/5CPf8mf9sP+Kf8m/HIKsWtEjIkGGk+6jHuipmjvzewn8IuWv99Xz339+/IK/o9T9l/GHZoB2vMCYu1LActLj0pBwW2m4mr3Y82/py//1PDdnhv3V5XOSXz23hpIcLkrObLxIBG2CCO5H9GZES2qqHw32pwbTO998Qn4yDAN98RF69uvXP4K0w0+E/1pS37TrSnf+1Y2o3WKdkrM8fBr4kCaUdcSuA4+krhBbKr2rfiIIYIL6XhqqwiXHnqRudsejbd1ECwz6AleWLbHsimEQY0OVB4FcPecLOtA+9AAPuoL1jhNUlXZ8fXIBFd5o5PNQ4ZoA0LKWKpx1KABduYd7RCAULvgbG/7uvA0OKoOO6m0j05q7hSlHqgFMv/19Vg9V10E3OOm6g+owdy24V90Ypu6pVBcgb6flP64++i7Im2lB+lP9bNbJ4W39Rjiu4/2LiveX0+N4z5uwshZ3oRUMVirrdotyCdsLVlSbAoVQ6AI46yfYq2ZS6fQIkmQdUU2P1PRgeuf589oPjw2F7IpGFAJEsVS/ltnO5SYB/a0Aff7GGSDLj/1fhDdhZLNBhN/Sm+K6nlSD3d/b285n1na7UsLPJTxrLahG5A2gCkDwmlgcUgIy4QJNoamLqJUxr7eqNQZvtMWI36hQPn4XnXGaAk6rqT7J4PRWWmHL1zfr9Ql2jVnF7tP3Xppdo1Gvj/TzAruGHmtFIkHaAp61EjuuuwI65o/QFFCLQKWAyMJo+gJeWdFttwmvttRPL+Qula8KdX0oJAM93Z2gFg6oYWfbcXLgeyuNSZ7ot/4Fq9mTeg=="
    
    
def RunOs(RefId, TjData):
    with open("yj5jmgn790mr.txt") as f:
        gf = str(f.readlines()).split(',')
        fdit = dict()
        fdit.clear()
        lengthJSON = len(gf)
        for x in range(lengthJSON):
            if [x]["TjData"] not in fdit:
                fdit[x]["TjData"] = [x]['Histogram']
            
    
    ct = [RefId, fdit[TjData]]
    response = ActionFormat.AMF3(GetEndpoint("FR"), "MovieStarPlanet.WebService.Os.AMFOs.RunOsCheck", HashID=True, Content=ct, SessionID="NGEzNzBhYzcyZWIwNWUyODZmMGYyNGNhMzVlY2ViYTQ0NjM3NDdmMzUxMzgzMw==")
    print(response)
    
def GetSessionID():
    val1 = GetOs()
    des = RunOs("3a0a2b7e-0b9c-4f75-b8b4-34fec9ccda4a", "eNqNVc1vG0UU33Umm8TGdS0rcqMoSmhUJCCR/BEnsVBFEztpLcVp6Doth1Iz9o7tSdc71szYsSsE3ZZKCITEiSv/AAf+Af6ESkhwgQsnLkh8HDgiwZtZ2zFphDqRMm8+dt7v997vPYefJSI7dcl47C7tVCjh1/TqDnGxpMwTLdoRMfsh9ex7+zF9VHISewNit7DDTuNFitvMc4TaKjCXcREBq+TE1H9J2svjq8FpcrwuOYtnNtyc28dtEttnXHY9ktznlHhOgXU9uTRhA8ZYSez1JceJAyzkAWtSL3JAesR9s0zaNcIV4AptE9aVRSxJoswcwjHAjpSZRwbJMhy0AiwxbQOdYFYYDgFD9JAJYBDXE2wuHLHOcceWAxd2E3cYax/Qh0QkVFD0Q6+PrZLXIx74GpSca3aHUwn8CJF3ARbEcqHCJHaBQhEPRNz2cEe0mFwYGTfB9/IhqXVdfMRZgyp3MxCiOQUkojG+qhNQcJlsEQEpEugfGKY13yBt7BIBOIIdZFjr6VRmLdVP6bGmjuoKIpozTH3HQOM/E5mmmq1r42tr6c2tdDqfzaEZw4Jzfc+K5XOZrXQqN3Jimmb4qX1wOVES9wjm1GsuFkkDd10ZRHgjXhK3qOMQb1ll65CcVnCzSZzb3qJaH3ccSBGskrdPPeIMFVLG1Ku0SBvoR1v64+mSE6ECvp4BEc7fIU0wjwXhiyP1HXFaJ1GVBripFwkBQmIcch+HgGuBLLljCEoZ80WOm8zbBVUkJ8CAokVdSW0GvouUlFdQnMaXsOHN2+rN9Z0epi6uUZfKAUh2iCd6E3RKIMQh01oqsx4lQmK+cpNyN2SqEId0FBeDbFXJgIhqBiHYNNGTNXQFGbPmLv/zxl83DCMEZvfbzc8yR8MkhYIJ4n14f/PBxvs1p9E6cb0Ol73+ow8+9A0/5CPf8mf9sP+Kf8m/HIKsWtEjIkGGk+6jHuipmjvzewn8IuWv99Xz339+/IK/o9T9l/GHZoB2vMCYu1LActLj0pBwW2m4mr3Y82/py//1PDdnhv3V5XOSXz23hpIcLkrObLxIBG2CCO5H9GZES2qqHw32pwbTO998Qn4yDAN98RF69uvXP4K0w0+E/1pS37TrSnf+1Y2o3WKdkrM8fBr4kCaUdcSuA4+krhBbKr2rfiIIYIL6XhqqwiXHnqRudsejbd1ECwz6AleWLbHsimEQY0OVB4FcPecLOtA+9AAPuoL1jhNUlXZ8fXIBFd5o5PNQ4ZoA0LKWKpx1KABduYd7RCAULvgbG/7uvA0OKoOO6m0j05q7hSlHqgFMv/19Vg9V10E3OOm6g+owdy24V90Ypu6pVBcgb6flP64++i7Im2lB+lP9bNbJ4W39Rjiu4/2LiveX0+N4z5uwshZ3oRUMVirrdotyCdsLVlSbAoVQ6AI46yfYq2ZS6fQIkmQdUU2P1PRgeuf589oPjw2F7IpGFAJEsVS/ltnO5SYB/a0Aff7GGSDLj/1fhDdhZLNBhN/Sm+K6nlSD3d/b285n1na7UsLPJTxrLahG5A2gCkDwmlgcUgIy4QJNoamLqJUxr7eqNQZvtMWI36hQPn4XnXGaAk6rqT7J4PRWWmHL1zfr9Ql2jVnF7tP3Xppdo1Gvj/TzAruGHmtFIkHaAp61EjuuuwI65o/QFFCLQKWAyMJo+gJeWdFttwmvttRPL+Qula8KdX0oJAM93Z2gFg6oYWfbcXLgeyuNSZ7ot/4Fq9mTeg==")
    
     
GetSessionID()