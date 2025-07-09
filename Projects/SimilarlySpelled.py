import streamlit as st
import requests

st.title("Similarly Spelled Words")

word = st.text_input("Enter a word", placeholder="Eg. Hippo")
is_clicked = st.button("Generate", type='primary')

if is_clicked:
    endpoint = f"https://api.datamuse.com/words?sp={word}"
    response = requests.get(endpoint)

    data = response.json()

    if response.status_code == 200:
        for item in data:
            st.write(item.get('word'))
    else:
        st.toast("Soemthing went wrong")