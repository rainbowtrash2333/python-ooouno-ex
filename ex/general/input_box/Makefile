BUILD_DIR  = input_box
BUILD_ROOT_DIR = ../../../build
BUILD  = $(BUILD_ROOT_DIR)/$(BUILD_DIR)

help:
	@echo "Run make build to compile into 'build/$(BUILD_DIR)' folder."
	@echo "Run make run to execute the dialog script locally."


.PHONY: build run help

build:
	oooscript compile --pyz-out --embed --config "$(PWD)/config.json" --embed-doc "$(PWD)/inputbox.odt" --build-dir "build/$(BUILD_DIR)"
	rm -f $(BUILD)/*.pyz
	rm -f $(BUILD)/*.py

run:
	python $(PWD)/run.py