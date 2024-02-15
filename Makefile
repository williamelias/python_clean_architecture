test:
	docker compose run --rm clean_project pytest clean_project/tests

mer:
	python3 generate_mer.py