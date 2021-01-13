# app.py should pass pylint
# optional, but recommended, build a simple integration test

setup:
	    # Create python virtualenv & source it
	    # source ~/.lyst/bin/activate
	    python -m venv ~/.lyst
			pip install -r requirements.txt

test:
	    # Additional, optional, tests could go here
	    python tests/test.py


validate-circleci:
	    circleci config process .circleci/config.yml

run-circleci-local:
	    circleci local execute

lint:
	    # This is a linter for Python source code linter: https://www.pylint.org/
	    # This should be run from inside a virtualenv
	    pylint --disable=R,C,W1203,C0114,C0301,R0912,C0413,E0401 Tests/*.py Solution/lyst.py

all: setup test lint
