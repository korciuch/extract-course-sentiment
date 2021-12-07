import os
import csv
import nltk.data
import regex as re
import networkx as nx
from pymongo import MongoClient
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.parse.corenlp import CoreNLPServer
from nltk.parse import CoreNLPParser, CoreNLPDependencyParser
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer, _preprocess