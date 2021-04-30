# RelAIability

A tool to identify reliability of a news article.

RelAibility aims to help internet news-readers by analysing the new sites for fake news. It prevents its users from falling for a plethora of  fake news articles available on the internet. It is user friendly and also gives classification labels using a Google BERT-based model that is hosted using a Flask API and is consumed by a frontend and a Google Chrome extension. 

### Installing and steps to run the server and extension after cloning this repository:

1. `chmod +x deploy.sh` before running the deploy script for the first time.
2. `./deploy.sh setup`
3. `conda activate datax`
4. `./deploy.sh server`
5. Open Google Chrome, and navigate to `chrome://extensions/` in the omnibox.
6. Enable `Developer mode` on the top right of the screen. 
7. Click `Load unpacked` and navigate to the `extension` folder within this repository. Select it and load it in. 
8. Enjoy using the extension! It works on the `news.html` demo page within the `samples` directory, articles on `nbcnews.com`, and you can enter freeform text at `http://localhost:5000`.

See more instructions in deploy.sh to run your desired command!

### Directory descriptions:

Use the deploy script as explained above and documented within the file itself to get up and running!

| Directory | Description|
|:-------------:|:-------------:|
| **extention** | Contains all relevant source code for the Google Chrome extension. |
| **notebooks** | Contains various Jupyter Notebooks that were used to train iterations of the models, used to just predict labels for given text with a pretrained model, and also contains some basic sample data. |
| **samples** | Contains sample news pages and supporting CSS/JS files. |
| **server** | Contains Flask server code that runs the API, various HTML templates, supporting CSS/JS static files, and more. |

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

##### Available labels: 

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

#### Notebooks:
The directory contains codes that were used for expirmenting with the models and the finalised code for the BERT model. The codes were written in Jupyter Notebook environment and this are all .ipynb files.
- RandomForest_datax_final.ipynb : code used in low tech demo for a random forest model that would serve as a placeholder while the team worked on implementing BERT. Ramdom Forest was chosen due to its suitability for classification problems and quick implementability. 
- training_bert.ipynb : code used to train BERT model, and outputting model metrics and confusion matrix over prediction for the test set. pre-trained BERT Base Uncased model is trained upon the dataset from FakeNewsChallenge's 10000 rows in the PyTorch environment.
- code_to_predict.ipynb : code that shows how to make a prediction with the saved BERT model for a sample text.
- training_bertnewarch.ipynb : code that adds additional drop-put layers to BERT model to improve performance. This represents potential future improvements to the current model.

#### Server:
We have an informational page hosted by the server that provides explanations of what each label actually means for the user. 

### Performance


