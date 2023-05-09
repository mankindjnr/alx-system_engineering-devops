#!/usr/bin/python3
"""
Write a function that queries the Reddit API and returns the
number of subscribers (not active users, total subscribers)
for a given subreddit. If an invalid subreddit is given, the
function should return 0.
"""

import requests


def top_ten(subreddit):
    """ Set the API endpoint and headers"""
    endpoint = "https://api.reddit.com/r/{}/hot/".format(subreddit)
    headers = {'User-agent': 'Mozilla/5.0'}

    # Query the API and handle errors
    response = requests.get(endpoint, headers=headers)
    if response.status_code != 200:
        print("None")
        return

    posts = response.json()['data']['children']
    for i in range(10):
        title = posts[i]['data']['title']
        print(title)
