
setup:
	python -m venv ~/.flask-ml-azure

source:
	source ~/.flask-ml-azure/bin/activate

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint-force:
	isort .
	black .

lint-check:
	isort ./app.py ./tests --check-only
	black --check ./app.py ./tests
	flake8 ./app.py ./tests
	pylint --disable=R,C,pointless-string-statement ./app.py ./tests

test:
	coverage run -m pytest -vv ./tests
