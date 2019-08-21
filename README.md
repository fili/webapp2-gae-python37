# webapp2 on Google App Engine Standard Python 3.7

Create a new virtual environment:

	virtualenv -p python3.7 env

To activate the environment:

	source env/bin/activate

Then run:

	pip install -r requirements.txt

Afterwards, to run the webserver:

	python main.py
	
To test with gcloud SDK, first get out of the virtual environment:

	deactivate
	
Then run the gcloud SDK shortcut to set up a temporary local GAE instance supporting Python 3.7:

	dev_appserver.py app.yaml


### Author

- [Fili Wiese](https://fili.org/) 
