SHELL := /bin/bash
MANAGE := python

.PHONY: all help deps static migrate restart update deploy

all: help

help:
	@echo " Usage: "
	@echo "  make start - start game"

pip-install:
	pip install -r requirements.txt

pipenv-install:
	pipenv install

generate-requirement:
	pipenv lock -r > requirements.txt

startapp:
	$(MANAGE) start.py
