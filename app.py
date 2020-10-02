from flask import Flask, renderTemplate,url_for, request
import pandas as pd
import numpy as np
from nltk.stem.porter import PorterStemmer 
import re 
import string
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import logisticRegression

def remove_pattern(input_text, pattern):
    r: re.findall(pattern, input_txt)
    for i in r:
        input_txt = re.sub(i ,'',input_text)
    return input_text