#################################################################################
# 
# test.py
# 
# Run this file to test the Pokemon class on every available Pokemon (1118 in
# total as of writing). 
# 
# Requirement: Please install the requests package by running
#   pip install requests
# 
################################################################################# 

import requests
from time import time
from pokemon import get_pokemon


def main() -> None:
  
  url = "https://pokeapi.co/api/v2/pokemon?limit=1200"
  all_pokemons = requests.get(url).json()
  num_pokemons = all_pokemons["count"]
  print("Retrieved", num_pokemons, "pokemon names.")

  i = 1
  pct = 0.05
  print("Retrieving data on these pokemons! This might take a while.")
  start = time()
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

  print("Done! Processed", num_pokemons, "pokemons in roughly", int(time() - start), "seconds.")
  return None


if __name__ == '__main__':
  main()