import streamlit as st

from bertosaurus import functions


@st.cache
def check_model_status():
    with st.spinner("Checking if required models are installed..."):
        if functions.is_model_present(
            "en_trf_bertbaseuncased_lg"
        ) and functions.is_model_present("en_core_web_sm"):
            return
            # st.success("You're good to go!")
        else:
            functions.download_model("en_trf_bertbaseuncased_lg")
            functions.download_model("en_core_web_sm")
            # st.success("You're good to go!")
            return
