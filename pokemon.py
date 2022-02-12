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


# This function returns the Pokemon's information as a dictionary.
def get_pokemon(name : str) -> dict:
  
  # Get Pokemon information.
  url_pokemon = "https://pokeapi.co/api/v2/pokemon/" + name
  pokemon_req = requests.get(url_pokemon)

  # Raise an exception if fetching data failed.
  if pokemon_req.status_code != 200:
    raise Exception("Something went wrong with the request!")

  # Retrieve available data from this request.
  pokemon = pokemon_req.json()
  output = {
    "name": pokemon["name"],
    "height": pokemon["height"],
    "types": str([t["type"]["name"] for t in pokemon["types"]])
  }
  
  # Access the species resource for Pokemon description, habitat,
  # and legendary status.
  url_species = pokemon["species"]["url"]
  species_req = requests.get(url_species)
  species = species_req.json()

  output["is_legendary"] = str(species["is_legendary"])

  # Sometimes, a Pokemon has no habitat.
  try:
    output["habitat"] = species["habitat"]["name"]
  except:
    output["habitat"] = "???"
  
  # Take first English-language flavour text as description.
  i = 0
  while species["flavor_text_entries"][i]["language"]["name"] != "en":
    i += 1
  output["desc"] = species["flavor_text_entries"][i]["flavor_text"]\
    .replace("\n", " ").replace("\f", " ")
  
  return output


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
      pokemon_info = get_pokemon(user_input)
    except:
      print("\nFailed to retrieve Pokemon data! Maybe try again?\n")
      continue
    
    print(
      "\nname:", pokemon_info["name"],
      "\ndescription:", pokemon_info["desc"],
      "\nheight:", pokemon_info["height"],
      "\ntypes:", pokemon_info["types"],
      "\nhabitat:", pokemon_info["habitat"],
      "\nis_legendary:", pokemon_info["is_legendary"], "\n"
    )

  return None


if __name__ == '__main__':
  main()