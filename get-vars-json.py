import urllib, json
url = "https://api.spotify.com/v1/artists/5wbIWUzTPuTxTyG6ouQKqz/albums?limit=50"
response = urllib.urlopen(url)
data = json.loads(response.read())
print data

for i in data['items']:
	print i['id']