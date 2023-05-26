import random
import numpy
import pandas as pd
import streamlit as st

mtsamples = pd.read_json("mtsamples.json")

st.title("demo")
st.write(
    "In order to prevent privacy leakage of the data we trained on, we fix the clinical notes and instructions that you can test. Please choose each of the notes and instructions!"
)

st.markdown("""---""")
if "rn" not in st.session_state:
    st.session_state["rn"] = random.randint(1, 10)
# rand_idx = random.randint(1, 106)
note_number = st.slider(
    "Select the clinical note. There are total 10.", 1, 10, st.session_state["rn"]
)


masked = mtsamples[mtsamples["note_number"] == note_number]

st.info(masked.input.values[0])


instruction = st.selectbox("Select your instruction", masked["instruction"].values)

masked_twice = masked[masked["instruction"] == instruction]

gpt_score = masked_twice["gpt-3.5-score"].values[0]
alpaca_score = masked_twice["alpaca-score"].values[0]
camel_score = masked_twice["clinical_alpaca(ft)-score"].values[0]

gpt = masked_twice["gpt-3.5"].values[0]
alpaca = masked_twice["alpaca"].values[0]
camel = masked_twice["clinical_alpaca(ft)"].values[0]

st.write("\n")
st.markdown("""---""")
st.write("\n")

st.write("**GPT-3.5**", f"({gpt_score}/10)")
st.success(gpt)

st.write("**CAMEL**", f"({camel_score}/10)")
st.warning(camel)

st.write("**Alpaca**", f"({alpaca_score}/10)")
st.error(alpaca)
