from bs4 import BeautifulSoup
import requests
import lxml
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient


urlEndPoint = "https://www.amazon.com/Newest-MSI-i5-10300H-i7-7920HQ-Ethernet/dp/B09MZ66PLC/ref=psdc_13896617011_t2_B098JFL5DK?th=1"


parametersHeader = {
    "Accept-Language": "fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding":"gzip, deflate",
    "Connection": "keep-alive",


}

willSend = False

theRequest = requests.get(url=urlEndPoint, headers=parametersHeader)
theRequest.raise_for_status()

mySoup = BeautifulSoup(theRequest.text, "lxml")
thePrice = mySoup.find('span', 'a-price-whole').next_element

if int(thePrice) < 600:
    willSend=True

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
        body=f"your product is under 600$, buy it now on Amazon !!!,there is the url -> {urlEndPoint}",
        from_='+16065590885',
        to='+33635719503'
    )
    print(message.status)

