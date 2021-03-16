# import ml classifiers
from nltk.tokenize import sent_tokenize # tokenizes sentences
from nltk.stem import PorterStemmer     # parsing/stemmer
from nltk.tag import pos_tag            # parts-of-speech tagging
from nltk.corpus import wordnet         # sentiment scores
from nltk.stem import WordNetLemmatizer # stem and context
from nltk.corpus import stopwords       # stopwords
from nltk.util import ngrams            # ngram iterator

import bs4 as bs
import numpy as np
import pandas as pd
import re
import hashlib
 
# download NLTK classifiers - these are cached locally on your machine
import nltk
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('punkt')

from sklearn import metrics
from sklearn.metrics import confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import normalize, FunctionTransformer
from sklearn.feature_extraction.text import CountVectorizer

ps = PorterStemmer()
wnl = WordNetLemmatizer()
eng_stopwords = set(stopwords.words("english"))

def review_cleaner(review, lemmatize=True, stem=False):
    '''
        Clean and preprocess a review.
            1. Remove HTML tags
            2. Extract emoticons
            3. Use regex to remove all special characters (only keep letters)
            4. Make strings to lower case and tokenize / word split reviews
            5. Remove English stopwords
            6. Lemmatize
            7. Rejoin to one string
        
        @review (type:str) is an unprocessed review string
        @return (type:str) is a 6-step preprocessed review string
    '''

    

    if lemmatize == True and stem == True:
        raise RuntimeError("May not pass both lemmatize and stem flags")

    #1. Remove HTML tags
    review = bs.BeautifulSoup(review,features='lxml').text

    #2. Use regex to find emoticons
    emoticons = re.findall('(:D|:\/)(?=\s|[^[:alnum:]+-]|$)', review)

    #3. Remove punctuation
    review = re.sub('[^a-zA-Z ]' ,'',review)

    #4. Tokenize into words (all lower case)
    review_words = (str.lower(review.replace('.','. '))).split()

    #5. Remove stopwords, Lemmatize, Stem
    ### YOUR CODE HERE ###
    
    review_wo_stopwords = [w for w in review_words if not w in eng_stopwords]
    
    token_tag = pos_tag(review_wo_stopwords)
    NN_count = 0
    JJ_count = 0

    for pair in token_tag:
        tag = pair[1]
        if tag == 'JJ':
            JJ_count+=1
        elif tag == 'NN':
            NN_count+=1
        
     
    def get_wordnet_pos(treebank_tag):

        if treebank_tag.startswith('J'):
            return wordnet.ADJ
        elif treebank_tag.startswith('V'):
            return wordnet.VERB
        elif treebank_tag.startswith('N'):
            return wordnet.NOUN
        elif treebank_tag.startswith('R'):
            return wordnet.ADV
        else:
            return 'n'
    
    wnl_stems = []
    
    for pair in token_tag:
        res = wnl.lemmatize(pair[0],pos=get_wordnet_pos(pair[1]))
        wnl_stems.append(res)
    
    for i in emoticons:
        wnl_stems.append(i)
    
    #6. Join the review to one sentence
    review_processed = ' '.join(wnl_stems)
    
    return review_processed

# We vectorize the text using a bag of words model
def get_vectorizer(ngram, max_features):
    return CountVectorizer(ngram_range=(1, ngram),
                             analyzer = "word",
                             tokenizer = None,
                             preprocessor = review_cleaner,
                             stop_words = None, 
                             max_features = max_features)

def article_cleaner(article, lemmatize=True, stem=False):
    #1. Remove HTML tags
    review = bs.BeautifulSoup(article,features='lxml').text
    #2. Use regex to find emoticons
    emoticons = re.findall('(?::|;|=)(?:-)?(?:\)|\(|D|P)', article)
    #3. Remove punctuation
    article = re.sub("[^a-zA-Z]", " ",article)
    #4. Tokenize into words (all lower case)
    article_words = (str.lower(article.replace('.','. '))).split()
    #5. Remove stopwords, Lemmatize, Stem
    ### YOUR CODE HERE ##
    article_wo_stopwords = [w for w in article_words if not w in eng_stopwords]
    token_tag = pos_tag(article_wo_stopwords)
    def get_wordnet_pos(treebank_tag):
        if treebank_tag.startswith('J'):
            return wordnet.ADJ
        elif treebank_tag.startswith('V'):
            return wordnet.VERB
        elif treebank_tag.startswith('N'):
            return wordnet.NOUN
        elif treebank_tag.startswith('R'):
            return wordnet.ADV
        else:
            return 'n'
    wnl_stems = []
    for pair in token_tag:
        res = wnl.lemmatize(pair[0],pos=get_wordnet_pos(pair[1]))
        wnl_stems.append(res)
    for i in emoticons:
        wnl_stems.append(i)
    #6. Join the review to one sentence
    article_processed = ' '.join(wnl_stems)
    return article_processed
    