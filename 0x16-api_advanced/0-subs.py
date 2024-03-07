#!/usr/bin/python3
"""this is the module that get subs"""
import requests


def number_of_subscribers(subreddit):

    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {"User-Agent": "My-User-Agent"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code >= 300:
        return 0
    return response.json().get('data', {}).get('subscribers', 0)
