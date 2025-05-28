from model import pass_image, create_prompt, call_llm, response_to_dataframe
import streamlit as st
import pandas as pd

@st.fragment()
def create_csv(filename, data):
    csv = data.to_csv(index=False)
    with open(f"./data/{filename}.csv", 'w', encoding="utf-8") as f:
        f.write(csv)

st.set_page_config(layout="wide")

st.title("Data Extractor")
with st.container(height=700):

    image = st.file_uploader("Upload Images", type=["jpg", "jpeg", "png"], label_visibility="collapsed")

    left, right = st.columns([0.3,0.7])

    with left:
        with st.container(height=465):
            if image:
                st.image(image=image)
                        

    with right:
        with st.container(height=465, border=True):
            if image:
                data = response_to_dataframe(call_llm(create_prompt(pass_image(image))))    
                st.dataframe(data)

        nested_left, nested_right = st.columns([0.7,0.3])

        with nested_left:
            filename = st.text_input(label="Enter Filename:", placeholder="filepath", label_visibility="collapsed")

        with nested_right:
            if st.button("Download"):
                create_csv(filename, data)

      

    




