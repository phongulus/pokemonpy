#################################################################################
# 
# test.py
# 
# Run this file to test the Pokemon class on every available Pokemon (1126 in
# total as of writing). 
# 
# Requirement: Please install the requests package by running
#   pip install requests
# 
################################################################################# 

import requests
from pokemon import get_pokemon


def main() -> None:
  
  url = "https://pokeapi.co/api/v2/pokemon?limit=1200"
  all_pokemons = requests.get(url).json()
  num_pokemons = all_pokemons["count"]
  print("Retrieved", num_pokemons, "pokemon names.")

  i = 1
  pct = 0.05
  print("Retrieving data on these pokemons! This might take a while.")
  for pokemon_ in all_pokemons["results"]:
    try:
      get_pokemon(pokemon_["name"])
    except Exception as e:
      print("Got an error for the", str(i) + "-th Pokemon!")
      print(e)
    i += 1
    if i / num_pokemons >= pct:
      print(str(int(pct * 100)) + "%", "done.")
      pct += 0.05

  print("Done!")
  return None


if __name__ == '__main__':
  main()