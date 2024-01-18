import requests
import json
import pandas as pd
from config import headers

# получение даты с апи sofascore
response = requests.get('https://api.sofascore.com/api/v1/sport/football/events/live', headers=headers)


# функция получения даты, составление таблицы с результатами матчей на момент запроса
def get_live_results():
    tournament_names_list = []
    country_list = []
    sport_list = []
    home_team_list = []
    away_team_list = []
    home_score_list = []
    away_score_list = []
    period_list = []

    results = pd.DataFrame()

    response = requests.get('https://api.sofascore.com/api/v1/sport/football/events/live', headers=headers)

    for i_matches in range(len(response.json()['events'])):
        tournament_name = response.json()['events'][i_matches]['tournament']['name']
        country = response.json()['events'][i_matches]['tournament']['category']['name']
        sport = response.json()['events'][i_matches]['tournament']['category']['sport']['name']
        home_team = response.json()['events'][i_matches]['homeTeam']['name']
        away_team = response.json()['events'][i_matches]['awayTeam']['name']
        home_score = response.json()['events'][i_matches]['homeScore']['current']
        away_score = response.json()['events'][i_matches]['awayScore']['current']
        period = response.json()['events'][0]['status']['description']

        tournament_names_list.append(tournament_name)
        country_list.append(country)
        sport_list.append(sport)
        home_team_list.append(home_team)
        away_team_list.append(away_team)
        home_score_list.append(home_score)
        away_score_list.append(away_score)
        period_list.append(period)

    results['tournament_name'] = tournament_names_list
    results['country'] = country_list
    results['sport'] = sport_list
    results['home_team'] = home_team_list
    results['away_team'] = away_team_list
    results['home_score'] = home_score_list
    results['away_score'] = away_score_list
    results['period'] = period_list

    print(results)


get_live_results()
