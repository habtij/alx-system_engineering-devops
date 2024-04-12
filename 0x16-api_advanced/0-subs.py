#!/usr/bin/python3
"""It queries the ``Reddit API`` and returns the number of subscriber"""

import requests


def number_of_subscribers(subreddit):
    """Returns total number of subscribers on a given subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "firefox:0x16-api_advanced-newthing"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0

    data = response.json()['data']
    pages = data['children']
    page_data = pages[0]['data']
    return page_data['subreddit_subscribers']
