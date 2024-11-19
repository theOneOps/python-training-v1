from bs4 import BeautifulSoup

with open("./website.html", 'r') as file:
    content = file.read()


theSoup = BeautifulSoup(content, 'html.parser')



#Class ="c-title__link lrv-a-unstyle-link">




for j in theSongs[:2]:
    spot_params = {
        'q': j,
        'type': 'track',
        'Content-Type': 'application/json',
        'year': theAnswerList[0],
    }

    content = requests.get(f"https://api.spotify.com/v1/search?", params=spot_params)
    content.raise_for_status()
    print(content.json())