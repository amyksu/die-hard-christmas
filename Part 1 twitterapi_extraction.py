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
api = TwitterAPI('HzFVEIJWUyWk344lqLe6nfhtp', 'Fp31XN6a0rR4eV5d6Nce8IADBYRqms62nFiqO4d7txh2jP2SHW', 
	'26332823-87G6TbYRE7KFSxf7oxXZ34k8U0vO0Fn4a01qJBhKU', 
	'P3eJbyyrqUs9xNKPYcYJDdb8gEJ2vTS59e7VbEGgi1tDE')

r = TwitterPager(api, 'search/tweets', {'q': 'Die Hard Christmas-filter:retweets', 'tweet_mode': 'extended'})

# Write to file
for item in r.get_iterator():
	row = item['full_text'] if 'full_text' in item else ''
	row = row.replace("\n", " ")
	print(row)
	file.writerow([row])
