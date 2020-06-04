# This files contains your custom actions which can be used to run
# custom Python code.

# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
import requests
import pandas as pd
import json
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
            print(slot_state)
            slot_state=slot_state.capitalize()
            slot_district=str(tracker.get_slot("user_district"))
            slot_district=slot_district.capitalize()
            print(slot_district)
            global lst
            source=requests.get('https://api.covid19india.org/v2/state_district_wise.json').json()

            for i in range(len(source)):
                if(source[i]['state']==slot_state):
                    lst=source[i]['districtData']
                    for j in range(len(lst)):
                        if(lst[j]['district']==slot_district):
                            confirmed=lst[j]['confirmed']
                            deceased=lst[j]['deceased']
                            recovered=lst[j]['recovered']
            dispatcher.utter_message(f"Information for state {slot_state} and in  distric {slot_district} confirmed cases is around {confirmed} death is{deceased} ,and recovered cases is around {recovered}")
            return []
        
class ActionState(Action):
    def name(self) -> Text:
        return "action_total_cases_in_state"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            slot_iso_state=str(tracker.get_slot("iso_state"))
            print(slot_iso_state)
            url = "https://covid19india.p.rapidapi.com/getStateData"+'/'+slot_iso_state

            headers = {
                'x-rapidapi-host': "covid19india.p.rapidapi.com",
                'x-rapidapi-key': "216dd782cdmsh7f86900ecb6882dp14269fjsndf6ecc7de5a9"
                }

            r = requests.request("GET", url, headers=headers).json()
            r=json.dumps(r)

            x= r[130:134]
            y=r[151:154]
            z=r[168:171]
            dispatcher.utter_message(f"In your {slot_iso_state} confirmed cases is around {x},Total recoverd {y},and total deaths {z}")
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
        
class NameAction(Action):
    def name(self) -> Text:
        return "action_your_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            slot_name=str(tracker.get_slot("NAME"))
            prediction = tracker.latest_message
            #print(prediction)
            #name=prediction['entities'][0]['value']
            #print(name)
            name_entity=next(tracker.get_latest_entity_values("NAME"), "Someone")
            dispatcher.utter_message(f"Hey {name_entity}  Do you want more about Corna Virus in Your Place!!example:--im leaving in statename and my district is !")
            return []
      
class ActionStatefull(Action):
    def name(self) -> Text:
        return "action_cases_in_state"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            slot_full_state=str(tracker.get_slot("user_state"))
            slot_full_state=slot_full_state.capitalize()
            dfs=pd.read_html("https://www.mohfw.gov.in/")
            df=dfs[0]
            x=df.loc[lambda df : df['Name of State / UT']==slot_full_state]
            for i in x.values:
                print(i[2])
                confirmed= i[2]
                recoverd=i[3]
                deaths=i[4]
            dispatcher.utter_message(f"In your {slot_full_state} confirmed cases is around {confirmed},Total recoverd {recoverd},and total deaths {deaths}")
            return []
class ActionHelpline(Action):
    def name(self) -> Text:
        return "action_helpline"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            slot_full_state=str(tracker.get_slot("user_state"))
            slot_full_state=slot_full_state.capitalize()
            dfs=pd.read_html("https://www.indiatvnews.com/coronavirus/helpline-numbers")
            df=dfs[0]
            df=df['State Helpline Numbers']
            x=df.loc[lambda df: df['State/UT']==slot_full_state]
            for i in x.values:
                ans=i[1]
            dispatcher.utter_message(f" {slot_full_state} Helpline Number is {ans}")
            return []
        