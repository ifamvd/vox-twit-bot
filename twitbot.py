"""
Author: Ismail Adiputra
Date  : Sep. 14, 2018

This is a script to post the links from VOX headlines, which was created by vox-headlines.py,
to my personal Twitter account. For this, a developer account is needed, This is simply
for learning purposes.
"""

import tweepy as tp
import time
import os

# get all the info we want to post to twitter
url = []
with open('links.txt') as f:
    for line in f:
        url.append(line.strip())

# get Twitter API credentials
consumer_key = "KrwDhDlaoqi0VqC2WeRdPb5nW"
consumer_secret = "HWqMFIy9dW6VYOeDWSHeuENhNJ3iSBlgHLs2YVJLIW40cTAuqW"
access_token = "150673828-Vmw0DzcnWffIbtHKIrXVNYG468W8JPnSggfxe4Up"
access_secret = "ZyGikUcNRAHOUpGgdVPwgJFRw95HWDLUj3wi6Qa7d1y5v"

# login to Twitter
auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)

# post the links
for i in url:
    api.update_status("Via TweePy: " + i)
    time.sleep(5)
