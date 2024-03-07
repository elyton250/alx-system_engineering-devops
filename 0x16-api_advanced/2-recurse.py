#!/usr/bin/pyhton3
"""This is the module that uses recurse"""
import requests

def recurse(subreddit, hot_list=None):
    """this uses recurse"""
 
    if hot_list is None:
        hot_list = []

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {"User-Agent": "My-User-Agent"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code >= 300:
        return None

    for post in response.json().get('data', {}).get('children', []):
        hot_list.append(post['data']['title'])

    after_cursor = response.json().get('data', {}).get('after')
    if after_cursor:
        recurse(subreddit, hot_list=hot_list)

    return hot_list
