import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
from random import choice
import json
import requests
from pprint import pprint

TOKEN = '431681149:AAGZpd-m_YAIuzuXwwg_nJscAmwq3Ehsg9Q'

def print_msg(msg):
    print(json.dumps(msg, indent=4))

def on_chat(msg):
    header = telepot.glance(msg, flavor="chat")
    print_msg(msg)
    ans = ""

    if header[0] == "text":
        text = msg["text"]
        if text.startswith("/"):
            command = text.lstrip("/")
           
            if command == "start" :
                bot.sendMessage(header[2],"OK， {}\n你準備好了...... 就直接開始".format(msg['from']['first_name']))
            
            elif command[:1] == "search" :
                ans == command[1:].split()
                    
                def 查歌單(ans) :
                    raw = requests.get('https://www.googleapis.com/youtube/v3/search?part=snippet&q=' + ans[1] + '&key=AIzaSyC-tL1Jz-02hKA7ZPlAI0xTHKpCO-Om6L8')
                    raw_json = json.loads(raw.text)
                    item = raw_json['items'][0]
                    url = 'https://www.youtube.com/watch?v=' + item['id']['videoId']
                    pprint(keys)
                    print('successful')
                    bot.sendMessage(header[2],url)
                查歌單(ans)

        #else:
         #   def 查歌單(keys) :
         #       raw = requests.get('https://www.googleapis.com/youtube/v3/search?part=snippet&q=' + keys + '&key=AIzaSyC-tL1Jz-02hKA7ZPlAI0xTHKpCO-Om6L8')
          #      raw_json = json.loads(raw.text)
          #      item = raw_json['items'][0]
         #       url = 'https://www.youtube.com/watch?v=' + item['id']['videoId']
          #      pprint(keys)
           #     bot.sendMessage(header[2],url)

           # print('Video sent')
           # bot.sendVideo(header[2],查歌單(keys) )

bot = telepot.Bot(TOKEN)
MessageLoop(bot, {
  'chat': on_chat
}).run_as_thread()


print('Listening ...')            