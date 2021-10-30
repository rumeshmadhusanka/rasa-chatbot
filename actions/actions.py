# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

import json
import random
from typing import Any, Text, Dict, List

from nltk.metrics.distance import jaccard_distance
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

songs_file = "../webscrape/si-songs-final.json"
songs = json.load(open(songs_file))


def build_index(instances):
    title_index = dict()
    body_index = dict()
    for ins in instances:
        doc_id = ins["id"]
        title_words = ins["title"].split()
        for pos in range(len(title_words)):
            if title_words[pos] in title_index:
                title_index[title_words[pos]].append((doc_id, pos))
            else:
                title_index[title_words[pos]] = [(doc_id, pos)]

        body_words = ins["body"].split()
        for pos in range(len(body_words)):
            if body_words[pos] in body_index:
                body_index[body_words[pos]].append((doc_id, pos))
            else:
                body_index[body_words[pos]] = [(doc_id, pos)]

    vocabulary = set(title_index.keys()).union(body_index.keys())

    return title_index, body_index, vocabulary


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


def suggest_song(mood):
    lst = []
    for ins in songs:
        sent = ins["sentiment"]
        if sent == mood:
            lst.append(ins["title"])
    return random.choice(lst)


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


class ActionSuggestHappySong(Action):
    def name(self) -> Text:
        return "action_suggest_happy_song"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Action: suggest song on happy mood")

        return []


class ActionSuggestSadSong(Action):
    def name(self) -> Text:
        return "action_suggest_sad_song"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Action: suggest song on sad mood")

        return []


if __name__ == '__main__':
    _, _, index = build_index(songs)
    print(index)
