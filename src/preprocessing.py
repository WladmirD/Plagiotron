import os
import string
import nltk
from nltk.corpus import stopwords
from nltk import word_tokenize, PorterStemmer, pos_tag
from nltkpreprocess import make_dictionary, vectorization, tfidf_transform, vector_by_tfidf, text_similarity
from nltk.tokenize import sent_tokenize


def preprocessing_nltk(txt_data):
    # Lowercase
    lower_data = txt_data.lower()

    # removing punctuation
    # print("all punctuations: {}".format(string.punctuation))
    punctuation_data = "“”‘’…{}".format(string.punctuation)

    text_p = "".join([char for char in lower_data if char not in punctuation_data])

    # tokenize
    words = word_tokenize(text_p)

    # stopwords filtering
    stop_words = stopwords.words('english')
    # print("stopwords: {}".format(stopwords))
    filtered_words = [word for word in words if word not in stop_words]
    # print(filtered_words)
    # ['truth', 'universally', 'acknowledged', 'single', 'man', 'possession', 'good', 'fortune', 'must', 'want', 'wife']

    # Stemming
    porter = PorterStemmer()
    stemmed = [porter.stem(word) for word in filtered_words]
    # print(stemmed)
    # ['truth', 'univers', 'acknowledg', 'singl', 'man', 'possess', 'good', 'fortun', 'must', 'want', 'wife']

    # pos tag
    pos = pos_tag(filtered_words)
    # print(pos)
    # [('truth', 'NN'), ('universally', 'RB'), ('acknowledged', 'VBD'), ('single', 'JJ'), ('man', 'NN'),
    # ('possession', 'NN'), ('good', 'JJ'), ('fortune', 'NN'), ('must', 'MD'), ('want', 'VB'), ('wife', 'NN')]
    return words, filtered_words, stemmed, pos


def all_sents(txt_data):
    all_sent = sent_tokenize(txt_data.lower())
    sent_data = []
    orig_sent = []
    for sent in all_sent:
        words, sent_words, stemmed, pos = preprocessing_nltk(sent)
        sent_data.append(sent_words)
        orig_sent.append(words)

    return orig_sent, sent_data


def read_txt(txt_file):
    try:
        with open(txt_file, "rt", encoding="utf-8") as r_f:
            return [line.strip() for line in r_f.readlines()]
    except:
        with open(txt_file, "rt") as r_f:
            return [line.strip() for line in r_f.readlines()]


def read_phase(txt_file):
    all_lines = read_txt(txt_file)
    all_phases = []
    cur_phase = []
    for line in all_lines:
        if line:
            cur_phase.append(line)
        else:
            if cur_phase:
                all_phases.append(" ".join(cur_phase))
            cur_phase = []

    if cur_phase:
        all_phases.append(" ".join(cur_phase))

    return all_phases


def read_all_txt(txt_file):
    all_phases = read_phase(txt_file)
    return " ".join(all_phases)


 