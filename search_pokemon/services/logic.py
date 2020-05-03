import requests


def pokemon_info(name: str) -> dict:
    """
    Utiliza el servicio pokemon de la API pokeapi para obtener datos básicos del pokémon dato su nombre.

    Paramétros:
        name(str): Nombre del pokémon a buscar

    Retorna:
        Diccionario con la información básica del pokémon (nombre, id, peso, altura y estadisticas básicas.
    """
    r = requests.get("https://pokeapi.co/api/v2/pokemon/%s" % name)
    response = r.json()
    pokemon = {
               "name": response["name"],
               "id": response["id"],
               "weight": response["weight"],
               "height": response["height"],
               "stats": []
               }
    for stat in response["stats"]:
        pokemon["stats"].append({stat["stat"]["name"]: stat["base_stat"]})
    return pokemon


def evolution_chain(id_chain: int) -> list:
    """
    Utiliza el servicio evolution-chain de la API pokeapi para obtener datos básicos de los pokémones de una cadena de
    evolución.

    Paramétros:
        id_chain(int): Identificador de la cadena de evolución a buscar.

    Retorna:
        Lista de dicionarios con la información básica de los pokémones que hacen parte de la cadena de evolución.
    """
    r = requests.get("https://pokeapi.co/api/v2/evolution-chain/%d" % id_chain)
    response = r.json()
    names = [response["chain"]["species"]["name"]]
    evolutions = response["chain"]["evolves_to"]
    for evolution in evolutions:
        names.append(evolution["species"]["name"])
        _multiple_evolutions(evolution["evolves_to"], names)
    pokemons = []
    for name in names:
        pokemons.append(pokemon_info(name))
    return pokemons


def _multiple_evolutions(evolutions: list, names: list) -> None:
    """
    Función de ayuda para tratar el caso en que se agreguen pokémones con varias evoluciones que a su vez tengan varias
    evoluciones.

    Paramétros:
        evolutions(list): Lista de evoluciones de un pokémon.
        names(list): Lista de los nombres de los pokémones de la cadena de evolución.
    """
    if len(evolutions) == 0:
        return
    if len(evolutions) == 1:
        names.append(evolutions[0]["species"]["name"])
        _multiple_evolutions(evolutions[0]["evolves_to"], names)
    else:
        for evolution in evolutions:
            names.append(evolution["species"]["name"])
            _multiple_evolutions(evolution["evolves_to"], names)
