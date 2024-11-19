from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth


continue_prog = True
theQuestion = input("Which year do you want to travel to ? Type the date in this format YYYY-MM-DD ")
theAnswerList = theQuestion.split('-')


def isbissextile(year):
    if (year % 4 == 0 and year % 100 != 0) and year % 400 == 0:
        return True
    return False


def valid(dateData):
    try:
        annee, mois, jour = dateData[0], dateData[1], dateData[2]
    except:
        return False
    fevrier = "28" if isbissextile(int(annee)) else "29"
    calendar = {
        "01": "31",
        "02": fevrier,
        "03": "31",
        "04": "30",
        "05": "31",
        "06": "30",
        "07": "31",
        "08": "31",
        "09": "30",
        "10": "31",
        "11": "30",
        "12": "31",

    }
    month = int(mois) if '0' not in mois else int(list(mois)[1])
    day = int(jour) if '0' not in jour else int(list(jour)[1])
    print(f"month={month}, day={day}")

    if (0 < month < 12) and (0 < int(day) < int(calendar[mois])):
        return True
    return False


def verification(theValue):
    if theValue == '':
        return False
    return (1958 < int(theValue[0]) < 2022) and valid(theValue)

while continue_prog :
    while not(verification(theAnswerList)):
        theQuestion = input("Which year do you want to travel to ? Type the date in this format YYYY-MM-DD ")
        theAnswerList = theQuestion.split('-')
    continue_prog = False

theUrl = f"https://www.billboard.com/charts/hot-100/{theQuestion}/"
print(theUrl)
print(theAnswerList)

link = requests.get(theUrl)
content = link.text


mySoup = BeautifulSoup(content, 'html.parser')
allH = mySoup.find_all("h3", id="title-of-a-story")
theList = []
theNewList = []
for i in allH:
    theList.append(str(i.string).replace('\t', ''))

for i in theList:
    if ':' not in i:
        theNewList.append(i.replace('\n', ''))

theSongs = theNewList[2:102]

spotifyEndpoint ="https://api.spotify.com/v1/search?q={}&type=track"
client_ID = '16c390caeefe4d6994f7bebffc165f5a'
client_Secret = '0497bfc071b24c62805ee2c9edef15bc'

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=client_ID,
        client_secret=client_Secret,
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]
print(user_id)
the_id = '31q3mb2v4fm4dz6dxqwmzqq5nqce'

