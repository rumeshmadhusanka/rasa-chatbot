#!/usr/bin/bash
echo "Starting a trained rasa discord bot"
rasa run &
rasa run actions &
cd discord-bot
python3 bot.py
