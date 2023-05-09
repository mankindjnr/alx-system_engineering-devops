#!/usr/bin/python3
"""
Write a function that queries the Reddit API and returns the
number of subscribers (not active users, total subscribers)
for a given subreddit. If an invalid subreddit is given, the
function should return 0.
"""

import requests


def number_of_subscribers(subreddit):
    """
    eturns the number of subscribers (not active users, total subscribers)
    for a given subreddit. If an invalid subreddit is given, the
    function should return 0.
    """
    baseurl = "https://api.reddit.com/r/{}/about/".format(subreddit)
    headers = {'User-Agent': 'myBot/0.0.1'}

    resp = requests.get(baseurl, headers=headers, allow_redirects=False)
    data = resp.json()
    if resp.status_code == 200:
        return data['data']['subscribers']
    else:
        return 0
