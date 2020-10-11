from flask import Flask, renderTemplate,url_for, request
import pandas as pd
import numpy as np
from nltk.stem.porter import PorterStemmer 
import re 
import string
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import logisticRegression

def remove_pattern(input_txt, pattern):
    r: re.findall(pattern, input_txt)
    for i in r:
        input_txt = re.sub(i ,'',input_txt)
    return input_txt

def count_punct(text):
    count = sum([1 for char in text if char in string.punctuation])
    return round(count/len(text) - text.count(" "),3)*100 

app = flask(__name__)
data = pd.read_csv("sentiment.tsv".sep ='\t')
    