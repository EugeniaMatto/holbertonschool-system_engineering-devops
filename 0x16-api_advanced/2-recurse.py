#!/usr/bin/python3
"""task 1"""

import json
import requests


def recurse(subreddit, hot_list=[], after=None):
    """ recurse """

    headers = {'User-Agent': 'ExternalAPI'}
    params = {'after': after}

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if 200 == response.status_code:
        request = response.json().get('data').get('children')
        for i in request:
            hot_list.append(i.get('data').get('children'))
        after = response.json().get('data').get('after')
        if after is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, after)
    else:
        return None
