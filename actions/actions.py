###########
# IMPORTS #
###########
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

# Requisição na API
import requests
from random import randint

################## 
# BANCO DE DADOS #
################## 
from pymongo import MongoClient

client = MongoClient("mongodb+srv://root:root@cluster0.zhp6j.mongodb.net/database?retryWrites=true&w=majority")
db = client["database"]
collection = db["historico"]

#############
# FUNCTIONS #
#############
def verify_house(house):
  if house in "grifinoriagrifinóriagriffy":
    return "Gryffindor"
  elif house in "sonserina":
    return "Slytherin"
  elif house in "lufa-lufalufa lufa":
    return "Hufflepuff"
  elif house in "corvinal":
    return "Ravenclaw"

###########
# ACTIONS #
###########
class ActionShowCharacter(Action):

    def name(self) -> Text:
        return "action_show_character"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            
        casa = tracker.get_slot("house")
        house = verify_house(casa.lower())

        # Fazendo a requisição na API
        api_url = f"http://hp-api.herokuapp.com/api/characters/house/{house}"
        response = requests.get(api_url)
        house = response.json()

        # Gerando um personagem random de 1 a 15
        character = house[randint(1, 15)]

        dispatcher.utter_message(image=character['image'])

        # Verificando gênero do personagem
        if character['gender'] in "male":
          dispatcher.utter_message(text=f"{character['name']} será seu acompanhante, ele vai te mostrar {casa.title()}.")
        else:
          dispatcher.utter_message(text=f"{character['name']} será sua acompanhante, ela vai te mostrar {casa.title()}.")

        # Enviando personagem para o BD
        character_simplified = {'name': character['name'],
                        'actor': character['actor'],
                        'house': character['house'],
                        'yearOfBirth': character['yearOfBirth']}

        collection.insert_one(character_simplified)

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