import requests
from bs4 import BeautifulSoup
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
urls = open("urls.txt").readlines()
urls = [i.strip() for i in urls]

out = []


def scrape_body(url):
    page = requests.get(url, allow_redirects=True, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")
    h2 = soup.find("h2")

    body = soup.find("div", {"id": "lyricsBody"})
    h2 = h2.text
    title = h2.split("-")[0].strip()
    singer = h2.split("-")[1].strip()
    body = body.text.strip().replace(".", "").replace("<br />", "\n").replace("//", " //")
    out.append({"title": title, "singer": singer, "body": body})


for u in urls:
    try:
        scrape_body(u)
    except:
        pass

json.dump(out, open("si-songs.json", "w"), ensure_ascii=False, indent=4)
