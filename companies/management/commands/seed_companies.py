import random

from django.core.management import BaseCommand
from django_seed import Seed

from companies.models import Company


class Command(BaseCommand):
    help = 'Seeds companies'

    def add_arguments(self, parser):
        parser.add_argument('--number', type=int, help='Create  new company')

    def handle(self, *args, **options):
        seed = Seed.seeder()
        number = options.get('number')
        seed.add_entity(Company, number, {
            'status':lambda x : random.choice(['LAYOFFS', 'HIRING', 'HIRING_FREEZE']),
        })
        seed.execute()
        self.stdout.write(self.style.SUCCESS(f'Seeding {number} companies'))