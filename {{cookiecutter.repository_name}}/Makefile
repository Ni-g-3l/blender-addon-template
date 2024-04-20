PACKAGE_VERSION = $(shell grep -oP 'version": \((.*?)\)' $(CURDIR)/{{cookiecutter.addon_module}}/__init__.py | cut -d'(' -f2 | cut -d')' -f1 | sed 's/, /./g')

install_dev:
	@echo "------------------- INSTALL DEV ENV ------------------- "
	rm -rf /tmp/blender/{{cookiecutter.addon_module}}
	mkdir /tmp/blender/{{cookiecutter.addon_module}}/scripts/addons -p
	ln $(CURDIR)/{{cookiecutter.addon_module}} /tmp/blender/{{cookiecutter.addon_module}}/scripts/addons/{{cookiecutter.addon_module}} -s
	@echo "------------------------------------------------------- "

run:
	@echo "--------------------- RUN BLENDER --------------------- "
	@export BLENDER_USER_SCRIPTS=/tmp/blender/{{cookiecutter.addon_module}}/scripts; \
	blender --addons {{cookiecutter.addon_module}}

deploy:release
	@echo "------------------- DEPLOY PACKAGE -------------------- "
	@echo Deploying ${PACKAGE_VERSION} version
	@git push --tags
	@gh release create ${PACKAGE_VERSION} ./dist/{{cookiecutter.addon_module}}-${PACKAGE_VERSION}.zip --generate-notes --latest 
	@echo "------------------------------------------------------- "

release:build clean
	@echo "------------------- RELEASE PACKAGE ------------------- "
	@echo Releasing ${PACKAGE_VERSION} version
	@git tag ${PACKAGE_VERSION} || echo "Tag already exists."
	@echo "------------------------------------------------------- "

build: clean
	@echo "-------------------- BUILD PACKAGE -------------------- "
	mkdir -p dist
	zip -r dist/{{cookiecutter.addon_module}}-${PACKAGE_VERSION}.zip {{cookiecutter.addon_module}}
	@echo "------------------------------------------------------- "

clean:
	@echo "-------------------- CLEAN PACKAGE -------------------- "
	find . -name \*.pyc -delete
	find . -name __pycache__ -delete
	@echo "------------------------------------------------------- "

test:
	python3 -m unittest discover tests

coverage:
	coverage run -m unittest discover
	coverage report -m
