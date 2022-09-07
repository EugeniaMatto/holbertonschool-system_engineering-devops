#!/usr/bin/python3
"""task 0 :D"""


import json
import requests

if __name__ == "__main__":
    i = 1
    final = {}
    while (i <= 10):
        tot = 0
        utask = 0
        user_url = "https://jsonplaceholder.typicode.com/users/{}".format(i)
        api_url = "https://jsonplaceholder.typicode.com/todos/"
        api_url = api_url + "?userId={}".format(i)
        res = requests.get(api_url).json()
        name = requests.get(user_url).json().get("username")
        lista = []
        for t in res:
            dic = {}
            dic["task"] = t.get("title")
            dic["completed"] = t.get("completed")
            dic["username"] = name
            lista.append(dic)
        final["{}".format(i)] = lista
        i += 1

    with open("todo_all_employees.json", 'w') as fileJson:
        fileJson.write(json.dumps(final))
    fileJson.close()
