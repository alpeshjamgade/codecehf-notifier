import requests
from bs4 import BeautifulSoup as bs
import lxml
import json




url = 'https://codechef.com/contests'
res = requests.get(url)
soup = bs(res.text, 'lxml')

all_contests = soup.find_all('table', {'class':'dataTable'})

present_contests = None
future_contests = None

cnt = 0
for contest in all_contests:
	if (cnt == 0):
		present_contests = contest.tbody
	elif (cnt == 1):
		future_contests = contest.tbody
	else:
		break
	cnt += 1

# print(present_contests)
# print(future_contests)
# contests = {
# 	"present_contests": {

# 	},
# 	"future_contests":{

# 	},
# }


contest_code = ""
contest_name = ""
start_time = ""
end_time = ""


for contest in future_contests:
	for data in contest:
		print(data.tr)
