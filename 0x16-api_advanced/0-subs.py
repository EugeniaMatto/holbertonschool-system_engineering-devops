#!/usr/bin/python3
""" task 0 """

import json
import requests


def number_of_subscribers(subreddit):
    """ number of subscribers ;) """

    """ headers """
    headers = {'User-Agent': 'ExternalAPI'}

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if 200 == response.status_code:
        return response.json()['data']['subscribers']
    return (0)
