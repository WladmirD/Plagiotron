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



word_embedding_model = sentence_transformers.models.Transformer('./model/paraphrase-mpnet-base-v2-2021-07-07_13-50-47/0_Transformer')

# Apply mean pooling to get one fixed sized sentence vector
pooling_model = models.Pooling(word_embedding_model.get_word_embedding_dimension(),
                               pooling_mode_mean_tokens=True,
                               pooling_mode_cls_token=False,
                               pooling_mode_max_tokens=False)

model = SentenceTransformer(modules=[word_embedding_model, pooling_model])




