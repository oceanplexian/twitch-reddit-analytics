# Reddit Analytics Project

The reddit-analytics script is an example of a tool that crawls the [reddit.com/r/twitch](https://www.reddit.com/r/twitch) subreddit, looks for keywords (Such as load, buffer, lag, offline, and freezing) counts the number of votes and comments, and if they exceed a certain threshold (more than 5 upvotes alone, or a combination of more than 10 upvotes & comments) groups them into a list which could be used to trigger an alert, or potentially send a slack notification. 

Example Usage:
```
[echaveza@8c8590c9f441 ~]$ python reddit.py
[512][124] - Currently seeing No Live Channels, Dashboard not working and many other anomalies.
[165][30] - Twitch chat isn't loading, cleared cache + cookies + browser data. Need help
[133][58] - Twitch chat down?
[102][66] - Twitch is still unwatchable in Australia, and it's impossible to get in proper contact with twitch support.
[101][16] - ""We are looking into issues causing video loading failures across the site." -Twitch Support
[84][55] - Streams without quality options buffering like mad
[44][55] - Twitch to Chromecast - Is this ever going to work again?
[38][9] - Unable to retrieve their stream key and go live.
[33][19] - Twitch will not let me log in, can't reset the password. I am still getting billed for my subscription
[27][8] - "We couldn't load this ad for you"
[26][19] - Sudden unbearable lag
[25][22] - "You have been blocked from accessing Twitch" - Haven't been able to watch streams since sunday
[24][7] - Twitch streams showing offline again in html5 player.
```

Some potential ideas for a related project:
  - Do more than parse a list of words - sentiment analysis?
  - Come up with a better scoring mechanism than the one above
  - Find a way to track or graph changes in sentiment, votes, or comments, and where they are trending
  - Deploy the script to an AWS environment, using Terraform and Lambda, or ECS, and have it run at certain intervals (e.g.  https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html)

### Installation

reddit-analytics has been tested with Python 2.7. This will work with the system python installed on Mac OS X, but it's usually better to install Python with Homebrew https://docs.brew.sh/Homebrew-and-Python, if you're using a Mac. You will also need to install the Praw library to talk to Reddit, e.g. ```pip install praw``` 

### Development

- First, create a fork so you can modify the code and commit changes (https://help.github.com/articles/fork-a-repo/)
- Feel free to use your editor of choice, however [Atom](https://atom.io/) is a great choice. 
- To set up an Atom environment follow this guide: https://hackernoon.com/setting-up-a-python-development-environment-in-atom-466d7f48e297
- If you have any questions, feel free to ping @echaveza in Slack
