[![CI](https://github.com/rumeshmadhusanka/rasa-chatbot/actions/workflows/main.yml/badge.svg?branch=master)](https://github.com/rumeshmadhusanka/rasa-chatbot/actions/workflows/main.yml)
[![CodeQL](https://github.com/rumeshmadhusanka/rasa-chatbot/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/rumeshmadhusanka/rasa-chatbot/actions/workflows/codeql-analysis.yml)
# RASA Chatbot for Sinhala Song Lyrics
<p align="center">
  <img src="background.png" />
</p>

Deployment guide: [DEPLOY.md](DEPLOY.md)<br>
## Data
This chatbot is trained on Sinhala lyrics scraped from [lyricslk.com](https://lyricslk.com). First the URLs that contain song lyrics are gahtherd. Then the webpages are scraped using BeautifulSoup library. Finally data is cleaned. Sripts relatedd to web scraping and data cleanning are stored in [webscrape](webscrape) directory.<br>
Final data contains the following attributes: 
1. id
2. title 
3. body - lyrics of the song
4. singers (one or more)
5. streams (derived)
6. sentiment (derived)

## Intentions the Chatbot Trained 

## Training Pipeline

## Lyrics Search

## Discord integration

## Deploymnet 
