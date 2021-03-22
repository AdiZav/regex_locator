current_dir := $(shell pwd)

.PHONY: help build run all

help:

	    @echo ""
	    @echo "Makefile commands:"
	    @echo "build"
	    @echo "run"
	    @echo "all"

.DEFAULT_GOAL := all

build:
	    @docker build -f Dockerfile -t regex_locator-img .



run:
		- docker container stop regex_locator-cont
		- docker container rm regex_locator-cont
		docker run -it --name regex_locator-cont -v ${current_dir}/py_code/:/regex_locator/ regex_locator-img python ./run_tests.py



all: build run
