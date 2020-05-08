#!/usr/bin/python3
"""Queries the Reddit API and returns the number of subscribers."""
from requests import get


def number_of_subscribers(subreddit):
    """Return the amount of subscribers."""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    Agents = {'User-Agent': 'Agent-Subscribe'}
    Response = get(url, headers=Agents, allow_redirects=False)
    if (Response.status_code != 200):
        return 0
    else:
        return Response.json()['data']['subscribers']
