This is our project's repo!

We will be doing a few things:
- scraping, cleaning, and storing data
- loading it into a notebook to train a model for political leaning/credibility
- hosting this model with a web server/api
- creating a google chrome extension to help users access the service & its output. see tutorial here: https://www.sitepoint.com/create-chrome-extension-10-minutes-flat/

For local setup:
- Clone this repository
- Create conda environment from file: `conda env create -f environment.yml`
- Take `finetuned_BERT_epoch_3.model` from Slack and copy into root directory of this repository
- Run flask server with `python3 server/app.py`. It will take a few seconds/minutes to start up the first time, and fewer the next
