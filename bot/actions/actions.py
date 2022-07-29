###########
# IMPORTS #
###########
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from .secrets import secrets

# Requisição na API
import requests
from random import randint

################## 
# BANCO DE DADOS #
################## 
from pymongo import MongoClient

client = MongoClient(secrets["CLUSTER"])
db = client[secrets["DB_NAME"]]
collection = db[secrets["COL_NAME"]]

#############
# FUNCTIONS #
#############
def verify_house(house):
  if house in "grifinoriagrifinóriagriffy":
    return "gryffindor"
  elif house in "sonserina":
    return "slytherin"
  elif house in "lufa-lufalufa lufa":
    return "hufflepuff"
  elif house in "corvinal":
    return "ravenclaw"

###########
# ACTIONS #
###########
class ActionShowCharacter(Action):

    def name(self) -> Text:
        return "action_show_character"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            
        casa = tracker.get_slot("house_slot")
        house = verify_house(casa.lower())

        db = client[secrets["DB_HOUSES"]]
        collection = db[house]

        # Selecionando um personagem aleatório do BD
        random_cursor = collection.aggregate([ {"$sample": {"size": 1}}]) 
        character = list(random_cursor)[0]

        dispatcher.utter_message(image=character['image'])

        # Verificando gênero do personagem
        if character['gender'] in "male":
          dispatcher.utter_message(text=f"{character['name']} será seu acompanhante, ele vai te mostrar {casa.title()}.")
        else:
          dispatcher.utter_message(text=f"{character['name']} será sua acompanhante, ela vai te mostrar {casa.title()}.")

        return []

class ActionShowHistory(Action):

    def name(self) -> Text:
        return "action_show_history"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

          dispatcher.utter_message(text="- Histórico dos acompanhantes")

          # Acessando o histórico
          for data in collection.find():
            dispatcher.utter_message(text=f"{data['name']} de {data['house']}.")

          return []