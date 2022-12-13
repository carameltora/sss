import websockets
import asyncio
import json


class Bot():
   
   def is_op10(jsonLoader: json.loads):
      if str(jsonLoader["op"]) == "10":
         return True
      else:
         return False
      
   async def Create_Connection(token: str):
      HeartBeat: int
      ID: int
      IsConnected: bool
      
      '''
        Connect to the gateway.
        make an infinity loop for keeping receiving messages.
      '''
      async with websockets.connect('wss://gateway.discord.gg/?v=10&encoding=json') as websocket:
         while True:
            response_recv = await websocket.recv()
            try:
               jsLoader = json.loads(response_recv)
               op10 = Bot.is_op10(jsLoader)
               print(op10)
            except:
               pass
        
                
def ah():
   asyncio.run(Bot.Create_Connection("e"))
   
ah()