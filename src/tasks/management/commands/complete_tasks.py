from django.core.management.base import BaseCommand
from multiprocessing import Pool, cpu_count

from tasks.tasks import fetch_task


class Command(BaseCommand):
    help = 'Create a pool of worker processes to execute tasks'

    def handle(self, *args, **kwargs):
        workers = cpu_count()
        with Pool(processes=workers) as pool:
            pool.map(fetch_task, range(1, workers + 1))
        self.stdout.write('Successfully executed tasks')
