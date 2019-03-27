.PHONY: all, build, install, test

all:
	make README.rst
	make build
	make install
	make test



README.rst: README.md
	pandoc README.md -o README.rst


build:
	make README.rst
	python setup.py sdist build
	python setup.py bdist_wheel --universal

install:
	python setup.py install --user


test:
	python -c "from vasptools import potcar; print(potcar.get_potcar_content(['H', 'He', 'Li']))"
