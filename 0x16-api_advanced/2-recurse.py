#!/usr/bin/python3
"""Queries RedditAPI and returns list containing titles of all HotArticles."""
import requests import get


def recurse(subreddit, hot_list=[], after=None):
    """Reddit API uses pagination for separating pages of responses."""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    Agents = {'User-Agent': 'Agent-Subscribe'}
    Response = get(url, headers=Agents,
                   allow_redirects=False, params={'after': after})
    if Response.status_code != 200:
        return None

    ChildTitles = Response.json()['data']['children']
    for HotArticles in ChildTitles:
        hot_list.append(HotArticles['data']['title'])
    AfterData = Response.json()['data']['after']
    if AfterData is None:
        return hot_list
    return recurse(subreddit, hot_list, AfterData)
