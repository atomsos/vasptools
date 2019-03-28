.PHONY: all build install test

all:
	make build
	make install
	make test



build:
	rm -rf build/ sdist/ dist/ vasptools.egg-info/
	python setup.py sdist build
	python setup.py bdist_wheel --universal

install:
	python setup.py install --user

travisinstall:
	python setup.py install

test:
	coverage run ./vasptools/test/test.py
	coverage report
	vasptools -h
	vasptools LISTSUBCOMMAND
	vasptools LISTSUBCOMMAND | xargs -n 1 -I [] vasptools [] -h



upload:
	twine upload dist/*

