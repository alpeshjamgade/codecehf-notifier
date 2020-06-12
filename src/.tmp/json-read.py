import json

# users = {
# 	"Alpesh Jamgade": "alpeshjamgade",
# }
# out = open("usernames.json", 'w')
# json.dump(users, out, indent = 6)
# out.close()
def getData():
	f = open('usernames.json',)
	data = json.load(f)
	for e in data["users"]:
		print(e["name"], e["userID"])

	f.close()
	return
getData()
