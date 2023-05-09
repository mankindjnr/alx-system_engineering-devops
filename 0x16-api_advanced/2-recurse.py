#!/usr/bin/python3
"""
a recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit. If no
results are found for the given subreddit, the function should return None.
"""
import requests

def recurse(subreddit, hot_list=None, after=None):
    """ Base case: hot_list is empty or reached the end of the pagination"""
    if hot_list is None:
        hot_list = []
    if after == "STOP":
        return hot_list

    # Set the API baseurl and header

    baseurl = "https://api.reddit.com/r/{}/hot?after={}".format(subreddit, after)
    header = {'User-agent': 'Mozilla/5.0'}
    params = {'after': after} if after else None

    # Query the API and handle errors
    response = requests.get(baseurl, headers=header, params=params)
    if response.status_code != 200:
        return None

    # Extract the post titles and recursively call the
    # function with the next page's token
    posts = response.json()['data']['children']
    for post in posts:
        hot_list.append(post['data']['title'])
        after = response.json()['data']['after']
    return recurse(subreddit, hot_list, after)
