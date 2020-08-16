import spacy
import streamlit as st

from bertosaurus import functions
from bertosaurus._helper import check_model_status

st.title("Bertosaurus")
st.header("The better thesaurus.")

# check if bert is present
check_model_status()

with st.spinner("Loading models..."):
    bert = spacy.load("en_trf_bertbaseuncased_lg")
    nlp = spacy.load("en_core_web_sm")

sentence = st.text_input("Input sentence", "I want to change the world.")
word = st.text_input("Word in sentence", "change")

# if st.button('Find synonyms'):
#     st.write('good')
# else:
#     st.write('bad')

st.subheader("Suggested synonyms:")
syns = functions.rank_syns(sentence, word, nlp, bert)

for syn, score in syns:
    text = syn + " ({}% match)".format(score)
    st.write(text)
