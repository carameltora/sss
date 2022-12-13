import pyamf
from pyamf import remoting
from pyamf.flex import messaging
import uuid
import requests
import random
from MovieStarPlanet.Security.ChecksumCalculator import ChecksumCalculator
import json


class ActionFormat():
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
        return str(decoded.bodies[0]).replace("('/1', <Response status=/onResult>", "").replace("</Response>)", "")
        
           

        