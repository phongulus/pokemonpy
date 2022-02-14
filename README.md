# Pokemonpy

A simple command-line Python app that returns basic information on Pokemons using PokeAPI!

## Requirements

This app requires Python 3 and the `requests` package. Install this package by running:
```
pip install requests
```

## Usage

Simply run `pokemon.py` to launch the command line app and enter a Pokemon name. Pokemonpy will attempt to retrieve the relevant information from `https://pokeapi.co/api/v2/pokemon/name` plus the `species-id` of the Pokemon and print out the former. Extra information will also be retrieved from `https://pokeapi.co/api/v2/pokemon-species/species-id` and be printed out as well.

If nothing is found at `https://pokeapi.co/api/v2/pokemon/name`, Pokemonpy will instead check to see if that `name` is present under `https://pokeapi.co/api/v2/pokemon-species` and return information that can obtained there. A `varieties` list will also be displayed with the names of the Pokemons under this species group. Enter the name of one of these Pokemons to see its `"name"`, `"height"`, and `"types"` attributes.

Alternatively, if you want to do other things with the `get_pokemon` and `get_species` functions, just copy `pokemon.py` into your project and add:
```
from pokemon import get_pokemon, get_species
```

`get_pokemon` will, given the name of a Pokemon (a string) as argument, return information about the Pokemon's `"name"`, `species_name`,  `"height"`, `"description"`, `"types"`, `"habitat"`, and `"is_legendary"` status as a dictionary.

The `get_species` function will, given the name of a Pokemon species (a string), return the `species_name`, `"description"`, `"habitat"`, and `"is_legendary"` status, as well as a `varieties` list containing the names of the Pokemons under that species group.

You can also run `test.py` to stress test Pokemonpy by retrieving info on every available Pokemon (all 1118 of them!). This isn't very useful as it doesn't print out anything and is more for debugging. It's also not recommended to run this often, as Python will send >2000 HTTP requests to PokeAPI each time. According to the PokeAPI documentation, each IP address is limited to 300 requests per resource per day, so it is technically possible to run `test.py` about 300 times before being blocked for the day (probably a bit less than that since some resources from `https://pokeapi.co/api/v2/pokemon-species` will be called more than once per run, due to multiple Pokemon varieties being of the same species), but that would be considered abusive usage of PokeAPI.

## To-do (for production)

- More information on the Pokemons! Maybe have a Pokemon class to store all this?
- Add caching features to store Pokemon info temporarily. This will improve performance for repeated requests and make Pokemonpy comply with PokeAPI's fair use policy. A SQLite database might be appropriate for the job. Alternatively, use a Python wrapper for PokeAPI such as PokeBase or Pokepy, both of which provide automatic caching.
- Be more generous with the Pokemon name input. Remove case sensitivity for name input. Add suggestions for Pokemon names? This would require calling either `https://pokeapi.co/api/v2/pokemon-species` or `https://pokeapi.co/api/v2/pokemon/` at launch to get the full list of possible names.