build:
	mkdir -p dist/build
	zip -r dist/build/{{cookiecutter.addon_module}}.zip {{cookiecutter.addon_module}}

test:
	python -m unittest discover

coverage:
	coverage run -m unittest discover
	coverage report -m
