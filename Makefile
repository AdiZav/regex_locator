.PHONY: help build run all

help:

	    @echo ""
	    @echo "Makefile commands:"
	    @echo "build"
	    @echo "push"
	    @echo "all"

.DEFAULT_GOAL := all

build:
	    @docker build -t regex_locator-img .

run:
	    docker run -it --name regex_locator-test_cont regex_locator-img
	    docker cp regex_locator-test_cont:/regex_locator/test.log .



all: build run