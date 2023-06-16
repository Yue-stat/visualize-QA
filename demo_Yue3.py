# Yue Liu
import random

import pandas as pd
import streamlit as st
import json

import requests
import base64
import json
import datetime

st.set_page_config(layout="wide")

def push_to_repo_branch(gitHubFileName, data, repo_slug, branch, user, token):
    
    message = "Automated update " + str(datetime.datetime.now())
    path = "https://api.github.com/repos/%s/branches/%s" % (repo_slug, branch)

    r = requests.get(path, auth=(user,token))
    if not r.ok:
        print("Error when retrieving branch info from %s" % path)
        print("Reason: %s [%d]" % (r.text, r.status_code))
        raise
    rjson = r.json()
    treeurl = rjson['commit']['commit']['tree']['url']
    r2 = requests.get(treeurl, auth=(user,token))
    if not r2.ok:
        print("Error when retrieving commit tree from %s" % treeurl)
        print("Reason: %s [%d]" % (r2.text, r2.status_code))
        raise
    r2json = r2.json()
    sha = None

    for file in r2json['tree']:
        # Found file, get the sha code
        if file['path'] == gitHubFileName:
            sha = file['sha']

    # if sha is None after the for loop, we did not find the file name!
    if sha is None:
        print ("Could not find " + gitHubFileName + " in repos 'tree' ")
        raise Exception

    import binascii

    content = binascii.b2a_base64(data.encode(), newline=False)

    # gathered all the data, now let's push
    inputdata = {}
    inputdata["path"] = gitHubFileName
    inputdata["branch"] = branch
    inputdata["message"] = message
    inputdata["content"] = content.decode('utf-8')
    if sha:
        inputdata["sha"] = str(sha)
    print(inputdata)

    updateURL = f"https://api.github.com/repos/{repo_slug}/contents/" + gitHubFileName
    try:
        rPut = requests.put(updateURL, auth=(user,token), data = json.dumps(inputdata))
        if not rPut.ok:
            print("Error when pushing to %s" % updateURL)
            print("Reason: %s [%d]" % (rPut.text, rPut.status_code))
            raise Exception
    except requests.exceptions.RequestException as e:
        print ('Something went wrong! I will print all the information that is available so you can figure out what happend!')
        print (rPut)
        print (rPut.headers)
        print (rPut.text)
        print (e)
        

    
gpt4 = "To add"

with open('gpt4_result.json') as json_file:
    gpt4_result = json.load(json_file)

score = pd.read_csv('score.csv')

A = [["" for i in range(30)] for j in range(10)]

st.title("GPT Prompt and Answers Demo")
st.write("Yue Liu, May 2023")

st.write(
    "Please choose each of the notes and instructions! :sunglasses:"
)

st.markdown("""---""")

if "rn" not in st.session_state:
    st.session_state["rn"] = random.randint(1, 10)
# rand_idx = random.randint(1, 106)

# hidden div with anchor
st.markdown("<div id='linkto_top'></div>", unsafe_allow_html=True) 



note_number = st.slider(
    "Select the clinical note. :smile:", 1, 10, st.session_state["rn"]
)


st.write("You selected", f"{note_number}")

mtsamples = pd.read_json("demo.json")

masked = mtsamples["data"][note_number-1]

note = masked["paragraphs"][0]['context']

st.info(note)



# hidden div with anchor
st.markdown("<div id='linkto_qa'></div>", unsafe_allow_html=True) 

st.markdown("""---""")


col1, col2, col3 = st.columns([1.3,2,0.3])

with col1:
  st.write("Questions")
          
          
with col2:
  st.write("Answers")
with col3:
    st.write("Choose your score for Eevee 👇 on a scale of 0 to 10")
  

      
q_list = []
for k, qa in enumerate(masked["paragraphs"][0]['qas']):
    
    
    Azure = ""
    for answer in qa['answers']:
      Azure = Azure + "; " + answer['text']
    Azure = Azure[2:]

    
    ind = 30*(note_number-1) + k
    chatgpt_score = score.iloc[ind]['chatgpt_score']
    gpt4_score = score.iloc[ind]['gpt4_score']
    alpaca_score = score.iloc[ind]['alpaca_score']   
    alpaca = score.iloc[ind]['alpaca']  
    
    
    gpt4 = "To add"
    gpt4_score = "NA"
    if k <= 7 or k >= 12:
        gpt4 = gpt4_result[note_number-1][k]
        gpt4_score = score.iloc[ind]['gpt4_score']
        
        
        
    col1, col2, col3 = st.columns([0.5,2,0.2])
    st.markdown("""---""")
    with col1:
        st.write("Q" + str(k+1))
        st.write(qa['question'])
        
        st.markdown("""---""")
        
        st.success("ChatGPT score: " + str(chatgpt_score))
        st.warning("GPT-4 score: " + str(gpt4_score))
        st.error("Eevee score: " + str(alpaca_score))
          
          
    with col2:
      st.write("**ChatGPT** (API from Azure)")
      st.success(Azure)
      st.write("**GPT-4**")
      st.warning(gpt4)
      st.write("**Eevee**")
      st.error(alpaca)
      st.markdown("""---""")
  
    with col3:
        A60 = st.radio(
        "Rate Eevee:",
        ["0", "1", "2" ,"3" ,"4" ,"5" ,"6" ,"7" ,"8" ,"9", "10"],
        key=30*(note_number-1)+k,
        )
        
        A[note_number-1][k] = A60
  

username = st.text_input('Your username:', '')

import random
import string

# print('anonymous-'.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=5)))

submit =  st.button('Submit Your Selected Choices')
if submit:
    if username == '':
        username = 'anonymous-' + ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=5))
        st.error(f"Username not entered. Your assigned username is: {username}")
    else:
        st.write("Your username is: ", f"{username}")
    
#    with open('feedback.json') as json_file:
 #       feedback = json.load(json_file)

    feedback = {"username": username, "result": A}
    
    st.write("Your answer is ")
    st.write(pd.DataFrame(A))
    
    
    # with open('feedback.txt') as f:
      #   lines = f.readlines()
    
    with open('feedback.txt', 'r') as f:
        old_str = f.read()
        f.close()

    def dict_to_str(dict):
        output_str = '{'
        for key, value in dict.items():
            output_str += '"' + key + '": '
            if type(value) == str:
                output_str += '"' + value + '", '
            elif type(value) == list:
                output_str += '['
                for i in range(len(value)):
                    output_str += '['
                    for j in range(len(value[i])):
                        output_str += '"' + value[i][j] + '", '
                    output_str = output_str[:-2]
                    output_str += '], '
                output_str = output_str[:-2]
                output_str += '], '
        output_str = output_str[:-2]
        output_str += '}'
        return output_str

    data = old_str + "\n" + dict_to_str(feedback)
    # st.write(data)
    push_to_repo_branch("feedback.txt", data, "Yue-stat/visualize-QA", "main", "Yue-stat",st.secrets["token"])
    # push_to_repo_branch(username+".txt", A, "Yue-stat/visualize-QA", "main", "Yue-stat",st.secrets["token"])
    
    st.success("Sumbitted!")
else: 
    st.warning("Not submitted!")
    
st.markdown("<a href='#linkto_top'>Back to Top: Re-select Note</a>", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("<a href='#linkto_top'>Link to note</a>", unsafe_allow_html=True)
    st.markdown("<a href='#linkto_qa'>Link to QAs</a>", unsafe_allow_html=True)
    st.markdown("""---""")
    st.info(note)


    

