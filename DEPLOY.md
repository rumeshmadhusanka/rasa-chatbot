# Deployment Guide
## Install dependecies
Clone this repository
```
git clone https://github.com/rumeshmadhusanka/rasa-chatbot.git
```
Create a python virtual environment
``` 
virtualenv env
```
Activate the created virtual environment
```
source env/bin/activate
```
Install the dependencies
```
pip3 install requirements.txt
```
## Scrape Data (optional)
Data is already commited to the repo. If you wish to scrape data yourself you can follow the steps:<br>
Scrape URLs
```
python3 webscrape/scrape.py
```
Scrape the song infomation from the urls
```
python3 song-info-scrape.py
```

Train the rasa chat bot
```
rasa train 
```
## Integrate with Discord
Create a discord application and obtain a token -- Follow this guide: [How to Get a Discord Bot Token](https://www.writebots.com/discord-bot-token/)<br>
Keep this token safe. Don't commit it to GitHub.
