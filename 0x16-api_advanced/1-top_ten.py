#!/usr/bin/python3
"""Queries the Reddit API and prints the titles of the first 10 hot posts."""
from requests import get


def top_ten(subreddit):
    """If not a valid subreddit, print None."""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    Agents = {'User-agent': 'Agent-Subscribe'}
    Response = get(url, headers=Agents, allow_redirects=False)
    if (Response.status_code != 200):
        print('None')
    else:
        ChildTitles = Response.json()['data']['children']
        for HotPosts in ChildTitles:
            print(HotPosts['data']['title'])
