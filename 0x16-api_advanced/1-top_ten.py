#!/usr/bin/python3
""" Script to print hot posts on a given Reddit subreddit. """

import requests


def top_ten(subreddit):
    """ Print the titles of the 10 hottest posts on a given subreddit """

    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    params = {"limit": 10}
    resp = request.get(
            url, headers=headers, params=params, allow_redirect=False
            )

    if resp.status_code == 404:
        print("None")
        return

    results = resp.json().get("data")
    [print(c.get("data").get("title")) for c in results.get("children")]
