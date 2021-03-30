import requests, json
from random import randint
import webbrowser

def random_artist(genre):
    r = requests.get('https://api.deezer.com/genre/' + str(genre) +'/artists')
    jdata = r.json()
    jarr = jdata['data']

    try:
        rand = randint(0,len(jarr)-1)
        print(jarr[rand]['name'])
        print(jarr[rand]['tracklist'].split('?')[0])
        tracklist = jarr[rand]['tracklist'].split('?')[0]
        random_song(tracklist)
    except:
        print("Fehler")

def random_song(tracklist):
    r = requests.get(tracklist)
    print(r.json()['data'][0]['link'])
    link = r.json()['data'][0]['link']
    webbrowser.open(link, new=0, autoraise=True)

stream = input("Welchen Musicstream wollen sie nützen? Spotify/Deezer\n").lower()
if stream == 'spotify':
    print('spotify')
    
elif stream == 'deezer':

    r = requests.get('https://api.deezer.com/genre')
    jdata = r.json()
    jarr = jdata['data']
    for x in jarr:
        print(x['name'] + ": " + str(x['id']))

    genre = input("Welche Genre willst du?\n")
    random_artist(genre)

    skip = input("Skip/Stop\n").lower()
    if skip == 'skip':
        random_artist(genre)
    elif skip == 'stop':
        print("Service wird gestoppt")
    else:
        print("Fehler")

else:
    print('Stream wurde nicht gefunden')

