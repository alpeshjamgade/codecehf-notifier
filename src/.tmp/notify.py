import requests
import bs4
from bs4 import BeautifulSoup as bs
import os
import notify2
import html
import pyttsx3



res = requests.get("https://codechef.com/users/alpeshjamgade")
# print(res.status_code)
# print(res.headers)

src = res.content
soup = bs4.BeautifulSoup(src, 'html.parser')

rating = soup.find("div", {"class": "rating-number"})
# for i in rating:
# 	print(i.string)
# 	notify2.init('app name')
# 	n = notify2.Notification("Codechef", "New Rating "+ i.string, icon="/home/alpeshjamgade/myworld/web-scrapping/chef-hat.png")
# 	n.show()
# 	n.set_timeout(1000)


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[13].id)
# for voice in voices:
#     print(voice, voice.id)
#     engine.setProperty('voice', voice.id)
#     engine.say("Mother Fucker")
#     engine.runAndWait()
#     engine.stop()

# engine.say("Notification sir, The quick brown fox jumped over the lazy dog.")
# engine.runAndWait()
def speakUp(message):
	engine = pyttsx3.init()
	voices = engine.getProperty('voices')
	engine.setProperty('voice', voices[13].id)
	engine.say("Notifiacation sir, " + message)
	engine.runAndWait()

def notify(title, message, icon_path):
	notify2.init('app name')
	n = notify2.Notification(title, message, icon=icon_path)
	n.show()
	n.set_timeout(1000)
	speakUp(message)

notify("Codecehf", "New Rating "+rating.string, "/home/alpeshjamgade/myworld/web-scrapping/chef-hat.png")

