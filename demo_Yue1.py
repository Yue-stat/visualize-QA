# Yue Liu
import random

import pandas as pd
import streamlit as st


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
    "Select the clinical note. ", 1, 10, st.session_state["rn"]
)


st.write("You selected", f"{note_number}")

mtsamples = pd.read_json("demo.json")

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

st.write("You selected Question", f"{index + 1}")

Azure = ""
for answer in masked["paragraphs"][0]['qas'][index]['answers']:
     Azure += answer['text']

        


st.write("\n")
st.markdown("""---""")
st.write("\n")

st.write("**Azure**")
st.success(Azure)


gpt4 = "To add"

gpt4_result = ['''1. The patient's primary diagnosis is right groin pseudoaneurysm.''',
'''2. The following sentences describe the diagnosis: "Patient is a ___ year old female status post uterine artery fibroid embolization by ___ on ___ who was discharged ___ and around midnight awoke with right groin pain." "In the ED, patient was found by ultrasound to have a right groin pseudoaneurysm." "Patient was admitted for thrombin injection of pseudoaneurysm." "This is a ___ year old female with uterine fibroid embolization on ___ who presented with right groin pain and swelling determined by ultrasound to be a pseudoaneurysm." "Pseudoaneurysm: Patient presented with psuedoaneurysm confirmed by ultrasound that was secondary to her recent uterine fibroid embolization on ___. On ___ patient underwent psuedoaneurysm thrombin injection."
''',  '''3. The patient's comorbidities are Rheumatoid Arthritis and Irritable Bowel Syndrome.
''',  '''4. The following sentences describe the comorbidities: "Past Medical History:1. Rheumatoid Arthrits2. Irritable Bowel Syndrome." "3)Rheumatoid Arthritis:Stable during this admission. Patient was continued on outpatient regimen of prednisone and folate." "2) Constipation: Patient experienced constipation during this admission. Last bowel movement day prior to admission. Patient reports that she has irritable bowel syndrome with constipation at baseline."
''',  '''5. The medications mentioned in the discharge summary are Prednisone, Folate, Methotrexate, Culturale, Ibuprofen, Oxycodone, Colace, Senna, and Lactulose.
''',  '''6. The sentences in the note that describe the medications include:
- "Medications on Admission:1. Prednisone 5mg QDAY2. Folate 1 mg QDAY3. Methotrexate 10mg Q wk4. Culturale (probiotic) daily."
- "Discharge Medications:1. Prednisone 5 mg Tablet Sig...8. Oxycodone 5 mg Tablet Sig: ___ Tablets PO three times a day as needed for pain.Disp:*18 Tablet(s)* Refills:*0*"
- "You were started on the following new medications:**Ibuprofen 800 mg by mouth every 8 hours...**Lactulose 30mL by mouth twice a day as needed for constipation."
''',  '''7. No specific lab results or lab tests are mentioned in this discharge summary.
''',  '''
8. No sentences in the note describe the labs as no specific lab results or lab tests were mentioned in the discharge summary.
''',  '''
9. The treatment plan for the patient involved a thrombin injection into her right groin pseudoaneurysm. Post-procedure, her pain was managed with IV pain medication and anti-inflammatory medication, and transitioned to oral oxycodone and ibuprofen at discharge. For her constipation, worsened due to pain medications, she was started on a bowel regimen including colace, senna, and lactulose. Her stable rheumatoid arthritis continued to be managed with her outpatient regimen of prednisone and folate.
''',  '''
10. The sentences in the note that describe the treatment plan include:
- "On the floor, patient reported right groin pain of ___. She had no other complaints."
- "1) Pseudoaneurysm: Patient presented with pseudoaneurysm confirmed by ultrasound... She was given a prescription for oxycodone 5mg ___ tabs TID as needed for pain... She was also prescribed ibuprofen 800 mg PO TID to reduce inflammation and instructed to take this medication with food and water."
- "2) Constipation: Patient experienced constipation during this admission... Patient started on bowel regimen including colace, senna and lactulose... She will contact her primary care physician if she is unable to have a bowel movement within ___ hours of discharge."
- "3)Rheumatoid Arthritis: Stable during this admission. Patient was continued on outpatient regimen of prednisone and folate."
- "You came to the emergency department because you were having severe right sided groin pain... We treated your pain with IV pain medication and anti-inflammatory medication. Prior to discharge we transitioned you to oral pain medication which appropriately addressed your pain... We are discharging you with senna, colace and lactulose."
''',  '''
11. The identified problem of a right groin pseudoaneurysm was treated with a thrombin injection. Post-procedure, the patient experienced right groin and pelvic pain, which were managed initially with intravenous morphine, then transitioned to oral oxycodone at discharge. Ibuprofen was also prescribed to reduce inflammation. Additionally, the patient's constipation, a secondary problem during admission, was managed with a bowel regimen including Colace, Senna, and Lactulose, with instructions for follow-up if the issue persists.
''',  '''
12. The primary issue identified in this summary is a right groin pseudoaneurysm, which is likely caused by the patient's recent uterine artery embolization. As a result of the pseudoaneurysm and its subsequent treatment, the patient experienced severe pain, leading to the administration of narcotic pain medication. This medication likely contributed to the exacerbation of the patient's pre-existing condition of constipation during the hospital stay.
''',  '''
13. The patient's discharge medications include Prednisone 5 mg, Folic Acid 1 mg, Methotrexate Sodium 10 mg, Ibuprofen 800 mg, Colace 100 mg, Senna 8.6 mg, Lactulose 10 gram/15 mL Solution, and Oxycodone 5 mg.
''',  '''
14. The patient's diagnoses include a right groin pseudoaneurysm (primary discharge diagnosis), Rheumatoid Arthritis (past medical history), Irritable Bowel Syndrome (past medical history), Bicuspid Aortic Valve (past medical history), and Constipation (diagnosed during recent admission). 
''',  '''
15. The primary discharge diagnosis for this patient is a right groin pseudoaneurysm.
''',  '''
16. The medications prescribed to the patient at discharge are Prednisone 5mg daily, Folic Acid 1mg daily, Ibuprofen 800mg every eight hours for seven days, Methotrexate Sodium 10mg once a week, Colace 100mg twice a day as needed for constipation, Senna 8.6mg once a day as needed for constipation, Lactulose 10 gram/15 mL twice a day, and Oxycodone 5mg three times a day as needed for pain.
''',  '''
17. The patient, a woman with a history of uterine fibroid embolization, was admitted due to right groin pain and swelling. An ultrasound confirmed a pseudoaneurysm in her right groin, which was treated with thrombin injection. Post-procedure, the patient experienced pain in the right groin and pelvis, managed with pain and anti-inflammatory medication. She also experienced constipation, which was managed with a bowel regimen and prescribed medication for at-home use.
''',  '''
18. The specific date of the patient's thrombin injection for the pseudoaneurysm is not provided in the discharge summary.
''',  '''
19. Yes, there is a relationship between the patient's irritable bowel syndrome (IBS) and her constipation during this admission. The patient's baseline IBS already includes constipation, and this was likely exacerbated by the narcotic pain medication she received during her hospital stay.
''',  '''
20. The key symptoms the patient experienced prior to presenting to the ED were right groin pain, noticeable swelling in her right groin that felt firm, an increase in the size of the swelling, pain radiating across her lower abdomen causing significant discomfort, and difficulty straightening her right leg due to pain.
''',  '''
21. The standard medical term for "Bicuspid aortic valve" is "Bicuspid aortic valve". It is already a standard medical term, indicating a congenital heart defect where the aortic valve only has two leaflets instead of the usual three.
''',  '''
22. "TTE" stands for "Transthoracic Echocardiogram". It is a type of heart ultrasound that views the structure and function of the heart through the chest wall.
''',  '''
23. Key features of the patient's physical exam are:
   - Vitals: T: 98.4, BP:96/60, P: 63, R:18, O2: 98% on room air
   - General condition: Alert, oriented, no acute distress
   - HEENT: Sclera anicteric, moist mucous membranes, oropharynx clear
   - Neck: supple, Jugular venous pressure not elevated, no lymphadenopathy
   - Lungs: Clear to auscultation bilaterally, no wheezes, rales, or ronchi
   - CV: Regular rate and rhythm, normal S1 + S2, no murmurs, rubs, gallops
   - Abdomen: soft, non-tender, non-distended, bowel sounds present, no rebound tenderness or guarding, no organomegaly
   - Extremities: Warm, well perfused, 2+ pulses, no clubbing, cyanosis or edema
   - Right Groin: Appears slightly swollen, no erythema, positive bruit auscultated, positive tenderness to palpation.
''',  '''
24. The surgical procedures the patient has undergone in the past include:
   - Bilateral knee arthroscopy
   - Bilateral Metatarsal surgery
''',  '''
25. 
Dear Patient,

We would like to inform you about your new prescribed medications and how to properly take them:

1. **Ibuprofen 800 mg**: Please take one tablet by mouth every 8 hours. This medication is meant to reduce inflammation and alleviate pain. Make sure to take this with food and water as it can cause stomach irritation.

2. **Oxycodone 5mg-10 mg**: Take this by mouth three times per day as needed for pain. This medication can cause constipation, so you may need to take a stool softener. Remember not to drive or operate heavy machinery while on this medication due to its potential sedative effect.

3. **Colace 100 mg**: To help prevent constipation, take one capsule by mouth twice daily as needed.

4. **Senna**: As a laxative, you can take one tablet daily if needed for constipation.

5. **Lactulose 30mL**: This liquid can be taken twice a day by mouth as needed for constipation.

Please remember to take these medications as directed and reach out to your healthcare provider if you experience any side effects or have further questions.

Best Regards,
Your Healthcare Team.
''',  '''
26. No clear relationship is documented between the patient's rheumatoid arthritis and her pseudoaneurysm in the discharge summary.
''',  '''
27. The patient was discharged home.
''',  '''
28. The prescribed oxycodone is to be taken as needed for pain, with a dosage of 5 mg per tablet, up to three times a day.
''',  '''
29. The patient is a woman who had a procedure for uterine fibroids. After she was discharged, she woke up around midnight with pain and swelling in her right groin, which was also hard to touch. This pain spread across her lower belly, causing her severe discomfort and trouble straightening her right leg. She was directed to the emergency department, where it was found that she had a pseudoaneurysm in her right groin. She was then admitted to the hospital for a treatment to clot the pseudoaneurysm.
''',  '''
30. The discharge summary does not provide specific laboratory values obtained during the patient's admission.
''']

if note_number == 1:
    gpt4 = gpt4_result[index]
    
st.write("**GPT-4**")
st.warning(gpt4)

# st.write("**Alpaca**")
# st.error(alpaca)



