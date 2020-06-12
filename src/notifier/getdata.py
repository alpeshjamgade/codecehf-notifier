import json
import os

with open('data/urls/txt', 'w') as f:
	x = input("enter: ")
	if (len(x)==0):
		break
	f.write(x)

f.close()