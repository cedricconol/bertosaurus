import warnings
from itertools import chain

import nltk
import spacy
import streamlit as st
from nltk.corpus import wordnet

warnings.filterwarnings("ignore")


def is_model_present(model):
    try:
        spacy.load(model)
        return True
    except OSError:
        return False


def download_model(model):
    spacy.cli.download(model)


def check_model_status():
    with st.spinner("Checking if required models are installed..."):
        if is_model_present("en_trf_bertbaseuncased_lg") and is_model_present(
            "en_core_web_sm"
        ):
            return
        else:
            download_model("en_trf_bertbaseuncased_lg")
            download_model("en_core_web_sm")
            return


def load_model(name):
    return spacy.load(name)


def get_syns(text, pos):
    try:
        synonyms = wordnet.synsets(text, pos=pos)
    except LookupError:
        nltk.download("wordnet")
        synonyms = wordnet.synsets(text, pos=pos)

    synonyms = set(
        chain.from_iterable([word.lemma_names() for word in synonyms])
    )
    synonyms.remove(text)
    return list(synonyms)


def doc_to_dict(doc):
    dictionary = {}

    for token in doc:
        dictionary[str(token)] = token.pos_

    return dictionary


def get_word_pos(doc, word):
    return doc_to_dict(doc)[word]


def ranked_synonyms(sentence, word, nlp=None, bert=None):
    if not bert:
        bert = load_model("en_trf_bertbaseuncased_lg")

    if not nlp:
        nlp = load_model("en_core_web_sm")

    spacy_to_nltk_pos = {"ADJ": "a", "ADV": "r", "NOUN": "n", "VERB": "v"}

    doc = nlp(sentence)
    word_pos = get_word_pos(doc, word)
    nltk_pos = spacy_to_nltk_pos[word_pos]

    candidate_words = get_syns(word, nltk_pos)

    candidate_sentences = []

    for candidate_word in candidate_words:
        candidate_sentences.append(sentence.replace(word, candidate_word))

    similarity_scores = {}
    sentence_bertified = bert(sentence)
    num_words = len(candidate_words)

    for i in range(num_words):
        candidate_bertified = bert(candidate_sentences[i])
        similarity_score = sentence_bertified.similarity(candidate_bertified)
        similarity_scores[candidate_words[i]] = round(
            similarity_score * 100, 2
        )

    ranked = sorted(
        similarity_scores.items(), key=lambda kv: kv[1], reverse=True
    )
    return ranked
