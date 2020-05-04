# Generated by Django 3.0.5 on 2020-05-04 00:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EvolutionChain',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('id', models.PositiveIntegerField(unique=True)),
                ('height', models.PositiveIntegerField()),
                ('weight', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Stat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('speed', 'speed'), ('special-defense', 'special-defense'), ('special-attack', 'special-attack'), ('defense', 'defense'), ('attack', 'attack'), ('hp', 'hp')], max_length=15, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='PokemonStat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base', models.PositiveIntegerField()),
                ('pokemon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search_pokemon.Pokemon')),
                ('stat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search_pokemon.Stat')),
            ],
        ),
        migrations.CreateModel(
            name='PokemonEvolution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.PositiveSmallIntegerField()),
                ('evolution_chain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search_pokemon.EvolutionChain')),
                ('pokemon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search_pokemon.Pokemon')),
            ],
        ),
        migrations.AddField(
            model_name='pokemon',
            name='stats',
            field=models.ManyToManyField(through='search_pokemon.PokemonStat', to='search_pokemon.Stat'),
        ),
        migrations.AddField(
            model_name='evolutionchain',
            name='pokemon',
            field=models.ManyToManyField(through='search_pokemon.PokemonEvolution', to='search_pokemon.Pokemon'),
        ),
    ]
