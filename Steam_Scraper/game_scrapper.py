import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

user_agent = {'User-agent': 'Mozilla/5.0'}
with open('filename') as f:
    game_path = f.read()
path = '/' + game_path + 'user-reviews?page='
links = []
i = 1
#Had to jump pages with no comments, this was done manually
links.append('/' + game_path + '/user-reviews')
print(links)
while (i < 50):
    if (i == 18):
        i+=1
    if (i == 43):
        i+=1
    links.append('/' + game_path+ '/user-reviews?page=' + str(i))
    i +=1
root = 'https://www.metacritic.com'
website = f'{root}'
names = []
dates = []
ratings = []
reviews = []
#iterate through the pages using the root + path and do the job
for link in links:
    linktogo=root+link
    print(linktogo)
    result = requests.get(linktogo, headers = user_agent)
    content = result.text
    soup = BeautifulSoup(content, 'html.parser')
#Save the name, date, score and review
    for links in soup.find_all('div', class_='name'):
        name = links.get_text().strip()
        names.append(name)
    for links in soup.find_all('div', class_='date'):
        date = links.get_text()
        dates.append(date)
    for links in soup.find_all('div', {"class": lambda x: x and "metascore_w user medium" in x}):
        score = links.get_text()
        ratings.append(score)
    for links in soup.find_all('div', {"class": "review_body"}):
        if(links.find("span")):
            review = links.get_text()
            review = review.replace('\n',' ')
            review = review.replace('\r',' ')
            reviews.append(review)
    games_dict = {'Name': names, 'Date': dates, 'Rating': ratings, 'Review':  reviews}

# Print the lengths.
print(len(names), len(dates), len(ratings), len(reviews))

# Create data frame.
game = pd.DataFrame.from_dict(games_dict, orient='index')
games = game.transpose()
games.to_csv('ratings.csv', index=False, header=True)
reviews = pd.read_csv('ratings.csv', lineterminator='\n')
