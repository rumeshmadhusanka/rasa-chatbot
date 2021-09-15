import requests
from bs4 import BeautifulSoup
import string

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}


def gen_urls():
    urls = []
    for letter in string.ascii_lowercase:
        for i in range(1, 20):
            URL = "https://lyricslk.com/search.php?q=" + letter + "&by=sortByLetter&page=" + str(i)
            urls.append(URL)
    return urls


def scrape_urls(url):
    urls = []
    page = requests.get(url, allow_redirects=True, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")
    songs = soup.find_all("div", {"class": "ResTitleSin"})
    for tag in songs:
        x = tag.find("a")['href']
        urls.append(x)
    return urls


p = gen_urls()
out = []
for u in p:
    try:
        res = scrape_urls(u)
        print(u)
        out.extend(res)
    except:
        pass

txt = open("urls.txt", "w")
for i in out:
    txt.write(i + "\n")
txt.close()
