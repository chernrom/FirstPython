from celery import Celery

# Создаем экземпляр Celery с RabbitMQ в качестве брокера и бэкенда
celery_app = Celery(
    'tasks',
    broker='amqp://guest:guest@localhost:5672//',  # Брокер
    backend='rpc://'  # Бэкенд для результатов (использует RabbitMQ)
)

# Определяем задачу
@celery_app.task
def add_two_numbers(x, y):
    return x + y