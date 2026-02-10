# Запустить сервер
run:
	python manage.py runserver

# Создать новое приложение
new_app:
	python manage.py startapp polls

# Создать файлы миграций на основе изменений моделей
migrations:
	python manage.py makemigrations

# Применить миграции к базе данных
migrate:
	python manage.py migrate

# Запустить линтер
lint:
	pylint $(shell git ls-files '*.py' | grep -v 'migrations/')

test:
	python manage.py test