import numpy as np
import pandas as pd
import praw
from config import *

reddit = praw.Reddit(client_id=PRAW_ID,client_secret=PRAW_SECRET,username=PRAW_USERNAME,password=PRAW_PASSWORD,user_agent=PRAW_USER_AGENT)

subreddit = reddit.subreddit('wallstreetbets')

hot_wsb = subreddit.hot(limit=5)

for submission in hot_wsb:
    # if not submission.stickied:
    print(submission.title)