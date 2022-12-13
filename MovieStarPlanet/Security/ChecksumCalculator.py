from array import array
from ast import Or
from datetime import datetime
import hashlib 
import MovieStarPlanet.Entities.TicketHeader as tk


class ChecksumCalculator:
    def createChecksum(arguments, ticket = None):
        text = ChecksumCalculator.fromArray(arguments)
        endData = "v1n3g4r"
        if ticket is not None:
            endData = ticket.split(",").pop()[0:5]     
        logData = '$CuaS44qoi0Mp2qp'
        return str(hashlib.sha1(str(text + endData + logData).encode('utf-8')).hexdigest())
   
   
    def fromArray(arguments):
       if arguments is None:
           return ""
       text = ""
       for item in arguments:
           text += ChecksumCalculator.fromObjectInner(item)
       return text
   
   
    def getEndData(arguments):
        for item in arguments:
            if isinstance(arguments, tk.TicketHeader):
                return str(arguments.Ticket).split(",").pop()[0:5]
        return "v1n3g4r"
    
    
    def fromObjectInner(param1):
        if param1 is None or isinstance(param1, tk.TicketHeader):
           return ""
        if isinstance(param1, str) or isinstance(param1, int):
            return str(param1)
        if isinstance(param1, bool):
            if param1 is True:
                return "True"
        if param1 is False:
            return "False"
        if isinstance(param1, datetime):
            return str(param1.year + param1.month + param1.day)
        if isinstance(param1, list):
            return ChecksumCalculator.fromArray(param1)
        if param1 is not None:
            return ChecksumCalculator.fromObject(param1)
        
        
    def fromObject(param1):
        listlo = dir(param1).sort()
        text = ""
        for item in listlo:
            text += ChecksumCalculator.fromObjectInner(param1[item])
        return text
   
   