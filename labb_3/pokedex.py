#! /usr/bin/env python3

import sys
import requests

API_SERVER = "https://www.ida.liu.se/~TDDE44/pokeapi/"

def get_json_as_dict(url):
    # print("Running get_json_as_dict with the url '{}'".format(url))
    r = requests.get(url)
    if r.status_code == 200:
        return r.json()
    else:
        return None

def get_pokemon_url(pokemon_name):
    data = get_json_as_dict(API_SERVER + "api/v2/pokemon")

    for pokemon in data["results"]:
        if pokemon["name"] == pokemon_name:
            return API_SERVER + pokemon["url"]
    
    return None

def get_pokemon(pokemon_name):
    url = get_pokemon_url(pokemon_name)
    if url:
        return get_json_as_dict(url)
    else:
        return None

# Returns a list of the json files for every ability the pokemon has.
def get_pokemon_abilities(pokemon_data):
    abilities = []
    abilities_short = pokemon_data["abilities"]
    for ability_short in abilities_short:
        ability_url = ability_short["ability"]["url"]
        abilities.append(get_json_as_dict(API_SERVER + ability_url))

    return abilities

# Returns the name and description of the ability in the given language.
def get_ability_info(ability, language):
    ability_info = {}
    
    # Get name in the given language.
    for name in ability["names"]:
        if name["language"]["name"] == language:
            ability_info["name"] = name["name"]
            break
    
    # Get text entry/description in the given language.
    for text_entry in ability["flavor_text_entries"]:
        if text_entry["language"]["name"] == language:
            ability_info["text_entry"] = text_entry["flavor_text"]
            break 

    return ability_info

def main():
    if len(sys.argv) == 1:
        print("Enter the name of a pokemon to see its abilities.")
    elif len(sys.argv) == 2:
        language = "en"
    else:sys
    pokemon_name = sys.argv[1].lower()
    language = sys.argv[2].lower()

    pokemon_data = get_pokemon(pokemon_name)
    if pokemon_data:
        abilities = get_pokemon_abilities(pokemon_data)
        
        print("{} has {} abilities.\n".format(pokemon_name.capitalize(), len(abilities)))
        
        for ability in abilities:
            ability_info = get_ability_info(ability, language)
            if ability_info:
                print("Ability '{}':".format(ability_info["name"]))
                print(ability_info["text_entry"] + "\n")
            else:
                print("No ability information in the specified language was found.".format(language))
                break
        
    else:
        print("No information about '{}' was found.".format(sys.argv[1]))

main()