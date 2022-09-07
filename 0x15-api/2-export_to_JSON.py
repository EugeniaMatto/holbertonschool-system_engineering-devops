#!/usr/bin/python3
"""task 0 :D"""


import json
import requests
import sys

if __name__ == "__main__":
    argv = sys.argv
    tot = 0
    utask = 0
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
    api_url = "https://jsonplaceholder.typicode.com/todos/"
    api_url = api_url + "?userId={}".format(argv[1])
    res = requests.get(api_url).json()
    name = requests.get(user_url).json().get("username")
    lista = []
    for t in res:
        dic = {}
        dic["task"] = t.get("task")
        dic["completed"] = t.get("completed")
        dic["username"] = name
        lista.append(dic)
    final = {}
    final["{}".format(argv[1])] = lista
    with open("{}.json".format(argv[1]), 'w') as fileJson:
        fileJson.write(json.dumps(final))
    fileJson.close()
