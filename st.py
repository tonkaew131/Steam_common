import requests 
import json

token = "B0165406E707D5F439954C2CB1A9984B"
#https://steamcommunity.com/dev/apikey

def commonElements(arr): 
	result = set(arr[0]) 
	for currSet in arr[1:]: 
		result.intersection_update(currSet) 
	return list(result) 

owngame = []
Case = int(input("How many people you wanna check? \n"))
for people in range(Case):
    steamid = input()
    url = "http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key="+token+"&steamid="+steamid+"&format=json"
    r = requests.get(url = url) 
    data = r.json()
    templt = []
    for game in range(data["response"]["game_count"]):
        templt.append(data["response"]["games"][game]["appid"])
    owngame.append(templt)

commongame = commonElements(owngame)
commongamename = []
for g in range(len(commongame)):
    appid = str(commongame[g])
    url = "http://store.steampowered.com/api/appdetails/?key="+token+"&appids="+appid+"&format=json"
    r = requests.get(url = url) 
    data = r.json()
    if data[appid]["success"] == True:
        commongamename.append(data[appid]["data"]["name"])

print("Total game in common :" + str(len(commongamename)))
output=open('output.txt', 'w', encoding='utf-8')
for element in commongamename:
    output.write(element)
    output.write('\n')
output.close()