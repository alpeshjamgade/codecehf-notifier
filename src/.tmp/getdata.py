import bs4
import requests
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import notify2
import pyttsx3

url = "https://codechef.com/users/alpeshjamgade"
def pt(text):
	print(type(text))

def parse(url):
	op = Options()
	op.headless = True
	res = webdriver.Firefox(executable_path=r"/home/alpeshjamgade/myworld/web-scrapping/geckodriver", options=op)
	res.get(url)
	html = res.page_source
	return html



html = parse(url)
soup = bs4.BeautifulSoup(html, 'lxml')
# row = soup.find("table", {"class": "dataTable"}) --- not working beacuase its a dynamic tag constanly updated by js;
row = soup.find('table', {'class': 'dataTable'}).tbody.tr

i = 0
for d in row:
	if (i == 2):
		print(d.span['title'])
	else:
		print(d.string)
	i += 1
