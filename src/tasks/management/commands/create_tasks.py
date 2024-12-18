from django.core.management.base import BaseCommand
from multiprocessing import Pool, cpu_count

from tasks.tasks import create_task


class Command(BaseCommand):
    help = 'Create multiple tasks using a pool of processes'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, nargs='?', default=100, help='Number of tasks to create')

    def handle(self, *args, **options):
        count = options['count']
        workers = cpu_count()
        with Pool(processes=workers) as pool:
            pool.map(create_task, range(count))
        self.stdout.write(self.style.SUCCESS(f'Successfully created {count} tasks'))
