.PHONY: populate

populate:
	python manage.py runscript clean_tables && python manage.py runscript populate_tables
