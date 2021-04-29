# RelAIability

A tool to identify reliability of a news article

RelAibility aims to help internet news-readers by analysing the new sites for fake news. It prevents its users from falling for a plethora of  fake news articles available on the internet. It is user friendly and also gives labels based on how accurate the news presented in the article is. 

## Prerequisites

lists of the software and envrionment that need to be installed. (Python 3.6, Pytorch..)

#### local setup:

- Clone this repository: `git clone https://github.com/rachitpareek/data-x-proj-9`
- Create conda environment from file: `conda env create -f environment.yml`
- Take `finetuned_BERT_epoch_3.model` from Slack and copy into root directory of this repository
- Run flask server with `python3 server/app.py`. It will take a few seconds/minutes to start up the first time, and fewer the next

#### Installing and steps to run the server:

1. `chmod +x deploy.sh` before running the deploy script for the first time.
2. `./deploy.sh setup`
3. `conda activate datax`
4. See instructions in deploy.sh to run your desired command!



### Dataset descriptions

This is an open source dataset composed of millions of news articles mostly scraped from a curated list of 1001 domains from http://www.opensources.co/.

github link:https://github.com/several27/FakeNewsCorpus

The dataset is formatted as a CSV and contains the following fields:

* id
* domain
* type
* url
* content
* scraped_at
* inserted_at
* updated_at
* title
* authors
* keywords
* meta_keywords
* meta_description
* tags
* summary
* source (opensources, nytimes, or webhose)

##### Available types: 

| Type | Description|
|:-------------:|:-------------:|
| **fake** | Sources that entirely fabricate information, disseminate deceptive content, or grossly distort actual news reports |
| **satire** | Sources that use humor, irony, exaggeration, ridicule, and false information to comment on current events. |
| **bias** | Sources that come from a particular point of view and may rely on propaganda, decontextualized information, and opinions distorted as facts. |
| **conspiracy** | Sources that are well-known promoters of kooky conspiracy theories. |
| **junksci** | Sources that promote pseudoscience, metaphysics, naturalistic fallacies, and other scientifically dubious claims. |
| **hate** | Sources that actively promote racism, misogyny, homophobia, and other forms of discrimination. |
| **clickbait** | Sources that provide generally credible content, but use exaggerated, misleading, or questionable headlines, social media descriptions, and/or images. |
| **unreliable** | Sources that may be reliable but whose contents require further verification. |
| **political** | Sources that provide generally verifiable information in support of certain points of view or political orientations. |
| **reliable** | Sources that circulate news and information in a manner consistent with traditional and ethical practices in journalism (Remember: even credible sources sometimes rely on clickbait-style headlines or occasionally make mistakes. No news organization is perfect, which is why a healthy news diet consists of multiple sources of information). |

### Model Interpretation



### Performance


