## Clustering PM Job Descriptions
# To better understand overarching similarities 

import pandas as pd
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import *
from sklearn.cluster import KMeans
from sklearn.decomposition import LatentDirichletAllocation

jd = pd.read_csv('jds.csv')

desc = jd.iloc[:,2]
desc_list = desc.values.tolist()

qual = jd.iloc[:,3]
qual_list = qual.values.tolist()

# Analyzing listing description first



# Analysing listing qualifications second