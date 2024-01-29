import praw
import pandas as pd
import datetime
import csv

#authorized codes, remove when uploading/sharing
reddit_read_only = praw.Reddit(client_id="#",		 # your client id
							client_secret="#",	 # your client secret
							user_agent="#")	


post = reddit_read_only.submission(url='https://www.reddit.com/r/Games/comments/175du38/blizzard_feels_hellish_heat_as_fans_complain/')

with open('comment_outputs/reddit_comments_post10.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    
    # Write header row
    csv_writer.writerow(['Author', 'Date', 'Likes', 'Comment'])

    # Set a comment limit
    comment_limit = 300
    comment_count = 0

    # Loop through the comments and write them to the CSV file
    for comment in post.comments.list():
        if comment_count >= comment_limit:
            break
        author = comment.author.name if comment.author else "Unknown"
        date = comment.created_utc
        likes = comment.ups
        comment_body = comment.body

        # Check for blank data before writing to the CSV
        if author and date and comment_body:
            csv_writer.writerow([author, date,likes, comment_body])
            comment_count += 1
