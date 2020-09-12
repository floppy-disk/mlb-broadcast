#!/usr/local/bin/python3
  
import json
import requests
import datetime
import subprocess


today = datetime.datetime.now()
startDate = today.strftime("%Y""%m""%d")
endDate = today.strftime("%Y""%m""%d")
curYear = today.strftime("%Y")

url = "http://lookup-service-prod.mlb.com/json/named.mlb_broadcast_info.bam?src_type='TV'&tcid=mm_mlb_schedule&sort_by='game_time_et_asc'&start_date='{}'&end_date='{}'&season='{}'".format(startDate, endDate, curYear)
x = requests.get(url)
json_doc = x.text
python_obj = json.loads(json_doc)

rowlist = python_obj['mlb_broadcast_info']['queryResults']['row']

tv=[]
newtv=[]
#remove out of market
for clump in rowlist:
    for k,v in clump.items():
        if (k == 'away_team_abbrev' and v == 'WSH'):
            network=clump['source_desc']
            tv.append(network)
            homeOrAway='away'
        elif (k == 'home_team_abbrev' and v == 'WSH'):
            network=clump['source_desc']
            tv.append(network)
            homeOrAway='home'
    for a in tv:
        if 'out-of-market' not in a:
            newtv.append(a)

for q in newtv:
    if 'MASN 2' in q:
        subprocess.call(["vlc", "--fullscreen", "[[[streamlink]]]"])
    elif 'MASN' in q:
        subprocess.call(["vlc", "--fullscreen", "[[[streamlink]]]"])
    elif 'ESPN' in q:
        subprocess.call(["vlc", "--fullscreen", "[[[streamlink]]]"])
