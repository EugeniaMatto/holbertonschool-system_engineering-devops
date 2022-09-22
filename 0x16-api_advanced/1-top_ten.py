#!/usr/bin/python3
"""" task 1 """

import json
import requests


def top_ten(subreddit):
    """ top ten """

    i = 0
    url = 'https://www.reddit.com/r/%7B%7D/hot.json'.format(subreddit)
    headers = {'User-Agent': 'ExternalAPI'}

    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code == 200:
        for k in res.json()['data']['children']:
            if i < 10:
                print(k['data']['title'])
            i += 1
    else:
        print(None)
