import re
import praw
import time
from dateutil.relativedelta import relativedelta


reddit = praw.Reddit(client_id='',
                     client_secret='',
                     user_agent='Twitch Support Notifier')

subreddit = reddit.subreddit("twitch")

# Some code to generate human readable timestamps for Example 2
time = time.time()
attrs = ['years', 'months', 'days', 'hours', 'minutes', 'seconds']
human_readable = lambda delta: ['%d %s' % (getattr(delta, attr), getattr(delta, attr) > 1 and attr or attr[:-1]) 
    for attr in attrs if getattr(delta, attr)]

# Keywords that trigger scoring
terms =  [ 'load', 'work', 'buffer', 'ingest', 'broken', 'connect', 'lag', 'offline', 'watch', 'buffer', 'blank', 
    'black', 'freezing', 'segments', 'website', 'quality', 'rip', 'sync', 'live', '500', 'stutter', 'down', 'play', 
    'rtmp' ]
terms_re = re.compile("|".join(terms))


# Example 1: loop to print the highest scored posts
for submission in subreddit.search("flair:'Tech Support'", limit=4000, sort='top'):
    title = submission.title.encode('utf-8')
    link  = submission.permalink
    num_comments = submission.num_comments
    upvotes = submission.ups
    combined_score = num_comments + upvotes
    delta = time - submission.created_utc


    if combined_score > 10 and upvotes > 5 and terms_re.search(title):
    # Example 2: print how long ago posts were made
    #    human_delta = human_readable(relativedelta(seconds=delta))
    #    print "The following was reported on reddit {} {} ago".format(human_delta[0], human_delta[1])

        print "[{}][{}] - {}".format(upvotes,num_comments, title)



