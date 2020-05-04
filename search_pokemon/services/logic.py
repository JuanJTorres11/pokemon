import requests
from ..models import *
from django.core.exceptions import ObjectDoesNotExist


def add_pokemon(name: str) -> Pokemon:
    """
    Utiliza el servicio pokemon de la API pokeapi para obtener datos básicos del pokémon dato su nombre.

    Paramétros:
        name(str): Nombre del pokémon a buscar

    Retorna:
       Objeto con la información básica del pokémon (nombre, id, peso, altura y estadisticas básicas.
    """

    try:
        return Pokemon.objects.get(name=name)

    except ObjectDoesNotExist:

        r = requests.get("https://pokeapi.co/api/v2/pokemon/%s" % name)
        if not r:
            raise RuntimeError("No existe el nombre de pokémon ingresado")
        response = r.json()
        p = Pokemon(name=response["name"], id=response["id"], weight=response["weight"], height=response["height"])
        p.save()
        for stat in response["stats"]:
            s = Stat.objects.get(name=stat["stat"]["name"])
            ps = PokemonStat(pokemon_name=p, stat=s, base=stat["base_stat"])
            ps.save()
        return p


def get_pokemon(name:str) -> dict:
    """
    Busca el pokémon dado su nombre en la base de datos y crea un diccionario con su información básica.

    Paramétros:
        name(str): Nombre del pokémon a buscar

    Retorna:
       Diccionario con la información básica del pokémon y sus evoluciones.
    """
    try:
        p = Pokemon.objects.get(name=name)
        pokemon = {
            "name": p.name,
            "id": p.id,
            "weight": p.weight,
            "height": p.height,
            "stats": [],
            "evolutions": []
        }
        stats = PokemonStat.objects.filter(pokemon_name=p)
        for stat in stats:
            pokemon["stats"].append({"stat": stat.stat_id, "base": stat.base})

        evolutionChain = PokemonEvolution.objects.get(pokemon=p)
        evolutionId = evolutionChain.evolution_chain
        position = evolutionChain.position
        chain = PokemonEvolution.objects.filter(evolution_chain=evolutionId)
        for evolution in chain:
            if evolution.position > position:
                pokemon["evolutions"].append({"name": evolution.pokemon.name, "id": evolution.pokemon.id,
                                              "evolution_type": "Evolution"})
            elif evolution.position < position:
                pokemon["evolutions"].append({"name": evolution.pokemon.name, "id": evolution.pokemon.id,
                                              "evolution_type": "Preevolution"})

        return pokemon
    except ObjectDoesNotExist:
        return None


def evolution_chain(id_chain: int) -> PokemonEvolution:
    """
    Utiliza el servicio evolution-chain de la API pokeapi para obtener datos básicos de los pokémones de una cadena de
    evolución.

    Paramétros:
        id_chain(int): Identificador de la cadena de evolución a buscar.

    Retorna:
        Lista de dicionarios con la información básica de los pokémones que hacen parte de la cadena de evolución.
    """
    ec = PokemonEvolution.objects.filter(evolution_chain=id_chain)
    if len(ec) == 0:
        r = requests.get("https://pokeapi.co/api/v2/evolution-chain/%d" % id_chain)
        if not r:
            raise RuntimeError("No existe la cadena de evolución de pokémon ingresada")
        response = r.json()
        names = [{"name": response["chain"]["species"]["name"], "pos": 1}]
        evolutions = response["chain"]["evolves_to"]
        for evolution in evolutions:
            names.append({"name": evolution["species"]["name"], "pos": 2})
            _multiple_evolutions(evolution["evolves_to"], names, 3)

        e = EvolutionChain(id=id_chain)
        e.save()
        for name in names:
            p = add_pokemon(name["name"])
            pe = PokemonEvolution(pokemon=p, evolution_chain=e, position=name["pos"])
            pe.save()
        return PokemonEvolution.objects.filter(evolution_chain=id_chain)
    else:
        return ec


def _multiple_evolutions(evolutions: list, names: list, count: int) -> None:
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
        names.append({"name": evolutions[0]["species"]["name"], "pos": count})
        _multiple_evolutions(evolutions[0]["evolves_to"], names, count + 1)
    else:
        for evolution in evolutions:
            names.append({"name": evolution["species"]["name"], "pos": count})
            _multiple_evolutions(evolution["evolves_to"], names, count + 1)
