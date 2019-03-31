.PHONY: all build install test

all:
	make build
	make install
	make test



build:
	rm -rf build/ sdist/ dist/ vasptools-*/ vasptools.egg-info/
	python setup.py sdist build
	python setup.py bdist_wheel --universal
	twine check dist/*

install:
	python setup.py install --user

travisinstall:
	python setup.py install

test:
	coverage run --source vasptools ./vasptools/test/test.py 
	coverage run --source vasptools `which vasptools` -h
	coverage run --source vasptools `which vasptools` LISTSUBCOMMAND
	coverage run --source vasptools `which vasptools` LISTSUBCOMMAND | xargs -n 1 -I [] bash -c '(coverage run --source vasptools `which vasptools` [] -h >/dev/null 2>&1 || echo ERROR: [])'
	coverage report -m

test_env:
	bash -c ' \
	rm -rf venv; \
	virtualenv venv; \
	source venv/bin/activate; \
	which python; \
	python --version; \
	pip install -r requirements.txt; \
	make build; \
	make travisinstall; \
	make test'
	
upload:
	twine upload dist/*

