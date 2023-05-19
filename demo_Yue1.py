# Yue Liu
import random

import pandas as pd
import streamlit as st


st.title("GPT Prompt and Answers demo")
st.write("Yue Liu, May 2023")

st.write(
    "In order to prevent privacy leakage of the data we trained on, we fix the clinical notes and instructions that you can test. Please choose each of the notes and instructions!"
)

st.markdown("""---""")

if "rn" not in st.session_state:
    st.session_state["rn"] = random.randint(1, 4)
# rand_idx = random.randint(1, 106)
note_number = st.slider(
    "Select the clinical note. ", 1, 4, st.session_state["rn"]
)


st.write("You selected", f"{note_number}")

mtsamples = pd.read_json("tmp5(4).json")
masked = mtsamples["data"][note_number-1]
note = masked["paragraphs"][0]['context']

q_list = []
for k, qa in enumerate(masked["paragraphs"][0]['qas']):
    q_list.append(qa['question'])
   
st.info(note)

instruction = st.selectbox("Select your instruction", q_list)

def find_loc(string, list):
    for i in range(len(list)):
        if string in list[i]:
            return i
          
          

index = find_loc(instruction, q_list)

Azure = ""
for answer in masked["paragraphs"][0]['qas'][index]['answers']:
     Azure += answer['text']

        
gpt4 = "To add"

st.write("\n")
st.markdown("""---""")
st.write("\n")

st.write("**Azure**")
st.success(Azure)

st.write("**GPT-4**")
st.warning(gpt4)

# st.write("**Alpaca**")
# st.error(alpaca)



