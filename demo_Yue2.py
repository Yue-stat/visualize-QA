# Yue Liu
import random

import pandas as pd
import streamlit as st
import json


gpt4 = "To add"

with open('gpt4_result.json') as json_file:
    gpt4_result = json.load(json_file)

A = [[0 for i in range(30)] for j in range(10)]

st.title("GPT Prompt and Answers demo")
st.write("Yue Liu, May 2023")

st.write(
    "Please choose each of the notes and instructions! :sunglasses:"
)

st.markdown("""---""")

if "rn" not in st.session_state:
    st.session_state["rn"] = random.randint(1, 10)
# rand_idx = random.randint(1, 106)
note_number = st.slider(
    "Select the clinical note. :smile:", 1, 10, st.session_state["rn"]
)


st.write("You selected", f"{note_number}")

mtsamples = pd.read_json("demo.json")

masked = mtsamples["data"][note_number-1]

note = masked["paragraphs"][0]['context']

st.info(note)

st.markdown("""---""")


col1, col2, col3 = st.columns(3)

with col1:
  st.write("Questions")
          
          
with col2:
  st.write("Answers")
  

      
q_list = []
for k, qa in enumerate(masked["paragraphs"][0]['qas']):
    
    
    Azure = ""
    for answer in qa['answers']:
      Azure = Azure + "; " + answer['text']
    Azure = Azure[2:]
    
    gpt4 = gpt4_result[note_number-1][k]
    col1, col2, col3 = st.columns(3)
    with col1:
      st.write(qa['question'])
      st.markdown("""---""")
          
          
    with col2:
      st.write("**ChatGPT** (API from Azure)")
      st.success(Azure)
      st.write("**GPT-4**")
      st.warning(gpt4)
      st.markdown("""---""")
  
    with col3:
        A60 = st.radio(
            "Choose an answer 👇",
            ("ChatGPT", "GPT-4"),
    )
        A60
        A[note_number-1][k] = A60
  

