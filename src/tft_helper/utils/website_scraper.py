from bs4 import BeautifulSoup
import requests


# TODO: CUSTOMIZE SEARCH (RANK)
LOLCHESS = "https://lolchess.gg/meta/augments?patch=1320&revision=1&tier=master&sort=avg-rank"


def grab_augments_table(website):
    page = requests.get(website)
    soup = BeautifulSoup( page.content , 'html.parser') 
    augments_table = soup.find('table')
    table_data = augments_table.find_all('tr')[1:]

    return table_data


def convert_augments_data(table_data):
    augments_data = {}
    for augment in table_data:
        name = augment.find(class_ = "name").text.strip()
        avg_rank = augment.find(class_ = "avg-rank sorted").text.strip()
        first_pick = augment.find(class_ = "first-pick").text.strip()
        second_pick = augment.find(class_ = "second-pick").text.strip()
        third_pick = augment.find(class_ = "third-pick").text.strip()
        top_rate = augment.find(class_ = "toprate").text.strip()
        win_rate = augment.find(class_ = "winrate").text.strip()
        pick_rate = augment.find(class_ = "pickrate").text.strip()
        games = augment.find(class_ = "games").text.strip()
    
        name = name.replace('+', "Plus")
        augments_data[name] = (avg_rank, first_pick, second_pick, third_pick, top_rate, win_rate, pick_rate, games)

    return augments_data
