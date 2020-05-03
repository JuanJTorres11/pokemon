from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Encuentra e imprime la información de un Pokémon según su ID'

    def add_arguments(self, parser):
        parser.add_argument('id', type=int, help='ID del pokémon a buscar')

    def handle(self, *args, **kwargs):
        try:
            self.stdout.write("TODO info de evolución %s" % kwargs['id'])
        except:
            raise CommandError('Hubo un error')