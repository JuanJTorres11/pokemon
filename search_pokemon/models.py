from django.db import models


class Stat (models.Model):
    STATS = [
        ("speed", "speed"),
        ("special-defense", "special-defense"),
        ("special-attack", "special-attack"),
        ("defense", "defense"),
        ("attack", "attack"),
        ("hp", "hp")
    ]
    name = models.CharField(max_length=15, choices=STATS, unique=True)


class Pokemon (models.Model):
    name = models.CharField(max_length=30, primary_key=True)
    id = models.PositiveIntegerField(unique=True)
    height = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()
    stats = models.ManyToManyField(Stat, through='PokemonStat')


class PokemonStat(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    stat = models.ForeignKey(Stat, on_delete=models.CASCADE)
    base = models.PositiveIntegerField()


class EvolutionChain(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    pokemon = models.ManyToManyField(Pokemon, through="PokemonEvolution")


class PokemonEvolution(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    evolution_chain = models.ForeignKey(EvolutionChain, on_delete=models.CASCADE)
    position = models.PositiveSmallIntegerField()
