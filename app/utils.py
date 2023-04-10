import requests
import json


def get_request_list(url="https://pokeapi.co/api/v2/evolution-chain/"):
    res = requests.get(url)
    if res.status_code == 200:
        content = json.loads(res.content)
        next = content["next"]
        request_list =  [item["url"] for item in content["results"]]
        return request_list, next
    return [], None


def get_no_evolution_from_evolution_chain(evolution_chain):
    # Asumo que existen cadenas en las que se puede terminar en mas de un pokemom
    no_evolution = []

    if not evolution_chain["evolves_to"]:
        name = evolution_chain["species"]["name"]
        no_evolution.append(name)

    for next_pokemon in evolution_chain["evolves_to"]:
        names = get_no_evolution_from_evolution_chain(next_pokemon)
        no_evolution.extend(names)

    return no_evolution


def get_all_pokemon_no_evolution_chain():
    # Asumo que si un pokemos esta al final de 1 cadena, no puede estar en otra cadena
    # en un nivel intermedio

    list_url = url="https://pokeapi.co/api/v2/evolution-chain/?limit=100"
    request_list, next_list_url = get_request_list(url=list_url)

    no_evolution = []

    while request_list:
        chain_url = request_list.pop()
        evolution_chain_request = requests.get(chain_url)

        if evolution_chain_request.status_code == 200:
            evolution_chain = json.loads(evolution_chain_request.content)["chain"]
            names = get_no_evolution_from_evolution_chain(evolution_chain)
            no_evolution.extend(names)

        if not request_list and next_list_url:
            request_list, next_list_url = get_request_list(url=next_list_url)
        
    return no_evolution


def get_pokemon_weight(pokemon):
    # pokemon can be id or name 

    res = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")

    if res.status_code == 200:
        pokemon = json.loads(res.content)
        name = pokemon["species"]["name"]
        weight = pokemon["weight"]

        return {
            "name": name,
            "weight": weight
        }

    return {
        "name": "",
        "weight": float("inf")
    }


def get_min_weight(pokemon_list):
    weights_and_names = [get_pokemon_weight(pokemon) for pokemon in pokemon_list]
    min_weight = min(weights_and_names, key=lambda item: item["weight"])
    return min_weight["name"]


def get_min_weight_no_evolution():
    no_evolution = get_all_pokemon_no_evolution_chain()
    return get_min_weight(no_evolution)
