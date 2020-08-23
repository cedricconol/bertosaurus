import sys

from itertools import chain

import nltk
import spacy
from nltk.corpus import wordnet


class Bertosaurus:
    def __init__(self):
        try:
            self.bert = self._load_model("en_trf_bertbaseuncased_lg")
        except OSError:
            self._download_model("en_trf_bertbaseuncased_lg")
            self.bert = self._load_model("en_trf_bertbaseuncased_lg")

        try:
            self.nlp = self._load_model("en_core_web_sm")
        except OSError:
            self._download_model("en_core_web_sm")
            self.nlp = self._load_model("en_core_web_sm")

    def _download_model(self, model):
        spacy.cli.download(model)

    def _load_model(self, name):
        sys.stdout.write('Loading {}...\n'.format(name))
        model = spacy.load(name)
        sys.stdout.write('Done!\n')
        return model

    def _get_syns(self, text, pos):
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

    def _doc_to_dict(self, doc):
        dictionary = {}

        for token in doc:
            dictionary[str(token)] = token.pos_

        return dictionary

    def _get_word_pos(self, doc, word):
        return self._doc_to_dict(doc)[word]

    def ranked_synonyms(self, sentence, word):
        spacy_to_nltk_pos = {"ADJ": "a", "ADV": "r", "NOUN": "n", "VERB": "v"}

        doc = self.nlp(sentence)
        word_pos = self._get_word_pos(doc, word)
        nltk_pos = spacy_to_nltk_pos[word_pos]

        candidate_words = self._get_syns(word, nltk_pos)

        candidate_sentences = []

        for candidate_word in candidate_words:
            candidate_sentences.append(sentence.replace(word, candidate_word))

        similarity_scores = {}
        sentence_bertified = self.bert(sentence)
        num_words = len(candidate_words)

        for i in range(num_words):
            candidate_bertified = self.bert(candidate_sentences[i])
            similarity_score = sentence_bertified.similarity(
                candidate_bertified
            )
            similarity_scores[candidate_words[i]] = round(similarity_score, 5)

        ranked = sorted(
            similarity_scores.items(), key=lambda kv: kv[1], reverse=True
        )
        return ranked
