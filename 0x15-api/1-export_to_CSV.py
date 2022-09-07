#!/usr/bin/python3
"""task 0 :D"""

import csv
import json
import requests
import sys

if __name__ == "__main__":
    argv = sys.argv
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
    api_url = "https://jsonplaceholder.typicode.com/todos/"
    api_url = api_url + "?userId={}".format(argv[1])
    res = requests.get(api_url).json()
    name = requests.get(user_url).json().get("username")
    with open('{}.csv'.format(argv[1]), 'w') as csvfile:
        wr = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in res:
            out = [argv[1], name, task.get("completed"), task.get("title")]
            wr.writerow(out)
    csvfile.close()
