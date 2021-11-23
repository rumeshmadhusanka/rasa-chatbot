from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from actions.helper import extract_artist, get_logger, \
    suggest_song

logger = get_logger("actions")


class ActionMostPopularSong(Action):

    def name(self) -> Text:
        return "action_get_most_popular_song"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        logger.debug("ActionMostPopularSong")
        dispatcher.utter_message(text="Action: this is the most popular song")

        return []


class ActionMostPopularSongOfArtist(Action):

    def name(self) -> Text:
        return "action_get_most_popular_song_of_artist"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        artist_obj = tracker.latest_message['entities'][0]
        artist = artist_obj['value']
        logger.debug("ActionMostPopularSongOfArtist")
        logger.debug(str(artist_obj))
        dispatcher.utter_message(text="Action: this is the most popular song of artist " + artist)
        return []


class ActionSongsOfSinger(Action):

    def name(self) -> Text:
        return "action_songs_of_artist"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        artist = extract_artist(tracker.latest_message)
        logger.debug("ActionSongsOfSinger")
        dispatcher.utter_message(text="Action: this is the songs of this singer " + artist)

        return []


class ActionMatchLyrics(Action):
    def name(self) -> Text:
        return "action_match_lyrics"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        logger.debug("ActionMatchLyrics")
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
