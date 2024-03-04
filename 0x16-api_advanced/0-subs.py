#!/usr/bin/python3
"""It queries the ``Reddit API`` and returns the number of subscriber"""

import requests


def number_of_subscribers(subreddit):
    """Returns total number of subscribers on a given subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    resp = requests.get(url, headers=headers, allow_redirects=False)
    if resp.statusCode == 200:
        data = resp.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
