#!/usr/bin/python3
"""It queries the ``Reddit API`` and returns the number of subscriber"""

import requests


def number_of_subscribers(subreddit):
    """Returns total number of subscribers on a given subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 400:
        return 0

    results = response.json().get("data")
    return results.get("subscribers")
