from django.db import models


class Stat (models.Model):
    name = models.CharField(max_length=15, primary_key=True)

    def __str__(self):
        return self.name


class Pokemon (models.Model):
    name = models.CharField(max_length=30, primary_key=True)
    id = models.PositiveIntegerField(unique=True)
    height = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()
    stats = models.ManyToManyField(Stat, through='PokemonStat')

    def __str__(self):
        return "Nombre: %s\nID: %d\nAltura: %d\nPeso: %d" % (self.name, self.id, self.height, self.weight)


class PokemonStat(models.Model):
    pokemon_name = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    stat = models.ForeignKey(Stat, on_delete=models.CASCADE)
    base = models.PositiveIntegerField()

    def __str__(self):
        return "Pokémon: %s\nEstadistica: %s\n Valor base: %d" % (self.pokemon_name.name, self.stat, self.base)


class EvolutionChain(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    pokemons = models.ManyToManyField(Pokemon, through="PokemonEvolution")

    def __str__(self):
        return "Cadena de Evolución: %d\n Pokémon: %s\n" % (self.id, self.pokemons)


class PokemonEvolution(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    evolution_chain = models.ForeignKey(EvolutionChain, on_delete=models.CASCADE)
    position = models.PositiveSmallIntegerField()

    def __str__(self):
        return "Cadena de Evolución: %d\n Pokémon: %s\n Posición: %d" % (self.evolution_chain.id, self.pokemon,
                                                                         self.position)
