from django.core.management.base import BaseCommand, CommandError
from ...services import logic
import pprint


class Command(BaseCommand):
    help = 'Encuentra e imprime la información de los Pokémones de una cadena de evolución según su ID'

    def add_arguments(self, parser):
        parser.add_argument('id', type=int, help='ID de la cadena de evolución pokémon a buscar')

    def handle(self, *args, **kwargs):
        try:
            self.stdout.write("La información de la cadena de evolución con id %s es" % kwargs['id'])
            pprint.pprint(logic.evolution_chain(kwargs['id']))
        except RuntimeError as err:
            raise CommandError('Hubo un error al buscar la cadena de evolución: %s' % err)
