install:
	@sudo pip install colorama
	@sudo python setup.py install
	@sudo rm -rf build dist *.egg-info
	@echo "Done..."

upload:
	@sudo rm -rf build dist *.egg-info
	python setup.py sdist upload
