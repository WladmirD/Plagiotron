from sentence_transformers import SentenceTransformer, SentencesDataset, InputExample, LoggingHandler, losses, models, util
import nltk
import faiss
import numpy as np
import pandas as pd
import sentence_transformers
import  os

print(sentence_transformers.__version__)
print(nltk.__version__)
print(faiss.__version__)
print(pd.__version__)
print(np.__version__)




nltk.download('punkt')
