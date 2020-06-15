from selenium import webdriver
from bs4 import BeautifulSoup as bs
import lxml
import notify2
import pyttsx3
import json

urls = {"codecehf":"https://www.codechef.com/users/", "leetcode":"https://www.leetcode.com"}
url = 'https://www.codechef.com/users/'


def speakUp(message):
	engine = pyttsx3.init()
	voices = engine.getProperty('voices')
	engine.setProperty('voice', voices[13].id)
	engine.say("Notifiacation sir, " + message)
	engine.runAndWait()

def notify(message):
	notify2.init('app name')
	n = notify2.Notification("Codechef", message, icon='./data/chef-hat.png')
	n.show()
	n.set_timeout(1000)

def check(res):
	soup = bs(res, 'lxml')
	# print(type(soup))
	new_submission = soup.find('table', {'class':'dataTable'}).tbody.tr
	cnt = 0
	DateTime = ""
	Problem = ""
	Result = ""
	Lang = ""
	for data in new_submission:
		if (cnt == 0):
			DateTime = data.string
		elif (cnt == 1):

			Problem = data.string
		elif (cnt == 2):
			Result = data.span.text
		else:
			Lang = data.string
		cnt += 1

	l = [Problem, Result, Lang]
	return l


def helper():
	f = open("./data/user.json")
	data = json.load(f)
	for platforms in data:
		url = platform["url"]
		for user in platforms["users"]:
			name = user["name"]
			id = user["id"]
			driver.get(url+id)
			res = driver.execute_script("return document.documentElement.outerHTML")

			l = check(res)
			if(type[l[1]] == None):
				l[1] = 0;
			_msg = l[0]+l[1]+l[2]
			if(_msg != user["ls"]):
				notify(user['name'] + " | "+ l[0] + " | "+ l[1] + " | "+l[2])
				user["ls"] = _msg
				f2 = open("./data/user.json", "w+")
				f2.write(json.dumps(data))
				f2.close()
	f.close()

def main():
	f = open('./data/user.json',)
	data = json.load(f)
	options = webdriver.ChromeOptions()
	options.add_argument("headless")
	driver = webdriver.Chrome('./data/chromedriver', options=options)
	for user in data["codechef_users"]:
		print(user['name'])
		name = user["name"]
		id = user["id"]
		# print(url+id)
		driver.get(url+id)
		res = driver.execute_script('return document.documentElement.outerHTML')
		# print(res)
		l = check(res)
		if(type(l[1]) == None or l[1] == ''):
			l[1] ='0'
		tmp = l[0]+l[1]+l[2]
		
		if (tmp != user["ls"]):
			# message = "at {} User {} Solved {}, He scored {} using Language {}".format(l[0], user["name"], l[1], l[2], l[3])
			notify(user['name'] + " | "+ l[0] + " | "+ l[1] + " | "+l[2])
			# speakUp(message)
			user["ls"] = tmp
			f2 = open("./data/user.json", "w+")
			f2.write(json.dumps(data))
			f2.close()
	driver.quit()
	f.close()
	return


if __name__ == '__main__':
	options = webdriver.ChromeOptions()
	options.add_argument("headless")
	driver = webdriver.Chrome("./data/chrome/driver", options=options)
	main()
	driver.quit()
# notify("Codecehf", "New Rating "+rating.string, "/home/alpeshjamgade/myworld/web-scrapping/chef-hat.png")

# set webdriver and get page data;

# if (last_submission != tmp):
# 	last_submission = tmp
# 	notify('Codechef ', username + "  " + DateTime + "  " + Problem + "  " + Result + "  " + Lang,  "/home/alpeshjamgade/myworld/web-scrapping/chef-hat.png")
# 	speakUp("new submission by " + 
# 		username + " for the problem code "+ Problem + ". He scored " + Result + 
# 		" using Language "+ Lang)

# stored_submission = DateTime + Problem +  Result + Lang 

# print(DateTime)
# print(Problem)
# print(Result)
# print(Lang)

