# code to scrape Twitter API
import re
import os
import csv
import itertools
import collections
from TwitterAPI import TwitterAPI, TwitterPager


# File to write
file = csv.writer(open("die-hard-tweets-no-retweets.csv", "w+", encoding="utf-8"))

# Initialize Twitter API
api = TwitterAPI('*key*', '*secret key*', 
	'*access key*', 
	'*secret access key')

r = TwitterPager(api, 'search/tweets', {'q': 'Die Hard Christmas-filter:retweets', 'tweet_mode': 'extended'})

# Write to file
for item in r.get_iterator():
	row = item['full_text'] if 'full_text' in item else ''
	row = row.replace("\n", " ")
	print(row)
	file.writerow([row])
