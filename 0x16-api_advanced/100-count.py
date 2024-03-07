#!/usr/bin/python3
"""this one counts """
from collections import Counter
import requests



def count_words(subreddit, word_list, counts=None):
    """this one is a recurse that counts"""
    if counts is None:
        counts = Counter()

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {"User-Agent": "My-User-Agent"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code >= 300:
        return

    titles = [
        post['data']['title'] for post in response.json().get(
            'data', {}).get(
                'children', [])]

    for title in titles:
        for word in word_list:
            if word.lower() in title.lower().split():
                counts[word.lower()] += 1

    after_cursor = response.json().get('data', {}).get('after')
    if after_cursor:

        count_words(subreddit, word_list, counts=counts)

    for word, count in sorted(counts.items(), key=lambda x: (-x[1], x[0])):
        print(f"{word}: {count}")
