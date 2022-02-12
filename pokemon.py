#################################################################################
# 
# pokemon.py
# 
# A simple command line Python app to get information on your favourite Pokemons!
# 
# Requirement: Please install the requests package by running
#   pip install requests
# 
################################################################################# 

import requests


class Pokemon:

  def __init__(self, name : str) -> None:
    url_pokemon = "https://pokeapi.co/api/v2/pokemon/" + name
    self.pokemon = requests.get(url_pokemon).json()
    url_species = "https://pokeapi.co/api/v2/pokemon-species/" + name
    self.species = requests.get(url_species).json()

  def name(self) -> str:
    return self.pokemon["name"] if "name" in self.pokemon else "???"

  def height(self) -> str:
    return str(self.pokemon["height"]) if "height" in self.pokemon else "???"

  def is_legendary(self) -> str:
    return str(self.species["is_legendary"]) if "is_legendary" in self.species else "???"

  def habitat(self) -> str:
    try:
      return self.species["habitat"]["name"]
    except:
      return "???"

  def types(self) -> str:
    try:
      return str([t["type"]["name"] for t in self.pokemon["types"]])
    except:
      return "???"

  def desc(self) -> str:
    try:
      i = 0
      while self.species["flavor_text_entries"][i]["language"]["name"] != "en":
        i += 1
      return self.species["flavor_text_entries"][i]["flavor_text"].replace("\n", " ").replace("\f", " ")
    except:
      return "???"


def main() -> None:
  
  print(
    "#######################",
    "\n\nWelcome to the Pokedex!",
    "\n\nGet basic information on any Pokemon, or type 'exit' to quit!",
    "\n\n#######################\n"
  )

  exit = False
  while not exit:
    user_input = input("Enter a Pokemon name: ")

    if user_input == "exit":
      exit = True
      continue

    try:
      pokemon = Pokemon(user_input)
    except:
      print("\nFailed to retrieve Pokemon data! Maybe try again?\n")
      continue
    
    print(
      "\nname:", pokemon.name(),
      "\ndescription:", pokemon.desc(),
      "\nheight:", pokemon.height(),
      "\ntypes:", pokemon.types(),
      "\nhabitat:", pokemon.habitat(),
      "\nis_legendary:", pokemon.is_legendary(), "\n"
    )

  return None


if __name__ == '__main__':
  main()