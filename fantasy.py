import requests
from bs4 import BeautifulSoup

page = requests.get("http://www.espn.com/fantasy/football/story/_/page/" +
                    "18RanksPreseason300PPR/2018-fantasy-football-ppr-rankings-top-300")
soup = BeautifulSoup(page.content, 'html.parser')
players = soup.find_all('tr', class_='last')

playersList = []
for player in players:
    text = list(player.children)[0].get_text()
    if ". " in text:
        playersList.append(text.split(". ")[1])

resultFyle = open("output.csv", 'w')

# Write data to file
for r in playersList:
    resultFyle.write(r + "\n")
resultFyle.close()
