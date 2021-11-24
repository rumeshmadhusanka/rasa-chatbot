from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from actions.helper import get_logger, \
    suggest_song, songs_of_artist, get_most_popular_song, most_popular_of_artist, get_matched_lyrics

logger = get_logger("actions")


class ActionMostPopularSong(Action):

    def name(self) -> Text:
        return "action_get_most_popular_song"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        logger.debug("ActionMostPopularSong")
        resp = get_most_popular_song()
        dispatcher.utter_message(text=resp)

        return []


class ActionMostPopularSongOfArtist(Action):

    def name(self) -> Text:
        return "action_get_most_popular_song_of_artist"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        logger.debug("ActionMostPopularSongOfArtist")
        artist_obj = tracker.latest_message['entities'][0]
        artist = artist_obj['value']
        logger.debug(artist_obj)
        resp = most_popular_of_artist(artist)
        dispatcher.utter_message(text=resp)
        return []


class ActionSongsOfSinger(Action):

    def name(self) -> Text:
        return "action_songs_of_artist"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        logger.debug("ActionSongsOfSinger")
        artist_obj = tracker.latest_message['entities'][0]
        artist = artist_obj['value']
        logger.debug(artist_obj)
        resp = songs_of_artist(artist)
        dispatcher.utter_message(text=resp)

        return []


class ActionMatchLyrics(Action):
    def name(self) -> Text:
        return "action_match_lyrics"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        logger.debug("ActionMatchLyrics")
        song_obj = tracker.latest_message['entities'][0]
        song = song_obj['value']
        logger.debug(song_obj)
        resp = get_matched_lyrics(song)
        dispatcher.utter_message(text="Action: match song lyrics")

        return []


class ActionSuggestHappySong(Action):
    def name(self) -> Text:
        return "action_suggest_happy_song"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        string = suggest_song("positive")
        logger.debug("ActionSuggestHappySong")
        dispatcher.utter_message(text=string)

        return []


class ActionSuggestSadSong(Action):
    def name(self) -> Text:
        return "action_suggest_sad_song"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        string = suggest_song("negative")
        logger.debug("ActionSuggestSadSong")
        dispatcher.utter_message(text=string)

        return []
