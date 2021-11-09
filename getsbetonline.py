import json
import requests

## get token ##
def get_token():
  request = requests.get('https://api.play-gaming.com/authentication/v1/api/GetTokenBySiteId/158').text
  request = request.replace("ApiAccessToken = '", "Bearer ")
  request = request.replace("'", "")
  return request

## get league ids ##
path_leagues = '/getsbet/sportscontent/sportsbook/v1/Leagues/GetBySportId'
path_games = '/getsbet/sportscontent/sportsbook/v1/Events/GetByLeagueId'
path_markets = '/getsbet/sportscontent/sportsbook/v1/Events/GetByEventId'
headers = {
    'authority': 'sbapi.sbtech.com',
    'method': 'POST',
    'path': '',
    'scheme': 'https',
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'authorization': get_token(),
    'block-id': 'Center_TopLeaguesResponsiveBlock_32444',
    'content-length': '249',
    'content-type': 'application/json-patch+json',
    'locale': 'ro',
    'origin': 'https://online.getsbet.ro',
    'referer': 'https://online.getsbet.ro/',
    'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
    'sec-ch-ua-mobile': '?0',
    'sec-fetch-dest': '',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
    
}
headers['path']=path_leagues
payload_leagues = {"ids":["1"],"regionIds":["185"]}
response = requests.post("https://sbapi.sbtech.com/getsbet/sportscontent/sportsbook/v1/Leagues/GetBySportId", data=json.dumps(payload_leagues), headers=headers)
# print(response.status_code, response.reason)
json_data1 = json.loads(response.text)


leagues_list = []
leagues = json_data1.get('leagues')
for x in leagues:
  league_id = x.get('id')
  leagues_list.append(league_id)



## get games ids ##
games_id_list = []

for x in leagues_list:
  headers['path']=path_games
  payload_games = {"eventState":"Mixed","eventTypes":["Fixture","AggregateFixture"],"ids":[x],"regionIds":["185"]}
  r2 = requests.post("https://sbapi.sbtech.com/getsbet/sportscontent/sportsbook/v1/Events/GetByLeagueId", data=json.dumps(payload_games), headers=headers)
  json_data2 = json.loads(r2.text)
  
  events = json_data2.get('events')
  for x in events:
    id = x.get('id')
    games_id_list.append(id)


## get game markets ##

outcome_list = []
odds_list = []

for x in games_id_list:
  headers['path']=path_games
  payload_markets = {"ids":[x],"marketIds":["1_58224924", "3_58253871"]}
  r3 = requests.post("https://sbapi.sbtech.com/getsbet/sportscontent/sportsbook/v1/Events/GetByEventId", data=json.dumps(payload_markets), headers=headers)

  json_data3 = json.loads(r3.text)
  
  game = json_data3.get('events')[0].get('eventName')
  
  markets = json_data3.get('markets')

  
  for x in markets:
    name = x.get('name')
    if name == 'Peste/Sub':
      selections = x.get('selections')
      for x in selections:
        market_name = x.get('points')
        if market_name == 2.5:
          outcome = x.get('outcomeType')
          outcome_list.append(outcome)
          odds = x.get('displayOdds').get('decimal')
          odds_list.append(odds)

    if name == '1x2':
      selections = x.get('selections')
      for x in selections:
        outcome = x.get('outcomeType')
        outcome_list.append(outcome)
        odds = x.get('displayOdds').get('decimal')
        odds_list.append(odds)


  

  dictt = dict(zip(outcome_list, odds_list))
  dictt['name'] = game
  nm = dictt['name']
  home = dictt['Home']
  tie = dictt['Tie']
  away = dictt['Away']
  over = dictt['Over']
  under = dictt['Under']
  
  gm = nm + ' ' + home + ' ' + tie + ' ' + away + ' ' + over + ' ' + under
  print(gm)
