from math import factorial
from random import randint, choice
from django.db import transaction

from tasks.models import Task


def calculate_factorial(number: int) -> int:
    return factorial(number)


def get_random_number(number: int) -> int:
    return randint(1, number)


tasks = {
    'Factorial': calculate_factorial,
    'Get random number': get_random_number,
}


def create_task(_):
    Task.objects.create(
        task_info={
            'name': choice(tuple(tasks.keys())),
            "args": (randint(10, 1000), ),
        },
    )


def fetch_task(worker_id):
    while True:
        with transaction.atomic():
            task = Task.objects.\
                select_for_update(skip_locked=True).\
                filter(status='pending')\
                .order_by('id').first()
            if not task:
                break
            task.status = 'processing'
            task.worker_id = worker_id
            task.save()
    
        process_task(task)


def process_task(task: Task):
    name = task.task_info.get('name')
    args = task.task_info.get('args', [])
    kwargs = task.task_info.get('kwargs', {})
    result = tasks[name](*args, **kwargs)
    task.task_info['result'] = str(result)
    task.status = 'completed'
    task.save()