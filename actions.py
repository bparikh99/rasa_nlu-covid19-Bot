# This files contains your custom actions which can be used to run
# custom Python code.

# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from app import cases   
from app import statewise
from graph import graphics
from app import statewise_full
import app
from SendEmail import sendingemailuser
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet,UserUtteranceReverted


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_total_cases"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            slot_state=str(tracker.get_slot("user_state"))
            slot_state=slot_state.capitalize()
            slot_district=str(tracker.get_slot('user_district'))
            slot_district=slot_district.capitalize()
            temp=cases(slot_state,slot_district)
            dispatcher.utter_message(f"Total cases in your {slot_state} and in  distric {slot_district} is around {temp}")
            return []
        
class ActionState(Action):
    def name(self) -> Text:
        return "action_total_cases_in_state"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            slot_iso_state=str(tracker.get_slot("iso_state"))
            print(slot_iso_state)
            temp=statewise(slot_iso_state)
            dispatcher.utter_message(f"In your {slot_iso_state} confirmed cases is around {temp[0]},Total recoverd {temp[1]},and total deaths {temp[2]}")
            return []
    
class EmailSend(Action):
    def name(self) -> Text:
        return "action_email_sent"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            slot_email=str(tracker.get_slot("email_id"))
            #slot_state=str(tracker.get_slot("user_state"))
            temp=sendingemailuser(slot_email)
            dispatcher.utter_message(f"Email Has Been Sent to {slot_email} read Further Details")
            return []
        
class GaphicsAction(Action):
    def name(self) -> Text:
        return "action_graphics_1"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            #slot_email=str(tracker.get_slot("email_id"))
            temp=graphics()
            link="https://imgur.com/vw0H4dr"
            dispatcher.utter_message(f"Graphs is according to your action {link} {temp}")
            return []
        
class NameAction(Action):
    def name(self) -> Text:
        return "action_your_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            slot_name=str(tracker.get_slot("NAME"))
            prediction = tracker.latest_message
            print(prediction)
            name=prediction['entities'][0]['value']
            print(name)
            name_entity=next(tracker.get_latest_entity_values("NAME"), None)
            dispatcher.utter_message(f"Hey {name}  Do you want more about Corna Virus in Your Place!!example:--im leaving in statename and my district is !")
            return []
      
class ActionStatefull(Action):
    def name(self) -> Text:
        return "action_cases_in_state"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            slot_full_state=str(tracker.get_slot("user_state"))
            slot_full_state=slot_full_state.capitalize()
            temp=statewise_full(slot_full_state)
            dispatcher.utter_message(f"In your {slot_full_state} confirmed cases is around {temp[0]},Total recoverd {temp[1]},and total deaths {temp[2]}")
            return []