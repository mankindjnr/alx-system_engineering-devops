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
    baseurl = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'myBot/0.0.1'}
    try:
        response = requests.get(baseurl, headers=headers, allow_redirects=False)
        data = response.json()
        return data['data']['subscribers']
    except:
        return 0
