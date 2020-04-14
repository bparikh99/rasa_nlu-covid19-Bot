# This files contains your custom actions which can be used to run
# custom Python code.

# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from bs4 import BeautifulSoup
import requests
import pandas as pd
source=requests.get('https://www.mohfw.gov.in/')
dfs = pd.read_html(source.text)
df=dfs[0]
df=df.drop(columns=['S. No.'],axis=1)
        

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            x=df.loc[lambda df: df['Name of State / UT']=={user_state}]
            ans="Total Cases =="+x['Total Confirmed cases (Including 76 foreign Nationals)']
            dispatcher.utter_templates("utter_ans_state",tracker,text=ans)
            return []
