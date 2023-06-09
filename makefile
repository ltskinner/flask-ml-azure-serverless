
setup:
	python -m venv ~/.flask-ml-azure

source:
	. ~/.flask-ml-azure/bin/activate

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint-force:
	isort .
	black .

lint-check:
	isort . --check-only
	black --check .
	flake8 .
	pylint --disable=R,C,pointless-string-statement ./app.py ./tests

test:
	coverage run -m pytest -vv ./tests
