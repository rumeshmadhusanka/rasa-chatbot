# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

import json
from typing import Any, Text, Dict, List

from nltk.metrics.distance import jaccard_distance
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

songs_file = "../webscrape/si-songs-final.json"
word_file = "../webscrape/word-count.json"

songs = json.load(open(songs_file))
words = json.load(open(word_file))


def song_of_artist(artist):
    lst = []
    for ins in songs:
        for singer in ins["singers"]:
            if jaccard_distance(singer, artist) < 0.3:
                lst.append(ins["title"])
    return lst


def most_popular_song():
    popular_song = ""
    max_views = 0
    for ins in songs:
        for singer in ins["singers"]:
            if max_views < ins["streams"]:
                max_views = ins["streams"]
                popular_song = ins["title"]
    return popular_song, max_views


def most_popular_of_artist(artist):
    popular_song = ""
    max_views = 0
    for ins in songs:
        for singer in ins["singers"]:
            if jaccard_distance(singer, artist) < 0.3:
                if max_views < ins["streams"]:
                    max_views = ins["streams"]
                    popular_song = ins["title"]
    return popular_song, max_views


def match_lyrics(guess):
    pass
    # todo implement proximity query


def extract_artist(message):
    if "ගේ" in message:
        return message.split("ගේ")[0]
    if "ගෙ" in message:
        return message.split("ගෙ")[0]
    if "ගායනා" in message:
        return message.split("ගායනා")[0]
    if "කියපු" in message:
        return message.split("කියපු")[0]


class ActionMostPopularSong(Action):

    def name(self) -> Text:
        return "action_get_most_popular_song"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Action: this is the most popular song")

        return []


class ActionMostPopularSongOfArtist(Action):

    def name(self) -> Text:
        return "action_get_most_popular_song_of_artist"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        artist = next(tracker.get_latest_entity_values("artist"), None)
        print(artist)

        artist = extract_artist(tracker.latest_message)
        dispatcher.utter_message(text="Action: this is the most popular song of artist " + artist)

        return []


class ActionSongsOfSinger(Action):

    def name(self) -> Text:
        return "action_songs_of_artist"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        artist = extract_artist(tracker.latest_message)
        dispatcher.utter_message(text="Action: this is the songs of this singer " + artist)

        return []


class ActionMatchLyrics(Action):

    def name(self) -> Text:
        return "action_match_lyrics"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Action: match song lyrics")

        return []
