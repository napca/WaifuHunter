from telethon.sync import TelegramClient, events
import config
import re
import os
import schedule
api_id = config.API_ID
api_hash = config.API_HASH

with TelegramClient('session-name' , api_id, api_hash,proxy=("socks5", '127.0.0.1', 9050)) as client:

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





   def rewards():
       client.send_message(1976201765, '/start')
       client.send_message(1976201765, 'Rewards 🎁')
       client.send_message(1976201765, 'Daily Login 🌟')
       client.send_message(1976201765, 'Achievements 🏆')
       client.send_message(1976201765, 'Back 🔙')
       client.send_message(1976201765, 'SHOP 🛍')
       print("werks.")
   schedule.every().day.do(rewards)
#   schedule.run_all()

   @client.on(events.NewMessage(from_users="WaifuGacha_bot"))
   async def handler(event):
         text = event.message.message
         if re.search("🏆 Achievements 🏆", text) is not None :
           await event.click(0)
         if re.search("TICKETS FULL", text) is not None :
            await client.send_message(1976201765, 'Fast Autoplay 🎟🔄')
         if re.search("activate", text) is not None :
           await event.click(0)
         if re.search("🛍 NEW DAILY SHOP! 🛍", text)is not None :
             await event.click(4)
   @client.on(events.MessageEdited(from_users="WaifuGacha_bot"))
   async def handler(event):
        text=event.message.message
        if re.search("You can buy tickets🎟 with diamonds💎", text)is not None:
         diamonds=int(re.search("(?<=Your diamonds: )(.*)(?= 💎)", text).group())
         tickets=int(re.search("(?<=Your Tickets: )(.*)(?= 🎟)", text).group())
         if tickets = 1000:
             await client.send_message(1976201765, '🏖🎰 EVENT BANNER 🎰🏖')
         if diamonds > 65:
             await event.click(3)
         else:
             await client.send_message(1976201765, '🏖🎰 EVENT BANNER 🎰🏖')
   client.run_until_disconnected()

