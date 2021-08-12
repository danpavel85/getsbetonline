import json
import requests

## get league ids ##
headers1 = {
    'authority': 'sbapi.sbtech.com',
    'method': 'POST',
    'path': '/getsbet/sportscontent/sportsbook/v1/Leagues/GetBySportId',
    'scheme': 'https',
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJTaXRlSWQiOjE1OCwiU2Vzc2lvbklkIjoiNTlhYjFlYTktZmJkZC00MDY0LWEyNDUtMzQ4OTZlYzg4YmEzIiwibmJmIjoxNjI4NjYyMzUwLCJleHAiOjE2MjkyNjcxODAsImlhdCI6MTYyODY2MjM4MH0.x6DegWLZoczIHN7uEy7FV0VkPIrzjzxa4lRc3PK1HcE',
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
payload1 = {"ids":["1"],"regionIds":["185"]}
r1 = requests.post("https://sbapi.sbtech.com/getsbet/sportscontent/sportsbook/v1/Leagues/GetBySportId", data=json.dumps(payload1), headers=headers1)
# print(r1.status_code, r1.reason)
json_data1 = json.loads(r1.text)


leagues_list = []
leagues = json_data1.get('leagues')
for x in leagues:
  league_id = x.get('id')
  leagues_list.append(league_id)



## get games ids ##
games_id_list = []

headers2 = {
    'authority': 'sbapi.sbtech.com',
    'method': 'POST',
    'path': '/getsbet/sportscontent/sportsbook/v1/Events/GetByLeagueId',
    'scheme': 'https',
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJTaXRlSWQiOjE1OCwiU2Vzc2lvbklkIjoiNTlhYjFlYTktZmJkZC00MDY0LWEyNDUtMzQ4OTZlYzg4YmEzIiwibmJmIjoxNjI4NjYyMzUwLCJleHAiOjE2MjkyNjcxODAsImlhdCI6MTYyODY2MjM4MH0.x6DegWLZoczIHN7uEy7FV0VkPIrzjzxa4lRc3PK1HcE',
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

for x in leagues_list:
  payload2 = {"eventState":"Mixed","eventTypes":["Fixture","AggregateFixture"],"ids":[x],"regionIds":["185"]}
  r2 = requests.post("https://sbapi.sbtech.com/getsbet/sportscontent/sportsbook/v1/Events/GetByLeagueId", data=json.dumps(payload2), headers=headers2)
  json_data2 = json.loads(r2.text)
  
  events = json_data2.get('events')
  for x in events:
    id = x.get('id')
    games_id_list.append(id)


## get game markets ##

headers3 = {
    'authority': 'sbapi.sbtech.com',
    'method': 'POST',
    'path': '/getsbet/sportscontent/sportsbook/v1/Events/GetByEventId',
    'scheme': 'https',
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJTaXRlSWQiOjE1OCwiU2Vzc2lvbklkIjoiNTlhYjFlYTktZmJkZC00MDY0LWEyNDUtMzQ4OTZlYzg4YmEzIiwibmJmIjoxNjI4NjYyMzUwLCJleHAiOjE2MjkyNjcxODAsImlhdCI6MTYyODY2MjM4MH0.x6DegWLZoczIHN7uEy7FV0VkPIrzjzxa4lRc3PK1HcE',
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

outcome_list = []
odds_list = []

for x in games_id_list:
  payload3 = {"ids":[x],"marketIds":["1_58224924", "3_58253871"]}
  r3 = requests.post("https://sbapi.sbtech.com/getsbet/sportscontent/sportsbook/v1/Events/GetByEventId", data=json.dumps(payload3), headers=headers3)

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
