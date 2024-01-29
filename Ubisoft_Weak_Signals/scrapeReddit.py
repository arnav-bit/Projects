import praw
import pandas as pd
import datetime

#authorized codes to be entered here. The codes are created on the Reddit Developer Website

reddit_read_only = praw.Reddit(client_id="#",		 # your client id
							client_secret="#",	 # your client secret
							user_agent="#")	 # your user agent

#name of subs here
name_file = "IndieGaming"

#reading the name
subreddit = reddit_read_only.subreddit(name_file)

#checking for top 500 posts in the sub
posts = subreddit.top(limit = 500)

#creating a blank DF
posts_dict = {"Title": [], "Post Text": [],
              "ID": [], "Score": [],
              "Total Comments": [], "Post URL": [], "Date" : [], "subredName" : []
              }
 
def get_date(submission):
	time = submission.created
	return datetime.datetime.fromtimestamp(time)

def filter_posts_by_year(posts, year):
    for post in posts:
        post_date = get_date(post)
        if post_date.year == year:
            posts_dict["Title"].append(post.title)
            posts_dict["Post Text"].append(post.selftext)
            posts_dict["ID"].append(post.id)
            posts_dict["Score"].append(post.score)
            posts_dict["Total Comments"].append(post.num_comments)
            posts_dict["Post URL"].append(post.url)
            posts_dict['Date'].append(post_date)
            posts_dict['subredName'].append(name_file)

year_to_scrape = 2023 #define which year to scrape data from

posts = subreddit.top(limit=500)
filter_posts_by_year(posts, year=year_to_scrape)

top_posts = pd.DataFrame(posts_dict)
      
top_posts.to_csv('conclusions/outputs/scraped_'+name_file+str(year_to_scrape)+'.csv', index=None)
print("File saved")
