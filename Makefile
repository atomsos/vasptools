.PHONY: all build install test

all:
	make build
	make install
	make test



README.rst: README.md
	pandoc README.md -o README.rst


build:
	rm -rf build/ sdist/ dist/ vasptools.egg-info/
	make README.rst
	python setup.py sdist build
	python setup.py bdist_wheel --universal

install:
	python setup.py install --user

travisinstall:
	python setup.py install

test:
	python ./test_dir/test.py

upload:
	twine upload dist/*

