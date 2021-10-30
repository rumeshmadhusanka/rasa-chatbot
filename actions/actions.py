# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


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
        # artist = next(tracker.get_latest_entity_values("artist"), None)
        artist = tracker.latest_message["entities"]
        print(artist)
        # print(domain)
        # print(tracker.current_state())
        dispatcher.utter_message(text="Action: this is the most popular song of artist ")

        return []
