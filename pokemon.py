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
      url_pokemon = "https://pokeapi.co/api/v2/pokemon/" + user_input
      pokemon = requests.get(url_pokemon).json()
      url_species = "https://pokeapi.co/api/v2/pokemon-species/" + user_input
      species = requests.get(url_species).json()
    except:
      print("\nFailed to retrieve Pokemon data! Maybe try again?\n")
      continue

    # Check if the required data are available. Missing data will have 
    # "???" displayed instead.
    name = pokemon["name"] if "name" in pokemon else "???"
    height = pokemon["height"] if "height" in pokemon else "???"
    legend = species["is_legendary"] if "is_legendary" in species else "???"
    try:
      habitat = species["habitat"]["name"]
    except:
      habitat = "???"
    try:
      types = [t["type"]["name"] for t in pokemon["types"]]
    except:
      types = "???"
    try:
      desc = species["flavor_text_entries"][0]["flavor_text"]
      desc = desc.replace("\n", " ").replace("\f", " ")
    except:
      desc = "???"
    
    print(
      "\nname:", name,
      "\ndescription:", desc,
      "\nheight:", height,
      "\ntypes:", types,
      "\nhabitat:", habitat,
      "\nis_legendary:", legend, "\n"
    )

  return None

if __name__ == '__main__':
  main()