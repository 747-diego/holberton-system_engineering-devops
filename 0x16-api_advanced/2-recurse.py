#!/usr/bin/python3
"""Queries RedditAPI and returns list containing titles of all HotArticles."""
import requests import get


def recurse(subreddit, hot_list=[], after=None):
    """Reddit API uses pagination for separating pages of responses."""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    user_agent = {'User-Agent': 'Agent-Subscribe'}
    Response = get(url, headers=user_agent, allow_redirects=False)
    if Response.status_code != 200:
        return None
    else:
        ChildTitles = Response.json()['data']['children']
        AfterData = Response.json()['data']['after']

        for HotArticles in ChildTitles:
            hot_list.append(HotArticles['data']['title'])
        if AfterData is None:
            return hot_list
        return recurse(subreddit, hot_list, AfterData)
