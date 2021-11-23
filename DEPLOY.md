# Deployment Guide
## Install the dependecies
Deployemnt guide for Ubuntu 20.04 on a local machine or a cloud VM <br>
Clone the repository
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
pip3 install -r requirements.txt -r requirements-discord.txt
```
## Scrape Data (optional)
Data is already commited to the repo. If you wish to scrape data yourself you can follow the steps:<br>
Scrape URLs
```
python3 webscrape/scrape.py
```
Scrape the song infomation from the urls
```
python3 webscrape/song-info-scrape.py
```
Clean the data
```
python3 webscrape/divide-singers.py
```
Index the data
```
python3 webscrape/count-words.py
```
## Train the RASA chat bot
```
rasa train 
```
## Integrate with Discord
Create a discord application and obtain a token -- Follow this tutorial: [How to Get a Discord Bot Token](https://www.writebots.com/discord-bot-token/)<br>
Keep this token safe. Don't commit it to GitHub.<br>
Create a `.env` file and store your token
```
echo 'DISCORD_TOKEN=<your-discord-token>' > discord-bot/.env
```
If you don't want to integrate with Discord, replace you can skip the above step. Replace the `rasa run` commnad in the next step with `rasa shell` to interact with the chat bot in your terminal.
## Start the chatbot
Run the foloowing commands on seperate terminals:<br>
To start the chatbot
```
rasa run
```
To run the actions server
```
rasa run actions
```
To start the discord bot
```
python3 discord-bot/bot.py
```
## Run as a system service
If you want to restart the chat bot after restarting your machine or if you want to run the chat bot in background,

