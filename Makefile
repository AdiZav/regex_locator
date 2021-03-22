current_dir := $(shell pwd)

.PHONY: help build run all

help:

	    @echo ""
	    @echo "Makefile commands:"
	    @echo "build"
	    @echo "push"
	    @echo "all"

.DEFAULT_GOAL := all

one_test-build:
		@docker build -f OneTimeTest_Dockerfile -t regex_locator-one_test-img .

cont_test-build:
	    @docker build -f Dockerfile -t regex_locator-cont_test-img .

one_test-run:
		
	    docker run -it --name regex_locator-one_test regex_locator-one_test-img
	    docker cp regex_locator-one_test:/regex_locator/test.log .

cont_test-run:
		- docker container stop regex_locator-cont_test
		- docker container rm regex_locator-cont_test
		docker run -it --name regex_locator-cont_test -v ${current_dir}/py_code/:/regex_locator/ regex_locator-cont_test-img python ./run_tests.py



all: cont_test-build cont_test-run
