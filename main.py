from telethon.sync import TelegramClient, events
import config
import time
from random import randrange
import re
import os

api_id = config.API_ID
api_hash = config.API_HASH

with TelegramClient('session-name' , api_id, api_hash,proxy=("socks5", '127.0.0.1', 10805)) as client:
   print("Started.")
   @client.on(events.NewMessage(from_users="Collect_your_husbando_bot"))
   async def handler(event):
        message = event.message
        if(message.photo is not None): #check message has photo
         await   client.forward_messages("@StarkTelegraphBot" , event.message)

   @client.on(events.NewMessage(from_users="loli_harem_bot"))
   async def handler(event):
    message = event.message
    if(message.photo is not None): #check message has photo
         await   client.forward_messages("@StarkTelegraphBot" , event.message)
   @client.on(events.MessageEdited(from_users="StarkTelegraphBot"))
   async def handler(event):
    message = event.message
    cmd = 'URL=' + message.message + ' ./cmd.sh'
    print(os.system(cmd))
    out = os.popen(cmd).read()
    text = '/protecc ' + out
    await client.send_message(-1001384823039, text)
   client.run_until_disconnected()
