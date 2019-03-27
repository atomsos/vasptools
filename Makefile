PHONY: all

all:
	make README.rst



README.rst: README.md
	pandoc README.md -o README.rst

