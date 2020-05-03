import requests


def pokemon_info(name: str) -> dict:
    r = requests.get("https://pokeapi.co/api/v2/pokemon/%s" % name)
    response = r.json()
    pokemon = {
               "name": response["name"],
               "id": response["id"],
               "weight": response["weight"],
               "stats": []
               }
    for stat in response["stats"]:
        pokemon["stats"].append({stat["stat"]["name"]: stat["base_stat"]})
    return pokemon


def evolution_chain(id_chain: int) -> list:
    r = requests.get("https://pokeapi.co/api/v2/evolution-chain/%d" % id_chain)
    response = r.json()
    names = [response["chain"]["species"]["name"]]
    evolutions = response["chain"]["evolves_to"]
    for evolution in evolutions:
        names.append(evolution["species"]["name"])
        multiple_evolutions(evolution["evolves_to"], names)
    pokemons = []
    for name in names:
        pokemons.append(pokemon_info(name))
    return pokemons


def multiple_evolutions(evolutions: list, names: list) -> None:
    if len(evolutions) == 0:
        return
    if len(evolutions) == 1:
        names.append(evolutions[0]["species"]["name"])
        multiple_evolutions(evolutions[0]["evolves_to"], names)
    else:
        for evolution in evolutions:
            names.append(evolution["species"]["name"])
            multiple_evolutions(evolution["evolves_to"], names)
