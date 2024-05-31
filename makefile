.PHONY: start

start:
	docker-compose up -d && \
	docker-compose exec python bash -c " \
		python manage.py makemigrations && \
		python manage.py migrate && \
		python manage.py runscript clean_tables && \
		python manage.py runscript populate_tables \
	" && \
	docker-compose up
