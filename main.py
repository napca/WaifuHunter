from telethon.sync import TelegramClient, events
from promise import Promise
import config
import re
import os
import schedule
import time
import asyncio
from threading import Thread
api_id = config.API_ID
api_hash = config.API_HASH

with TelegramClient('session-name' , api_id, api_hash) as client:

   print("Started.")
   def rewards():
       while True:
        client.send_message(1976201765, '/start')
        time.sleep(3)
        client.send_message(1976201765, 'Rewards 🎁')
        time.sleep(10)
#   rewards()
#   async def rewards():
#        print(1)
#        print(2)
#        await Promise.all([client.send_message(1976201765, '/start'), client.send_message(1976201765, 'Rewards 🎁')]);
#        asyncio.close()
#        print('werks.')
#   def thread():
#       while True:
#           asyncio.run(rewards())
#           time.sleep(10)
#   Thread(target=thread).start()


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
   @client.on(events.NewMessage(from_users="StarkTelegraphBot"))
   async def handler(event):
         text = event.message.message
         if re.search('File is ready to Upload', text) is not None :
           await event.click(0)
         if re.search('https://', text) is not None :
            message = event.message
            cmd = 'URL=' + message.message + ' ./cmd.sh'
            print(os.system(cmd))
            out = os.popen(cmd).read()
            text = '/protecc ' + out
            await client.send_message(-1001384823039, text)





   @client.on(events.NewMessage(from_users="WaifuGacha_bot"))
   async def handler(event):
         text = event.message.message
         if re.search("🎁 REWARDS 🎁", text) is not None :
             print("cum")
             await client.send_message(1976201765, 'Daily Login 🌟')
             time.sleep(1)
             await client.send_message(1976201765, 'Achievements 🏆')
             time.sleep(1)
             await client.send_message(1976201765, 'Back 🔙')
             time.sleep(3)
             await client.send_message(1976201765, 'SHOP 🛍')
         if re.search("TICKETS FULL", text) is not None :
            await client.send_message(1976201765, 'Fast Autoplay 🎟🔄')
         if re.search("activate", text) is not None :
           await event.click(0)
         if re.search("🛍 NEW DAILY SHOP! 🛍", text)is not None :
             await event.click(4)
         if re.search("🗓 WEEKLY REWARD 🗓", text) is not None :
             await event.click(0)
         if re.search("🏆 Achievements 🏆", text) is not None :
           await event.click(0)
   @client.on(events.MessageEdited(from_users="WaifuGacha_bot"))
   async def handler(event):
        text=event.message.message
        if re.search("You can buy tickets🎟 with diamonds💎", text)is not None:
         diamonds=int(re.search("(?<=Your diamonds: )(.*)(?= 💎)", text).group())
         tickets=int(re.search("(?<=Your Tickets: )(.*)(?= 🎟)", text).group())
         if tickets == 1000:
             await client.send_message(1976201765, 'PLAY NOW! 🎟')
         if diamonds >= 65:
             await event.click(3)
         else:
           await client.send_message(1976201765, 'PLAY NOW! 🎟')
   client.run_until_disconnected()

