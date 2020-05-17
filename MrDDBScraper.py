from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
import csv
 
api_id = 1049984
api_hash = 'b761cd6f412e62cce12b0cceb0d4e3f1'
phone = '+17062523105'
client = TelegramClient(phone, api_id, api_hash)
 
client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code: '))
 
 
chats = []
last_date = None
chunk_size = 200
groups=[]
 
result = client(GetDialogsRequest(
             offset_date=last_date,
             offset_id=0,
             offset_peer=InputPeerEmpty(),
             limit=chunk_size,
             hash = 0
         ))
chats.extend(result.chats)
 
for chat in chats:
    try:
        if chat.megagroup== True:
            groups.append(chat)
    except:
        continue
 
print('join My Youtube Channel Tech DDB ')
print('link :- https://www.youtube.com/channel/UCPMhxTNY0h0z1mzsrD6FP_w ')
print('Choose a group to scrape members from:')
i=0
for g in groups:
    print(str(i) + '- ' + g.title)
    i+=1
 
g_index = input("Enter a Number: ")
target_group=groups[int(g_index)]
 
print('Fetching Members...')
all_participants = []
all_participants = client.get_participants(target_group, aggressive=True)
 
print('Saving In file...')
with open("members.csv","w",encoding='UTF-8') as f:
    writer = csv.writer(f,delimiter=",",lineterminator="\n")
    writer.writerow(['username'])
    for user in all_participants:
        if user.username:
            username= user.username
        else:
            username= ""
        writer.writerow([username])      
print('Members scraped successfully.')
print('Subscribe My Youtube Channel. Thanks For Use This Script.')
