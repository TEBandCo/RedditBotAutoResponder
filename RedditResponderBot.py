#adapted from busterttoni11 and bboe's videos. 

#changes made by /u/TheEpicBlob. 

import praw
import time


comment_to_search = [''] #list of keywords to search, comma separated 
subreddit_to_search = [''] #list of subreddits to search and comment on,comma separated
comment_to_reply_with = "" #comment to reply with, use triple quotes for multiline


def authenticate():
    print("Authenticating..."),
    reddit = praw.Reddit('SPECIFY_USER_CREDS_HERE', #see praw.ini file
        user_agent="SPECIFY USER AGENT HERE") #provide description of bot
    print("Authenticated as {}".format(reddit.user.me()))
    return reddit



def main():
    reddit = authenticate()
    while True:
        run_bot(reddit)


def run_bot(reddit):
    print("Getting comments...")
    for sub in subreddit_to_search:
        for comment in reddit.subreddit(sub).stream.comments(skip_existing=True):
            for keyword in comment_to_search:
                if keyword in comment.body and comment.author.name !=reddit.user.me(): 
                    print("String found in " + comment.id)
                    comment.reply(comment_to_reply_with)
                    print("Replied to " + comment.id)
                    print("Waiting for 10 seconds")
                    time.sleep(10)


if __name__ == '__main__':
    main()
