#!/usr/bin/python3
import json
import requests
import sys
if __name__ == "__main__":
	argv = sys.argv
	total = 0
	utask = 0
	user_url = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
	api_url = "https://jsonplaceholder.typicode.com/todos/"
	api_url = api_url + "?userId={}".format(argv[1])
	res = requests.get(api_url).json()
	r_user = requests.get(user_url).json().get("name")
	for task in res:
		total += 1
		if task.get("completed"):
			utask += 1
	print("Employee {} is done with tasks({}/{}):".format(r_user, utask, total))
	for task in res:
		if task.get("completed"):
			print("\t {}".format(task.get("title")))
