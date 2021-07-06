import os
import json
import praw
import requests
import pandas as pd

reddit = None

with open('client.json', 'r') as f:
    data = json.load(f)
    reddit = praw.Reddit(client_id=data['client_id'], client_secret=data['client_secret'], user_agent='reddit-bot')

def write_posts():
    df = pd.DataFrame(columns=['id', 'categories'])
    df['id'] = []
    df['categories'] = []
    i = 0

    for sub in reddit.subreddits.popular(limit=100):
        subname = sub.display_name
        if subname == 'Home':
            continue
        os.mkdir(subname)
        for submission in reddit.subreddit(sub.display_name).hot(limit=200):
            url = submission.url
            if '.jpg' in url[-4:] or '.png' in url[-4:]:
                r = requests.get(url, stream=True)
                if r.status_code == 200:
                    print('{}: Fetched {}'.format(subname, url))
                    with open(subname + '/' + str(i) + '.jpg', 'wb') as f:
                        for chunk in r:
                            f.write(chunk)
                
                    df = df.append({'id': int(i), 'categories': subname}, ignore_index=True)
                    i += 1
    df.to_csv('categories.csv', index=False)

write_posts()