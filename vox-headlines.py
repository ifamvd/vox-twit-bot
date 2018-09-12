"""
Author: Ismail Adiputra
Date  : Sep. 12, 2018

This is a script to collect top stories headlines from the vox website, which then will be
tweeted through a tweet bot.
"""

import requests
import os
from bs4 import BeautifulSoup as bs

# vox homepage url
url = 'https://www.vox.com'
# download the vox homepage
page = requests.get(url)
soup = bs(page.text, 'html.parser')
# find the top stories headlines
stories = soup.find("div", class_="c-newspaper__main")
print(stories)