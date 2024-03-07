#!/usr/bin/python3
"""this module rewuests from reddit api"""


def number_of_subscribers(subreddit):
    """this function obtains information from a subreddit"""
    import requests

    info = requests.get(
        f'https://www.reddit.com/r/{subreddit}/about.json', headers={
            "User-Agent": "My-User-Agent"}, allow_redirects=False)

    if info.status_code >= 300:
        return 0
    return info.json().get('data').get('subscribers')
