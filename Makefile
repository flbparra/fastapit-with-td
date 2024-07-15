run:
	@uvicorn store.main:app --reload

precommit-intall:
	@poetry run pre-commit install

test:
	@poetry run pytest
