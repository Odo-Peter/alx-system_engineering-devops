#!/usr/bin/python3
"""
queries the Reddit API and returns the number of
subscribers for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    try:
        url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
        req = requests.get(
            url, allow_redirects=False, headers={
                'User-Agent': 'wg1987'})
        req_json = req.json()
        data = req_json.get('data')
        number = data.get('subscribers')
        return (number)

    except BaseException:
        return(0)
