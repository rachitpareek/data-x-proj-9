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

This should explain how to use the deploy script to set up the repo and run the server:
1. `chmod +x deploy.sh` before running the deploy script for the first time.
2. `./deploy.sh setup`
3. `conda activate datax`
4. See instructions in deploy.sh to run your desired command!