# Данный скрипт следует запускать при первой инициализации проекта на машине, после голого старта.

# Инициализация aerich
docker-compose exec web aerich init -t db.TORTOISE_ORM

# Инициализация базы данных, связь моделей
docker-compose exec web aerich init-db

# Создание миграций
docker-compose exec web aerich migrate

# Проведение миграций
docker-compose exec web aerich upgrade