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
# Information is retrieved from the https://pokeapi.co/api/v2/pokemon/ endpoint.
def get_pokemon(name : str) -> dict:
  
  # Get Pokemon information.
  pokemon_url = "https://pokeapi.co/api/v2/pokemon/" + name
  pokemon_req = requests.get(pokemon_url)

  # Raise an exception if fetching data failed.
  if pokemon_req.status_code != 200:
    raise Exception("Request failed with status code: " + str(pokemon_req.status_code))

  # Retrieve available data from this request.
  pokemon = pokemon_req.json()
  output = {
    "name": pokemon["name"],
    "height": pokemon["height"],
    "types": [t["type"]["name"] for t in pokemon["types"]]
  }

  return {**output, **get_species(pokemon["species"]["name"], fetch_pokemons=False)}


# This function returns a Pokemon species' information as a dictionary.
# If the optional argument fetch_pokemons is true, the output dictionary will include
# a list of Pokemon varieties under this species group.
# Information is retrieved from the https://pokeapi.co/api/v2/pokemon-species/ endpoint.
def get_species(name : str, fetch_pokemons : bool = True) -> dict:

  # Get Pokemon species information.
  species_url = "https://pokeapi.co/api/v2/pokemon-species/" + name
  species_req = requests.get(species_url)

  # Raise an exception if fetching data failed.
  if species_req.status_code != 200:
    raise Exception("Request failed with status code: " + str(species_req.status_code))

  # Access the species resource for Pokemon description, habitat,
  # and legendary status.
  species = species_req.json()
  output = {}
  output["species_name"] = species["name"]
  output["is_legendary"] = species["is_legendary"]

  # Sometimes, a Pokemon species has no habitat (e.g. lucario).
  try:
    output["habitat"] = species["habitat"]["name"]
  except:
    output["habitat"] = "???"
  
  # Take first English-language flavour text as description.
  i = 0
  while species["flavor_text_entries"][i]["language"]["name"] != "en":
    i += 1
  output["description"] = species["flavor_text_entries"][i]["flavor_text"]\
    .replace("\n", " ").replace("\f", " ")

  if fetch_pokemons:
    output["varieties"] = [p["pokemon"]["name"] for p in species["varieties"]]

  return output


def main() -> None:
  
  print(
    "#######################",
    "\n\nWelcome to Pokemonpy!",
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
      print()
    except Exception as e:
      print("\nFailed to retrieve Pokemon data!")
      print("Error:", e, "\n")
      print("Checking the api/v2/pokemon-species/ endpoint...")
      try:
        pokemon_info = get_species(user_input)
        print("Found species info! To get more details, enter one of the species' varieties.\n")
      except Exception as e1:
        print("Failed to retrieve Pokemon species data!")
        print("Error:", e1, "\n")
        continue
    
    for key, val in pokemon_info.items():
      print("" + key + ":", val)
    print()

  return None


if __name__ == '__main__':
  main()