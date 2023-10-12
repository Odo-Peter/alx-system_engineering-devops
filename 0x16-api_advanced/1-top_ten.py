#!/usr/bin/python3
"""
queries the Reddit API and returns the top 10
posts for a given subreddit
"""
import requests


def top_ten(subreddit):
    try:
        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
        req = requests.get(
            url, allow_redirects=False, headers={
                'User-Agent': 'Jennifer12345'},
            params={'limit': 10})

        children = req.json().get('data').get('children')
        for child in children:
            print(child.get('data').get('title'))
    except ConnectionError:
        print(None)
