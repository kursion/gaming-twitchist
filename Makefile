install:
	@sudo pip install colorama
	@sudo python setup.py install
	@sudo rm -rf build dist *.egg-info
	@echo "Done..."

upload:
	python setup.py sdist upload
