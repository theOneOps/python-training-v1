import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
willSend = False

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

stock_API = "https://www.alphavantage.co/query?"
stockApiKey = 'D9QQGQSL82CVZNUK'
news_API = "https://newsapi.org/v2/everything?"
newsApiKey = 'f89d37c570594b59a291982ebef3d4b0'
title = ''

stock_params = {
    'function': 'TIME_SERIES_DAILY',
    'apikey': stockApiKey,
    'symbol': STOCK,
}

getStock = requests.get(url=stock_API, params=stock_params)
getStock.raise_for_status()
stockData = getStock.json()

dates_stock = list(stockData['Time Series (Daily)'])
first_dateStock = float(stockData['Time Series (Daily)'][f"{dates_stock[0]}"]['4. close'])
scd_dateStock = float(stockData['Time Series (Daily)'][f"{dates_stock[1]}"]['4. close'])
percent = round(scd_dateStock / first_dateStock, 2)

if percent > 0:
    title = f"🔺{percent}%"
else:
    title = f"🔻{percent}%"

willSend = True

news_params = {
    'q': COMPANY_NAME,
    'apiKey': newsApiKey,
    'from': stockData['Time Series (Daily)'][f"{dates_stock[0]}"],
    'to': stockData['Time Series (Daily)'][f"{dates_stock[1]}"],
    'sortBy': 'relevancy',
    'language': 'en',
}

getNews = requests.get(url=news_API, params=news_params)
getNews.raise_for_status()
newsData = getNews.json()
threeArticles = newsData["articles"][:3]
threeList = []

word = ''

for i in range(3):
    w = threeArticles[i]["title"] + '\n' + threeArticles[i]["description"] + '\n' + threeArticles[i]["url"]
    threeList.append(w)

theText = title + "\n" + "\n".join(threeList)

if willSend:
    # Find your Account SID and Auth Token at twilio.com/console
    # and set the environment variables. See http://twil.io/secure
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    account_sid = "ACbb17af5807818a3bbc5a71d0b92445ff"
    auth_token = "a71ef286037a5d64fa2c4210b5c7fd79"

    client = Client(account_sid, auth_token, http_client=proxy_client)

    message = client.messages \
        .create(
        body=theText,
        from_='+16065590885',
        to='+33635719503'
    )
    print(message.status)
