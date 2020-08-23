import streamlit as st

from bertosaurus import functions

st.title("Bertosaurus")
st.header("The better thesaurus.")


# check if bert is present
@st.cache
def check():
    functions.check_model_status()


# load models
@st.cache(allow_output_mutation=True)
def load_models():
    bert = functions.load_model("en_trf_bertbaseuncased_lg")
    nlp = functions.load_model("en_core_web_sm")

    return bert, nlp


sentence = st.text_input("Input sentence", "I want to change the world.")
word = st.text_input("Word in sentence", "change")


if not sentence and not word:
    st.warning(
        "Please write the word and the sentence in which the word will\
         be used."
    )
elif not sentence:
    st.warning("Please write the sentence in which the word will be used.")
elif not word:
    st.warning("Please write the word to start searching for synonyms.")
else:

    bert, nlp = load_models()

    st.subheader("Suggested synonyms:")
    syns = functions.ranked_synonyms(sentence, word, nlp, bert)

    for syn, score in syns:
        text = syn + " ({}% match)".format(score)
        st.write(text)
