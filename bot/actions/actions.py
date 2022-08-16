###########
# IMPORTS #
###########
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from .secrets import secrets

################## 
# BANCO DE DADOS #
################## 
from pymongo import MongoClient

client = MongoClient(secrets["CLUSTER"])
db = client[secrets["DB_NAME"]]

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

        collection = db["history"]

        query = {"house": house}
        house_history = collection.find_one(query)

        # Descrição da casa
        dispatcher.utter_message(house_history["description"])

        # Atualizando o histórico do BD
        new_counter = house_history["counter"] + 1
        new_value = {"$set": {"counter": new_counter}}
        collection.update_one(query, new_value)

        return [
            SlotSet("house_slot", None)
        ]

class ActionShowHistory(Action):

    def name(self) -> Text:
        return "action_show_history"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
          
          collection = db["history"]

          historico_das_casas = "Qual você achou que seria a casa mais visitada?\n"

          # Acessando o histórico casa por casa
          for data in collection.find():
            historico_das_casas += f"- {data['house'].title()} teve {data['counter']} visitas.\n"

          dispatcher.utter_message(text=historico_das_casas)

          return []