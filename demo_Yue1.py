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
    "Select the clinical note. :smile:", 1, 10, st.session_state["rn"]
)


st.write("You selected", f"{note_number}")

mtsamples = pd.read_json("demo.json")

masked = mtsamples["data"][note_number-1]

note = masked["paragraphs"][0]['context']

q_list = []
for k, qa in enumerate(masked["paragraphs"][0]['qas']):
    q_list.append(qa['question'])
   
st.info(note)

instruction = st.selectbox("Select your instruction. :smile:", q_list)

def find_loc(string, list):
    for i in range(len(list)):
        if string in list[i]:
            return i
          
          

index = find_loc(instruction, q_list)

st.write("You selected Question", f"{index + 1}")

Azure = ""
for answer in masked["paragraphs"][0]['qas'][index]['answers']:
     Azure = Azure + "; " + answer['text']
Azure = Azure[2:]
        


st.write("\n")
st.markdown("""---""")
st.write("\n")

st.write("**ChatGPT** (API from Azure)")
st.success(Azure)


gpt4 = "To add"

gpt4_0 = ['''1. The patient's primary diagnosis is right groin pseudoaneurysm.''',
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

gpt4_1 = [
'''1. The patient's primary diagnosis is acute right lower extremity (RLE) Deep Vein Thrombosis (DVT).
''',
'''
2. The sentences in the note that describe the diagnosis are: "Ms. ___ is a ___ PMHx advanced Alzheimer's dementia, chronic HCV, autoimmune hepatitis, and AFib who presents from her SNF for RLE DVT.", "DVT. Diagnosed by LENIs at ___. Patient started on Lovenox in ED for anticoagulation.", and "Patient admitted for evaluation of acute RLE DVT."
''',
'''
3. The comorbidities of the patient include advanced Alzheimer's dementia, chronic Hepatitis C virus (HCV) infection, autoimmune hepatitis, Atrial fibrillation (AFib), and atypical meningioma.
''',
'''
4. The sentences in the note that describe the comorbidities are: "Ms. ___ is a ___ PMHx advanced Alzheimer's dementia, chronic HCV, autoimmune hepatitis, and AFib who presents from her SNF for RLE DVT.", "Her course at the time was also notable for new paroxysmal AFib", "Asymptomatic bacteriuria: UA was positive and she was initially given antibiotics.", "Atypical meningioma. Recently seen on brain MRI in ___.", "# A. fib. Recent diagnosis of paroxysmal AFib.", "# Autoimmune hepatitis. - Continued home prednisone", "# Alzheimer's dementia. At baseline.- Continued home donepezil and memantine".
''',
'''
5. The medications mentioned in the discharge summary include Aspirin, Donepezil, Levetiracetam (Keppra), Memantine, Multivitamins with minerals, Nifedipine, Prednisone, and Vitamin E.
''',
'''
6. The sentences in the note that describe the medications are: "Patient at the time was placed on Keppra for seizure prophylaxis.", "Autoimmune hepatitis. - Continued home prednisone", "Hypertension. Stable.- Continued home nifedipine", "Alzheimer's dementia. At baseline.- Continued home donepezil and memantine", "The Preadmission Medication list is accurate and complete.", and "Please resume all previous medications".
''',
'''
7. The labs mentioned in the discharge summary include: glucose, urea N, creatinine, sodium, potassium, chloride, total CO2, anion gap, lactate, WBC, RBC, hemoglobin, hematocrit, MCV, MCH, MCHC, RDW, RDWSD, Neutrophils, Monocytes, Eosinophils, Basophils, Platelet Count, PTT, Urine Color, Urine Appearance, Urine Blood, Nitrite, Protein, Glucose, Ketone, Bilirubin, Urobilinogen, PH, Leukocytes, RBC in urine, WBC in urine, Bacteria in urine, Yeast in urine, and Epithelial Cells in urine.
''',
'''
8. The sentences in the note that describe the labs are: "Initial labs were unremarkable", "UA was grossly positive and the patient was given IV ceftriaxone", "Pertinent Results: ADMISSION LABS... ", "IMAGING/STUDIES... RLE DVT FINDINGS".
''',
'''
9. The treatment plan for the patient includes placement of an Inferior Vena Cava (IVC) filter due to her high risk for bleeding from an atypical meningioma and newly diagnosed RLE DVT. Anticoagulation treatment was deferred due to her age, risk of falls, and high risk of bleeding from her meningioma. She was continued on her home medications which include Aspirin, Donepezil, Memantine, Nifedipine, Prednisone, Multivitamins with minerals, Vitamin E, and Levetiracetam.
''',
'''
10. The sentences in the note that describe the treatment plan are: "After discussion with HCP... decision made to place IVC filter and NOT anti coagulate given the patient's high risk for bleeding", "She went for uncomplicated IVC filter placement on...", "She will not be anti coagulated going forward", "Thus antibiotics were stopped", "Continued Keppra 500 mg BID", "Continued home prednisone", "Continued home nifedipine", "Continued home donepezil and memantine".
''',
'''
11. The identified problem is the patient's high risk for bleeding due to her atypical meningioma and newly diagnosed RLE DVT. The subsequent treatment plan, which is the placement of an IVC filter and the avoidance of anticoagulation, is directly related to managing this risk.
''',
'''
12. The two major problems identified in this discharge summary are the atypical meningioma and the RLE DVT. The atypical meningioma contributes to a high risk for bleeding which directly influenced the decision to place an IVC filter for the RLE DVT rather than the typically used systemic anticoagulation treatment. This is a clear causal relationship where the presence of one condition (atypical meningioma) influenced the treatment of another condition (RLE DVT).
''',
'''
13. The patient is currently on the following medications: Aspirin (81 mg daily), Donepezil (10 mg at bedtime), Levetiracetam (500 mg twice daily), Memantine (21 mg daily), Multivitamins with minerals (1 tablet daily), Nifedipine CR (30 mg daily), Prednisone (5 mg daily), and Vitamin E (400 units daily).
''',
'''
14. The patient has been diagnosed with Acute Right Lower Extremity (RLE) Deep Vein Thrombosis (DVT), Alzheimer's dementia, Autoimmune hepatitis, and Hepatitis C Virus (HCV) infection. The diagnosis of Acute RLE DVT occurred during the recent onsite visit, while Alzheimer's dementia, Autoimmune hepatitis, and HCV infection are part of the patient's past medical history. The patient also has a recently diagnosed atypical meningioma from a previous onsite visit. 
''',
'''
15. The patient's chief complaint can be classified under the category of 'Vascular Issues', specifically Deep Vein Thrombosis (DVT) in the Right Lower Extremity (RLE).
''',
'''
16. The patient has an allergy to Codeine.
''',
'''
17. The discharge summary does not specify an exact date for the diagnosis of the patient's atypical meningioma. It was mentioned that it was "recently seen on brain MRI", however, the exact timing is not provided in the summary.
''',
'''
18. Yes, there is a relationship between the patient's Alzheimer's dementia and her Activities of Daily Living (ADL) impairment. As a result of her Alzheimer's, she is impaired in preparing food, remembering to bathe, and recalling faces, which are all essential daily living activities. She lives at home but requires extensive support.
''',
'''
19. The keywords related to the patient's medical history include: Alzheimer's dementia, chronic HCV (Hepatitis C virus), autoimmune hepatitis, atrial fibrillation (AFib), RLE (Right Lower Extremity) DVT (Deep Vein Thrombosis), atypical meningioma, asymptomatic bacteriuria, hypertension, and seizure activity.
''',
'''
20. The patient has a blood clot in the right lower leg, Alzheimer's disease, a liver condition caused by the immune system (autoimmune hepatitis), Hepatitis C virus infection, high blood pressure, an irregular heart rhythm (atrial fibrillation), and a non-typical growth in the lining of the brain and spinal cord (atypical meningioma).
''',
'''
21. The patient has a history of advanced Alzheimer's disease, which affects her ability to remember and recognize people, and prepare food. She also has a low viral load of chronic Hepatitis C and autoimmune hepatitis. She has been diagnosed with an irregular heart rhythm, known as atrial fibrillation, but has not been put on anticoagulants due to her high risk of bleeding, age, and the risk of falls. She also has a non-typical brain tumor, or meningioma. 
''',
'''
22. The features identified in the patient's physical exam include: normal vital signs, alertness, no acute distress, clear eyes and throat, regular heart rate, clear lung sounds, a soft and distended abdomen with normal bowel sounds, warm extremities with good blood flow and sensitivity, normal psychological and dermatological state.
''',
'''
23. The term "LENIs" is not a standard abbreviation in medicine and may be a typo or a specific term used in the facility where this report was produced. Without further context, it's unclear what "LENIs" stands for in this discharge summary.
''',
'''
24. The medications mentioned in the discharge summary include: Aspirin, Donepezil, Memantine, NIFEdipine, PredniSONE, Vitamin E, LevETIRAcetam, Multivitamins with minerals, and Lovenox (used once in the ED).
''',
'''
25. No, the patient was not started on anticoagulation for her RLE DVT due to her high risk of bleeding.
''',
'''
26. The term "paroxysmal AFib" stands for Paroxysmal Atrial Fibrillation. This is the standard medical term for a condition characterized by irregular heartbeats in the atria that start and stop abruptly.
''',
'''
27. The patient's discharge condition could be classified as "stable but confused." She was alert and interactive but was always confused, which aligns with her diagnosis of advanced Alzheimer's dementia.
''',
'''
28. The patient, having a complex medical history including advanced Alzheimer's dementia, chronic HCV, autoimmune hepatitis, and AFib, presented with right lower extremity pain which was diagnosed as DVT. Due to her high bleeding risk related to an atypical meningioma, she underwent an IVC filter placement rather than anticoagulation. Additionally, she was found to have asymptomatic bacteriuria but was not treated with antibiotics as she had no symptoms suggestive of a UTI. She continued her home medications for her ongoing conditions.
''',
'''
29. The discharge summary does not provide specific contact information for the patient.
''',
'''
30. The patient's past medical history includes advanced Alzheimer's dementia, with impairment in preparing food, remembering to bathe, and recalling faces. She also has chronic Hepatitis C Virus infection with a low viral load, autoimmune hepatitis, hypertension, and an atypical meningioma. She had been living at home with extensive support.
'''
]

gpt4_2 = [
'''1. The primary diagnosis for the patient is the recurrence of right breast cancer.
''',
'''
2. The sentences describing the diagnosis are: "Chief Complaint:___ yo woman with history of breast CA, s/p lumpectomy and XRT ___ years ago; now with new primary cancer in same right breast" and "Discharge Diagnosis: Right breast cancer recurrence".
''',
'''
3. No explicit comorbidities are mentioned in the patient's discharge summary.
''',
'''
4. No sentences in the note describe any comorbidities as none are specified.
''',
'''
5. The medications mentioned in the discharge summary include: Flonase, Acyclovir, Aspirin, Acetaminophen, Docusate Sodium (Colace), Cefadroxil, Mupirocin Calcium (Bactroban), Hydromorphone (Dilaudid), Magnesium Hydroxide, Senna, and Bisacodyl.
''',
'''
6. The sentences that describe the medications are: "Medications on Admission: Flonase Acyclovir", "Discharge Medications: 1. Aspirin 81 mg Tablet, Chewable Sig: 1.5 Tablet, Chewables PO DAILY (Daily)... 6. Hydromorphone 2 mg Tablet Sig: One (1) Tablet PO every six (6) hours as needed for pain...", and "Medications: 1. Resume your regular medications unless instructed otherwise and take any new meds as ordered...7. Do not drive or operate heavy machinery while taking any narcotic pain medication. You may have constipation when taking narcotic pain medications (oxycodone, percocet, vicodin, hydrocodone, dilaudid, etc.); you should continue drinking fluids, you may take stool softeners, and should eat foods that are high in fiber."
''',
'''
7. The labs mentioned in the discharge summary are WBC, RBC, Hgb, Hct, MCV, MCH, MCHC, RDW, and Plt.
''',
'''
8. The sentence that describes the labs in the note is: "___ 05:17AM BLOOD WBC-9.7# RBC-4.09* Hgb-12.1 Hct-35.9* MCV-88 MCH-29.6 MCHC-33.7 RDW-12.8 Plt ___".
''',
'''
9. The treatment plan for the patient consisted of a right mastectomy and immediate deep inferior epigastric perforator flap breast reconstruction for a new primary breast cancer in the same right breast where she had a history of cancer. Post-operatively, she received morphine for pain control and was transitioned to oral dilaudid when she could tolerate oral intake. She was given IV fluids until she could tolerate oral intake, after which her diet was advanced. She was also started on a bowel regimen. She received IV cefazolin post-operatively, which was later switched to oral cefadroxil. Prophylactically, she was given subcutaneous heparin and encouraged to ambulate. Her reconstructed area was monitored for oxygenation and blood flow, and an area of ischemic, blistering tissue was treated with Bactroban cream.
''',
'''
10. The sentences in the note that describe the treatment plan are spread throughout the text under "Brief Hospital Course" and "Discharge Medications". 
''',
'''
11. The identified problem was a recurrence of breast cancer in the same right breast where the patient had a history of cancer. The subsequent treatment plan consisted of a mastectomy and immediate deep inferior epigastric perforator flap breast reconstruction for the new primary cancer. Pain control, infection control, hydration, and encouraging bowel movement were part of the post-operative care plan.
''',
'''
12. The diagnoses mentioned in the note are breast cancer recurrence, which is the recent onsite diagnosis from this hospital visit, and a history of breast cancer, which is from the patient's past medical history.
''',
'''
13. The patient's discharge medications include Aspirin (81mg, chewable), Acetaminophen (325mg), Docusate Sodium (100mg capsule), Cefadroxil (500mg capsule), Mupirocin Calcium (2% cream), Hydromorphone (2mg tablet), Magnesium Hydroxide (400mg/5 mL suspension), Senna (8.6mg tablet), and Bisacodyl (5mg tablet, delayed release).
''',
'''
14. The recent diagnosis from an onsite visit is a recurrence of right breast cancer. The past medical history includes breast cancer, for which the patient had previously undergone lumpectomy and radiation therapy.
''',
'''
15. The primary diagnosis for the patient is the recurrence of right breast cancer.
''',
'''
16. The patient has an allergy to Sulfa (Sulfonamide Antibiotics).
''',
'''
17. The exact time of the patient's previous lumpectomy and radiation treatment isn't specified in the discharge summary. The summary simply indicates that it took place 'years ago'.
''',
'''
18. The patient's family history includes instances of various types of cancer (breast cancer in a maternal grandmother and a second cousin, non-Hodgkin's lymphoma in a maternal aunt, bladder cancer in a maternal uncle, and brain cancer in an uncle) but there's no direct evidence of a genetic relation to the patient's diagnosis of breast cancer. However, a genetic predisposition cannot be ruled out without further genetic testing.
''',
'''
19. The patient, a female with a history of breast cancer and a new lesion in her right breast, was admitted to the plastic surgery service. She underwent a right mastectomy and immediate deep inferior epigastric perforator flap breast reconstruction. Post-operatively, her pain was managed with morphine and later oral dilaudid. She received IV fluids until tolerating oral intake, and a bowel regimen was initiated. She was monitored for signs of infection and provided with subcutaneous heparin as a prophylactic measure. A Vioptix oximeter was used to ensure adequate tissue oxygenation post-surgery. She developed some ischemic, blistering tissue at the reconstructive site during her stay, which was managed with Bactroban cream. She was discharged on post-operative day 5 in a stable condition.
''',
'''
20. The patient appears well-nourished and in no distress. HEENT examination was normal. There was some bruising on her upper back from an acupuncture site, but otherwise, her skin was unremarkable. Her lymph nodes were also unremarkable. Her right breast was slightly smaller than the left, with a well-healed lumpectomy incision at the periareolar location. An area of firmness was palpable below this incision. The rest of her breasts were without abnormal masses or lesions. Her abdomen was soft and without obvious masses, hernias, or hepatosplenomegaly. Her lungs and extremities were normal.
''',
'''
21. "POD" stands for "Post-Operative Day".
''',
'''
22. The patient's bra size is 38C, and she is indeed interested in deep inferior epigastric perforator flap breast reconstruction. She prefers the reconstruction to result in a slightly smaller size than her current one.
''',
'''
23. The patient's vital signs were stable throughout her stay, though specific measurements are not mentioned in the summary. Her blood work results show a white blood cell count of 9.7, red blood cell count of 4.09, hemoglobin of 12.1, hematocrit of 35.9, mean corpuscular volume of 88, mean corpuscular hemoglobin of 29.6, mean corpuscular hemoglobin concentration of 33.7, red cell distribution width of 12.8, and platelets count is not specified.
''',
'''
24. The patient was prescribed several medications upon discharge: Aspirin, Acetaminophen, Docusate Sodium, Cefadroxil, Mupirocin Calcium, Hydromorphone, Magnesium Hydroxide, Senna, and Bisacodyl. Prior to admission, she was on Flonase and Acyclovir.
''',
'''
25. The patient underwent a right mastectomy with immediate flap reconstruction, and her current medication regimen does appear to relate to this procedure. Post-surgery, she was given morphine for pain management, which was later switched to oral dilaudid. She was also given IV cefazolin and later switched to oral cefadroxil for a week after discharge to prevent infection. 
''',
'''
26. To take care of the drain, cleanse your hands well with soap and warm water before you start. Empty the fluid from the drain into a measuring cup twice a day, preferably at the same time each day. Keep track of the volume of fluid on a record sheet. After you've emptied it, make sure to reestablish suction in the drainage bottle.
''',
'''
27. The patient has a past medical history of breast cancer. She underwent lumpectomy and radiation therapy before being diagnosed with a new primary cancer in the same breast.
''',
'''
28. The patient's right breast shows a well-healed lumpectomy incision near the top of the areola. A firm area can be felt beneath this incision. There are no other abnormal masses or lesions, and there is no tenderness. The right breast is a bit smaller than the left. The distance from the sternal notch to the nipple is 25 cm on the right and 27.5 cm on the left, and the distance from the inframammary fold to the nipple is 11 cm on the right and 12 cm on the left.
''',
'''
29. Yes, the patient's post-operative pain was effectively managed.
''',
'''
30. Some of the medical abbreviations and terms in the summary are:
- "s/p": status post, indicating a procedure that has occurred in the past.
- "XRT": radiation therapy.
- "PO": per os, taken orally.
- "BID": bis in die, twice a day.
- "PCA": patient-controlled analgesia, a method of pain control that allows the patient to control their own medication.
- "POD": postoperative day, the number of days since the surgery.
- "WBC": white blood cell.
- "RBC": red blood cell.
- "Hgb": Hemoglobin.
- "Hct": Hematocrit.
- "MCV": Mean corpuscular volume.
- "MCH": Mean corpuscular hemoglobin.
- "MCHC": Mean corpuscular hemoglobin concentration.
- "RDW": Red cell distribution width.
- "Plt": Platelet.
'''
]

gpt4_3 = [
    '''1. The patient's primary diagnosis is bilateral Pulmonary Embolism (PE) and lower extremity Deep Venous Thrombosis (DVT).
''',
'''
2. The following sentences in the note describe the diagnosis: "The patient is a ___ year old male who reports that last evening he became suddenly SOB, sweaty, and clammy..."; "At the OSH patient thought to have large bilateral PE's and trop of 0.32."; "There are large pulmonary emboli involving the main pulmonary arteries extending in the bilateral upper lobes, right middle lobe, and bilateral lower lobes."; "Positive for pulmonary emboli with large clot burden."; "Left deep venous thrombus within the proximal femoral vein extending to the popliteal vein, nonocclusive."; "Right popliteal deep venous non occlusive thrombus."; and "Patient noted to have bilateral pulmonary embolism noted at outside hospital to have bilateral pulmonary embolism."
''',
'''
3. The patient's comorbidities include Chronic Low Back Pain, Deep Venous Thrombosis (DVT), Degenerative Joint Disease, Type I Diabetes, and Hyperlipidemia.
''',
'''
4. These sentences describe the comorbidities: "He also endorses chronic back pain in his lumbar spine that is currently ___.", "Past Medical History: CHRONIC LOW BACK PAIN DEEP VENOUS THROMBOSIS DEGENERATIVE JOINT DISEASE DIABETES TYPE I HYPERLIPIDEMIA.", "Patient continued on ISS and daily lantus and humalog.", "Patient continued on simvastatin 40 mg daily.", and "Patient with chronic low back pain. He was continued on tramadol 50 mg daily."
''',
'''
5. The medications mentioned in the discharge summary are Tramadol, Metformin, Humalog (insulin lispro), Simvastatin, Gabapentin, Rivaroxaban (Xarelto), and Aspirin.
''',
'''
6. These sentences in the note describe the medications: "The patient was started on tPA protocol... then continued on 20 mg xarelto daily.", "Patient continued on ISS and daily lantus and humalog. Metformin held. Gabapentin 100 mg TID continued.", "Patient continued on simvastatin 40 mg daily.", "Patient with chronic low back pain. He was continued on tramadol 50 mg daily.", and "Medications on Admission...Discharge Medications."
''',
'''
7. The labs mentioned in the discharge summary include troponin levels, hematology/oncology workup for Factor V Leiden and antiphospholipid syndrome, and labs on admission and discharge. Specific results are not provided for the latter two.
''',
'''
8. There are several mentions of labs in the discharge summary:
- "At the OSH patient thought to have large bilateral PE's and trop of 0.32."
- "Plan for outpatient follow up with Hem/Onc to address hypercoagulable work up with Factor V Leiden and antiphospholipid syndrome."
- "LABS ON ADMISSION:"
- "LABS ON DISCHARGE:"
''',
'''
9. The treatment plan for the patient involved management of bilateral pulmonary embolisms, hypoxia, Type II Diabetes with peripheral neuropathy, Hyperlipidemia (HLD), and chronic low back pain. The pulmonary embolisms were treated with tPA for thrombolysis and then rivaroxaban (Xarelto). The hypoxia was thought to be secondary to the pulmonary embolisms and was treated with home oxygen. The diabetes and neuropathy were managed with insulin and gabapentin. Hyperlipidemia was treated with simvastatin, and the chronic low back pain was managed with tramadol. The patient was to have outpatient follow up with Hematology/Oncology for further testing for Factor V Leiden Deficiency.
''',
'''
10. The sentences describing the treatment plan include:
- "The patient was started on tPA protocol as follows: tPA 10mg IV over 1 minute then 40mg over 2 hours with continued Unfractionated heparin at 1000u/hour with transition to weight based heparin until therapeutic."
- "Following this, the patient was started on xarelto 15 mg BID on ___ for 3 weeks and then continued on 20 mg xarelto daily."
- "The patient was discharged with home oxygen requirement for sleep and ambulation."
- "Patient continued on ISS and daily lantus and humalog. Metformin held. Gabapentin 100 mg TID continued."
- "Patient continued on simvastatin 40 mg daily."
- "Patient with chronic low back pain. He was continued on tramadol 50 mg daily."
- "Follow up with Hem/Onc as outpatient with work up for Factor V Leiden Deficiency."
''',
'''
11. The identified problem was the presence of bilateral pulmonary embolisms, and the subsequent treatment plan was to administer tPA for thrombolysis and rivaroxaban (Xarelto) as a prophylactic anticoagulant. Furthermore, the hypoxia was believed to be secondary to the pulmonary embolisms, leading to the provision of home oxygen for the patient.
''',
'''
12. Two major problems identified in this discharge summary are the bilateral pulmonary embolisms and the associated hypoxia. The causal relationship between these two issues is that the bilateral pulmonary embolisms likely led to the hypoxia due to impaired oxygen exchange in the lungs.
''',
'''
13. The patient is currently on the following medications: Gabapentin 100 mg PO BID, Humalog insulin lispro with varying units subcutaneous TID, Simvastatin 40 mg PO daily, Tramadol (Ultram) 50 mg PO TID PRN for back pain, Rivaroxaban 15 mg PO BID then 20 mg daily, Metformin (Glucophage) 1000 mg PO BID, and Aspirin EC 81 mg PO daily. The patient was also discharged with an Oxygen requirement.
''',
'''
14. The patient was diagnosed onsite with Pulmonary embolism (bilateral) and Lower extremity Deep Vein Thrombosis (DVT). From their past medical history, the patient has Chronic Low Back Pain, Deep Venous Thrombosis, Degenerative Joint Disease, Type I Diabetes, and Hyperlipidemia.
''',
'''
15. The patient's primary diagnosis is Bilateral Pulmonary Embolism, as confirmed during their recent onsite visit.
''',
'''
16. The patient has allergies to Penicillins and Ibuprofen.
''',
'''
17. The patient started taking Rivaroxaban (Xarelto) during their hospital stay. The recommended dosage is 15 mg twice daily with food for the first three weeks, and then 20 mg once daily indefinitely.
''',
'''
18. Based on the provided information, there is no direct relation between the patient's chronic low back pain and their pulmonary embolism. The back pain may contribute to the patient's overall discomfort and limited mobility, but it's not listed as a causative factor for the pulmonary embolism.
''',
'''
19. The patient's mother had numerous clots throughout her life, starting to develop deep vein thrombosis (DVTs) at a certain age. She was later diagnosed with pancreatic cancer and subsequently passed away from it. 
''',
'''
20. The patient, a man of unspecified age, complained of sudden onset of difficulty breathing, excessive perspiration, and feeling cold the previous night. He also experienced pain in his back, which he attributed to his lungs, and began to feel weakness in both his lower legs the next day. In addition to these symptoms, he has a consistent tingling sensation in his right leg due to peripheral neuropathy.
''',
'''
21. Two weeks before his hospital visit, the patient went on a three-hour car trip, but he has not traveled recently beyond that. 
''',
'''
22. The physical examination revealed the patient to be anxious and suffering from tachycardia. His oxygen saturation was at 90% even while on a non-rebreather and 6L nasal cannula. There was trace edema to mid-shins bilaterally and an abnormal sensation in the right lower extremity due to neuropathy. At discharge, the patient still showed tachycardia and needed oxygen support with 4L nasal cannula.
''',
'''
23. The patient was admitted with sudden shortness of breath and was found to have bilateral pulmonary embolisms and deep venous thrombosis in his legs. He was transferred to the critical care unit for thrombolysis, where he was treated with tissue plasminogen activator (tPA) and heparin, followed by rivaroxaban. His oxygen requirement and shortness of breath were attributed to the pulmonary embolisms. His diabetes was managed with insulin and metformin, his hyperlipidemia with simvastatin, and his chronic back pain with tramadol. Upon discharge, the patient was prescribed home oxygen for sleep and exertion.
''',
'''
24. SOB: Shortness of Breath, PE: Pulmonary Embolism, OSH: Outside Hospital, DVT: Deep Venous Thrombosis, CCU: Critical Care Unit, tPA: Tissue Plasminogen Activator, ISS: Insulin Sliding Scale, BID: Twice a Day, TID: Three Times a Day, EC: Enteric Coated, HL: Hyperlipidemia, RA: Room Air.
''',
'''
25. The medications mentioned in the patient's history include: TraMADOL (Ultram), MetFORMIN (Glucophage), HumaLOG (insulin lispro), Simvastatin, Gabapentin, and Rivaroxaban (Xarelto), Aspirin.
''',
'''
26. The patient's current oxygen requirement is for sleep and ambulation. They require this due to their condition of bilateral pulmonary embolisms, which has caused hypoxia.
''',
'''
27. Yes, there is a direct relation between the patient's hypoxia and their pulmonary embolism. The pulmonary embolisms have likely resulted in reduced oxygen levels (hypoxia) in the patient's blood.
''',
'''
28. The patient, a ___ year old male, was admitted after presenting with shortness of breath. Upon examination, he was found to have bilateral pulmonary embolism and deep venous thrombosis in the lower extremities. He underwent thrombolysis and was started on a regimen of Rivaroxaban (Xarelto) and Aspirin. His hypoxia was managed with home oxygen requirement for sleep and ambulation. His diabetes and hyperlipidemia were managed with the continuation of his preadmission medications. The patient's condition improved and he was discharged home.
''',
'''
29. Here are a few normalized clinical concepts mentioned in the summary: 
- Bilateral Pulmonary Embolism: Pulmonary Embolism (SNOMED CT: 415117006)
- Hypoxia: Hypoxia (SNOMED CT: 389086008)
- Type I Diabetes: Type 1 Diabetes Mellitus (SNOMED CT: 46635009)
- Chronic Lower Back Pain: Chronic Low Back Pain (SNOMED CT: 278040002)
- Hyperlipidemia: Hyperlipidaemia (SNOMED CT: 55822004)
''',
'''
30. Yes, the patient was discharged with a new medication, Rivaroxaban (Xarelto), which is an anticoagulant prescribed due to the patient's condition of bilateral pulmonary embolism and deep venous thrombosis.
'''
]

gpt4_4 = [
'''1. (Text Summarization) The patient's primary diagnosis was Acute hypoxemic respiratory failure secondary to parainfluenza 3 pneumonia.
''',
'''
2. (Content extraction) The sentences in the note that describe the diagnosis include:
- "The patient has remained profoundly hypoxemic despite broad abx coverage and diuresis, and he was found to have an elevated B-glucan and LDH, as well as NP swab positive for parainfluenza."
- "During his course developed worsening acidosis, hyponatremia, and altered mental status."
- "Time of death 00:15. Cause of death: parainfluenza pneumonia."
- "Discharge Diagnosis:Acute hypoxemic respiratory failure secondary to parainfluenza 3 pneumoniaAcute on chronic diastolic heart failureDeep vein thrombosisAtrial fibrillationRheumatoid arthritisOsteomyelitis"
''',
'''
3. The comorbidities of the patient, as mentioned in the discharge summary, include:

 Rheumatoid arthritis
 Chronic kidney disease stage 3
 Chronic back pain
 Hypertension
 Hyperlipidemia
 Type II diabetes mellitus
''',
'''
4. (Content extraction) The sentences in the note that describe the comorbidities are:

- "The patient is a 67-year-old female with a history of rheumatoid arthritis, chronic kidney disease stage 3, chronic back pain, hypertension, hyperlipidemia, and type II diabetes mellitus."
- "She was initially admitted with osteomyelitis of the spine secondary to Enterococcus bacteremia."
  ''',
'''
5. (Named Entity Recognition) The medications mentioned in the discharge summary are:

- Intravenous antibiotics
- Oxycodone
- Lisinopril
- Amlodipine
- Gabapentin
- Metformin
  ''',
'''
6. (Content extraction) The sentences in the note that describe the medications are:

- "She completed 6 weeks of intravenous antibiotics for Enterococcus bacteremia and osteomyelitis."
- "Her medications on discharge included oxycodone for pain, Lisinopril, Amlodipine for hypertension, gabapentin for neuropathic pain, and metformin for diabetes."
''',
'''
7. (Named Entity Recognition) The labs mentioned in the discharge summary include:

- Creatinine levels
- ESR (Erythrocyte Sedimentation Rate)
- CRP (C-Reactive Protein)
''',
'''
8. (Content extraction) The sentence in the note that describes the labs is: "She had stable creatinine levels and downward trending inflammatory markers (ESR, CRP)."
''',
'''
9. (Text Summarization) The treatment plan for the patient includes continuing her home medications for comorbid conditions, along with periodic lab monitoring. She should follow-up with the infectious disease department in one week to ensure that her Enterococcus bacteremia and osteomyelitis are being managed properly.
''',
'''
10. (Content extraction) The sentences in the note that describe the treatment plan are:

- "Her medications on discharge included oxycodone for pain, Lisinopril, Amlodipine for hypertension, gabapentin for neuropathic pain, and metformin for diabetes."
- "She is to follow up with the infectious disease department in 1 week."
- "She will also have lab work in 1 week to check her creatinine levels and inflammatory markers."

''',
'''
11. The identified problem of the patient is severe sepsis secondary to Enterococcus bacteremia from Osteomyelitis with SIRS criteria. The treatment plan related to this problem includes aggressive fluid resuscitation, intravenous antibiotics (Vancomycin and Ceftriaxone), as well as management of hyperglycemia with insulin.
''',
'''
12. The patient's diagnoses are:
   - Severe sepsis secondary to Enterococcus bacteremia from Osteomyelitis with SIRS criteria (recent onsite visit)
   - Rheumatoid arthritis (past medical history)
   - Chronic kidney disease stage 3 (past medical history)
   - Chronic back pain (past medical history)
   - Hypertension (past medical history)
   - Hyperlipidemia (past medical history)
   - Type II diabetes mellitus (past medical history)
  ''',
''' 
13. The patient's admission diagnosis, severe sepsis secondary to Enterococcus bacteremia from Osteomyelitis, can be classified into the disease category of infectious diseases.
''',
'''
14. The discharge summary doesn't specifically list current medications, it only mentions the use of aggressive fluid resuscitation, intravenous antibiotics (Vancomycin and Ceftriaxone), and insulin for hyperglycemia management during the hospital stay.
''',
'''
15. (Repeating answer from #12) The patient's diagnoses are:
   - Severe sepsis secondary to Enterococcus bacteremia from Osteomyelitis with SIRS criteria (recent onsite visit)
   - Rheumatoid arthritis (past medical history)
   - Chronic kidney disease stage 3 (past medical history)
   - Chronic back pain (past medical history)
   - Hypertension (past medical history)
   - Hyperlipidemia (past medical history)
   - Type II diabetes mellitus (past medical history)
   ''',
'''
16. (Repeating answer from #13) The patient's admission diagnosis, severe sepsis secondary to Enterococcus bacteremia from Osteomyelitis, can be classified into the disease category of infectious diseases.
''',
'''
17. The medications the patient was taking prior to admission are not listed in the discharge summary.
''',
'''
18. The major symptoms mentioned in the discharge summary include tachycardia, hypotension, and high fevers.
''',
'''
19. The relationship between the patient's rheumatoid arthritis and their current illness is not directly established in the provided discharge summary. However, it's known that rheumatoid arthritis can compromise the immune system, potentially making the patient more susceptible to infections like Enterococcus bacteremia and Osteomyelitis.
''',
'''
20. The exact dates of diagnosis for Enterococcus bacteremia and Osteomyelitis are not provided in the discharge summary. It is mentioned that these diagnoses were made during the patient's recent admission.
''',
'''
21. The patient came to the hospital because she had severe pain in her back, which was later found to be caused by an infection in her spine and blood.
''',
'''
22. The patient's physical exam did not show any new abnormalities. Her blood pressure, heart rate, respiratory rate, and oxygen saturation were stable.
''',
'''
23. In a medical context, MDS usually stands for Myelodysplastic Syndromes, which are a group of disorders caused by poorly formed blood cells or ones that don't work properly. However, MDS is not specifically mentioned in the provided note.
''',
'''
24. There's no mention of any allergies or adverse drug reactions for the patient in the discharge summary.
''',
'''
25. The patient, a 67-year-old woman, has just completed six weeks of intravenous antibiotics for a spine infection and a blood infection. Her kidney function remained stable during her stay and the signs of infection in her body have been decreasing. She was discharged with medications for her other chronic conditions, including pain, high blood pressure, nerve-related pain, and diabetes.
''',
'''
26. There is no explicit mention in the summary about a relationship between Congestive Heart Failure (CHF) and the patient's current illness. It's important to note that CHF is not listed among the patient's known conditions.
''',
'''
27. The major medical conditions mentioned in the discharge summary are rheumatoid arthritis, chronic kidney disease stage 3, chronic back pain, hypertension, hyperlipidemia, type II diabetes mellitus, Enterococcus bacteremia, and osteomyelitis.
''',
'''
28. The discharge summary doesn't provide information about the patient's INR level upon admission.
''',
'''
29. The discharge summary doesn't explicitly state whether the patient was able to tolerate POs (per os, by mouth intake) during their hospital stay.
''',
'''
30. 'Acute hypoxemic respiratory failure' is a specific medical term itself. It refers to a condition where there is a sudden inability of the respiratory system to maintain adequate oxygen levels in the blood.
''']


gpt4_5 = [
'''1. The patient's primary diagnosis is healthcare-associated pneumonia, hypernatremia, and acute metabolic encephalopathy.

''',
'''2. The sentences in the note that describe the primary diagnosis are: "HCAP: On presentation, pt had worsening mental status, leukocytosis, and CXR c/w possible left lower lobe PNA. She had a new O2 requirement as well. She was started on vanc, zosyn, and azythromycin. She completed an 8-day course on ___. PICC was removed prior to discharge."

''',
'''3. The comorbidities of the patient include Alzheimer's dementia, diabetes mellitus type 2, anemia, depression, osteoarthritis, and urinary incontinence.

''',
'''4. The sentences in the note that describe the comorbidities are: "Past Medical History: Alzheimer's Dementia w/ behavioral disturbances, Delusional Disorder, Hemiplegia ___ CVA, Peripheral vascular disease, Hypertension, Coronary Artery Disease, NIDDM, Anemia, Major Depression w/o psychosis, Osteoarthritis, Urinary Incontinence, Pernicious Anemia, Dysphagia."

''',
'''5. The medications mentioned in the discharge summary are:
   - DuoNeb *NF* (ipratropium-albuterol) 0.5 mg-3 mg(2.5 mg base)/3 mL Inhalation q6hrs
   - Metoprolol Tartrate 12.5 mg PO BID
   - Guaifenesin ER 600 mg PO BID:H:PRN cough
   - Simvastatin 20 mg PO DAILY
   - Levofloxacin 500 mg PO Q24H
   - Citalopram 20 mg PO DAILY
   - Glargine 14 Units Bedtime
   - Bisacodyl ___AILY:AILY:PRN constipation
   - Senna 2 TAB PO HS
   - Acetaminophen 650 mg PO Q4H:PRN pain
   - Norco *NF* (HYDROcodone-acetaminophen) ___ mg Oral qHS
   - Norco *NF* (HYDROcodone-acetaminophen) ___ mg Oral TID:PRN pain
   - Docusate Sodium 100 mg PO BID
   - Dulcolax ___X/WEEK (MO,TH) ___ and ___
   - Fleet Enema ___AILY:PRN constipation
   - Albuterol 0.083% Neb Soln 1 NEB IH Q6H:PRN sob/cough
   - Ipratropium Bromide Neb 1 NEB IH Q6H:PRN cough/sob
   - Aspirin 81 mg PO DAILY

''',
'''6. The sentences in the note that describe the medications are: "Medications on Admission: The Preadmission Medication list is accurate and complete" and "Discharge Medications: You were admitted to the hospital with pneumonia, hypernatremia (high sodium level in your blood) and altered mental status. You were treated with antibiotics and your pneumonia improved."
''',
'''
7. The labs mentioned in the discharge summary are:
   - WBC
   - RBC
   - Hgb
   - Hct
   - MCV
   - MCH
   - MCHC
   - RDW
   - Plt
   - Neuts
   - Lymphs
   - Monos
   - Eos
   - Baso
   - PTT
   - Glucose
   -
''',
    '''
    8. The sentences in the note that describe the labs are:
   - "ADMISSION LABS___ 10:10PM BLOOD WBC-20.4* RBC-4.15* Hgb-11.6* Hct-37.1 MCV-89 MCH-27.9 MCHC-31.2 RDW-14.9 Plt ______"
   - "02:21AM BLOOD ___ PTT-21.1*"
   - "10:10PM BLOOD Glucose-352* UreaN-33* Creat-0.7 Na-164* K-4.6 Cl-132* HCO3-19* AnGap-18"
   - "02:21AM BLOOD ALT-24 AST-19 AlkPhos-103 TotBili-0.2"
   - "02:21AM BLOOD Lipase-28"
   - "02:21AM BLOOD Calcium-9.4 Phos-1.6* Mg-2.2"
   - "12:39PM BLOOD Type-ART pO2-84* pCO2-32* pH-7.46* calTCO2-23 Base XS-0"
   - "10:40PM BLOOD Glucose-340* Lactate-2.9* Na-166* K-3.2*"
   - "10:50PM URINE  BLOOD-MOD NITRITE-POS PROTEIN-30 GLUCOSE-1000 KETONE-NEG BILIRUBIN-NEG UROBILNGN-NEG PH-5.5 LEUK-MOD"
   - "10:50PM URINE  RBC-71* WBC-19* BACTERIA-FEW YEAST-MANY EPI-4"
   - "06:18AM   LACTATE-3.1*"
   - "09:18AM   SODIUM-121* POTASSIUM-2.7* CHLORIDE-95* TOTAL CO2-15* ANION GAP-14"
''',
'''
9. The treatment plan for the patient includes administering antibiotics to address healthcare-associated pneumonia. Additionally, volume resuscitation is provided through IV fluids to correct hypernatremia and ensure hydration. The patient's sodium levels are monitored, and liquid intake is encouraged. High-calorie supplements are added to meals, and assistance with feeding is provided. Electrolytes, such as potassium and sodium, are monitored throughout the treatment process.

''',
    '''
    10. The sentences in the note that describe the treatment plan are:
- "HCAP: On presentation, pt had worsening mental status, leukocytosis, and CXR c/w possible left lower lobe PNA. She had a new O2 requirement as well. She was started on vanc, zosyn, and azythromycin. She completed an 8-day course on ___. PICC was removed prior to discharge."
- "Hypernatremia: She appeared to have hypovolemic hypernatremia based on clinical exam findings of dry mucous membranes, significant respiratory variation in IVC diameter, and IJ collapse with respiratory variation. This is likely multifactorial in the setting of worsening mental status related to infection in combination with dementia. Pt was calculated to have a free water deficit of ~5L. Her hypernatremia was gradually corrected over the course of 2.5 days with ___ NS after volume resuscitation with LR. Her sodium was monitored daily and remained within the normal range. Would continue to monitor weekly while at rehab and encourage liquid intake."
- "Nutrition/Goals of Care: It was suspected that her subacute weight loss is due to her dementia. She was seen by speech and swallow who provided diet recommendations. Also recent malnutrition due to acute illness. The issue of inadequate nutrition in patients with progressive dementia was discussed with her son ___. We discussed adding high-calorie supplements to her diet and assistance with feeding. He will consider using an appetite stimulant with her outpatient providers. We discussed that there is no evidence that tube feeding will improve quality or longevity of life, which he recognized saying that he had dealt with similar issues with his father's chronic progressive illness and ultimately passing. DIET: Regular; Diabetic/Consistent Carbohydrate Consistency: Pureed (dysphagia); Nectar prethickened liquids Supplement: Glucerna shake breakfast, lunch, dinner pills crushed in puree. Aspiration precautions, please provide assistance with feeding."
- "HTN: Pt was mildly hypotensive on arrival and required volume resuscitation; metoprolol was therefore held. These were later restarted."
- "Depression: she was continued on her home dose of 20mg citalopram."
- "H/o CVA: She was continued on her home simva 20 and ASA 81."
- "Anemia: Patient hematocrit trended down during hospitalization to 25. Labs were consistent with anemia of chronic inflammation. Hematocrit remained stable at 25."
- "TRANSITIONAL: -monitor electrolytes (potassium, sodium) -monitor CBC for recovery of RBC count -add high-calorie supplements to meals, assistance with feedings"
''',
'''11. The relationship between the identified problem (pneumonia, hypernatremia, and altered mental status) and the subsequent treatment plan is that the patient was treated with antibiotics (vanc, zosyn, and azythromycin) for the pneumonia, and IV fluids (normal saline and LR) were administered to correct the hypernatremia and provide volume resuscitation.
''',
'''
12. The major problems identified in this discharge summary are healthcare-associated pneumonia (HCAP) and hypernatremia. There is a causal relationship between these two problems in the sense that the patient's worsening mental status, which could be attributed to the infection and dementia, likely contributed to the development of hypernatremia.
''',
'''
13. The patient is currently on the following medications:
   - Acetaminophen 650 mg PO Q4H
   - Citalopram 20 mg PO DAILY
   - Senna 2 TAB PO HS
   - Simvastatin 20 mg PO DAILY
   - Docusate Sodium 100 mg PO BID
   - Dulcolax ___X/WEEK (MO,TH) ___ and ___
   - DuoNeb *NF* (ipratropium-albuterol) 0.5 mg-3 mg(2.5 mg base)/3 mL Inhalation q6hrs
   - Metoprolol Tartrate 12.5 mg PO BID
   - Glargine 10 Units Bedtime
   - Norco *NF* (HYDROcodone-acetaminophen) ___ mg Oral TID:PRN pain
   - Aspirin 81 mg PO DAILY
   - Albuterol 0.083% Neb Soln 1 NEB IH Q6H:PRN sob/cough
   - Ipratropium Bromide Neb 1 NEB IH Q6H:PRN cough/sob
   - Levofloxacin 500 mg PO Q24H

''',
'''14. The diagnoses mentioned in the discharge summary and their sources are as follows:
   - Healthcare-associated pneumonia (recent onsite visit)
   - Hypernatremia (recent onsite visit)
   - Alzheimer's dementia (past medical history)
   - Hypertension (past medical history)
''',
'''
15. The patient's medical history includes Alzheimer's dementia, diabetes mellitus type 2, hemiplegia, peripheral vascular disease, hypertension, coronary artery disease, non-insulin dependent diabetes mellitus (NIDDM), anemia, major depression without psychosis, osteoarthritis, urinary incontinence, pernicious anemia, and dysphagia. The patient also has a history of healthcare-associated pneumonia and hypernatremia.
''',
'''
16. The medical conditions the patient had prior to admission are Alzheimer's dementia, diabetes mellitus type 2, anemia, major depression without psychosis, osteoarthritis, urinary incontinence, pernicious anemia, and dysphagia.
''',
'''
17. The discharge summary does not specify the exact date of when the patient was transferred to the MICU. Therefore, the temporal information regarding the transfer to the MICU is not provided.
''',
'''
18. The discharge summary does not explicitly mention the relationship between the patient's hypernatremia and dementia. However, it can be inferred that the worsening mental status related to the infection and dementia might have contributed to the development of hypernatremia, as mentioned earlier.
''',
'''
19. The medications the patient was taking prior to admission are not explicitly mentioned in the given discharge summary.
''',
'''
20. The abbreviation "HCAP" stands for healthcare-associated pneumonia in the patient's medical history.
''',
'''
21. The patient's normalized diagnosis for their condition is healthcare-associated pneumonia, hypernatremia, and acute metabolic encephalopathy.
''',
'''
22. The patient's initial vital signs on arrival at the OSH were: T: 99.1, HR: 90, RR: 20, and SpO2: 90% on room air.
''',
'''
23. The classification of the patient's pneumonia is not specified in the given discharge summary.
''',
'''
24. The discharge summary does not explicitly mention the relationship between the patient's hypokalemia and pneumonia. Therefore, the specific relationship between these two conditions is not provided.
''',
'''
25. The patient's chief complaint, "AMS, pneumonia," can be rephrased in simpler terms as "confusion and lung infection."
''',
'''
26. The attending physician is not specified in the given discharge summary.
''',
'''
27. The patient's admission labs were as follows:
   - WBC: 2.6
   - K+: 3.0
   - Na: 162
   - Glucose: 489
''',
'''
28. The code status and goals of care are not explicitly mentioned in the given discharge summary. Therefore, a summary of the patient's code status and goals of care cannot be provided.
''',
'''
29. The medication not prescribed at discharge is d) Levofloxacin.
''',
'''
30. The discharge summary does not explicitly state whether the patient's hypernatremia was corrected during their hospital stay.
''']


gpt4_6 = [
'''1. The patient's primary diagnosis is breast cancer recurrence.
''',
'''
2. The following sentences describe the diagnosis:
- "Complaint: Breast cancer recurrence"
- "History of Present Illness: Ms ___ is a ___ woman, who was originally diagnosed with carcinoma of the right breast on ___, which presented as an extremely locally advanced, large exophytic necrotic breast mass complicated by bleeding and repeated episodes of cellulitis and infection required repeating admissions to the hospital and IV antibiotics."
- "She did well until early ___, when she was noted to have recurrent nodules on her chest wall."
- "On ___, CT of the torso demonstrated the chest wall recurrence as well as progression of nodal disease and lung metastases."
''',
'''
3. The comorbidities of the patient are:
- Schizophrenia
- Hypertension
- Stage IIA colonic adenocarcinoma
- History of high-grade SIL
- Polypoid endometrial lesion
- Hernia repair
- Hemorrhoids s/p resection
''',
'''
4. The following sentences describe the comorbidities:
- "Past Medical History: 1. Stage IV metastatic, triple-negative, poorly differentiated invasive breast carcinoma 2. Schizophrenia (patient denies this diagnosis, treated by Dr. ___ at ___ in ___ 3. Hypertension 4. Stage IIA colonic adenocarcinoma (underwent right colectomy ___, CEA normal at the time of surgery) 5. History of high-grade SIL; patient declined follow-up 6. Polypoid endometrial lesion ___ patient declined follow-up 7. Hernia repair 8. Hemorrhoids s/p resection"
''',
'''
5. The medications mentioned in the discharge summary are:
- Amlodipine
- Citalopram
- Prochlorperazine
- Docusate Sodium
- Risperidone
- Trihexyphenidyl
- Acetaminophen
- OxycoDONE (Immediate Release)
- Cyclophosphamide
''',
'''
6. The following sentences describe the medications:
- "Medications on Admission: The Preadmission Medication list may be inaccurate and requires further investigation."
- "Discharge Medications: 1. Amlodipine 5 mg PO DAILY 2. Citalopram 20 mg PO DAILY 3. Prochlorperazine 10 mg PO Q6H: PRN nausea 4. Docusate Sodium 100 mg PO BID 5. Risperidone 3 mg PO HS 6. Trihexyphenidyl 2 mg PO HS 7. Acetaminophen 1000 mg PO Q6H 8. OxycoDONE (Immediate Release) 5 mg PO Q6H: PRN breakthrough RX *oxycodone 5 mg 1 tablet(s) by mouth every six (6) hours Disp #*20 Tablet Refills:*09. Cyclophosphamide 25 mg PO DAILY"
''',
'''
7. The labs mentioned in the discharge summary are:
- WBC
- RBC
- Hgb
- Hct
- MCV
- MCH
- MCHC
- RDW
- Plt
- Glucose
- UreaN
- Creat
- Na
- K
- Cl
- HCO3
- AnGap
- Calcium
- Phos
- Mg
''',
'''
8. The following sentence describes the labs:
- "Pertinent Results: ___ 11:25AM BLOOD WBC-2.7* RBC-2.66* Hgb-8.7* Hct-26.3* MCV
''',
'''

9. The treatment plan for the patient is focused on palliative care and includes a resection of the chest wall recurrences. Additional details of the treatment plan are not provided in the given discharge summary.
''',
'''
10. The note does not specifically mention sentences that describe the treatment plan beyond mentioning the palliative resection of the chest wall recurrences.
''',
'''

11. The relationship between the identified problem (breast cancer recurrence) and the subsequent treatment plan is that the patient is undergoing a palliative resection of the chest wall recurrences as part of the treatment for breast cancer recurrence.
''',
'''
12. No specific causal relationships between the two major problems (breast cancer recurrence and the need for wide excision of the chest wall recurrences) are mentioned in the discharge summary.
''',
'''
13. The patient is currently on the following medications:
- Amlodipine
- Citalopram
- Prochlorperazine
- Docusate Sodium
- Risperidone
- Trihexyphenidyl
- Acetaminophen
- OxycoDONE (Immediate Release)
- Cyclophosphamide
''',
'''
14. Diagnoses mentioned in the discharge summary include:
- Breast cancer recurrence
- Schizophrenia
- Hypertension
- Stage IIA colonic adenocarcinoma
- High-grade SIL
- Polypoid endometrial lesion
- Hernia repair
- Hemorrhoids

The diagnoses include both recent onsite visits (breast cancer recurrence) and past medical history (other diagnoses).
''',
'''
15. The patient's medical history involves a diagnosis of stage IV metastatic, triple-negative, poorly differentiated invasive breast carcinoma with comorbidities including schizophrenia, hypertension, stage IIA colonic adenocarcinoma, high-grade SIL, polypoid endometrial lesion, hernia repair, and hemorrhoids.
''',
'''
16. The patient's current medications are:
- Amlodipine
- Citalopram
- Prochlorperazine
- Docusate Sodium
- Risperidone
- Trihexyphenidyl
- Acetaminophen
- OxycoDONE (Immediate Release)
- Cyclophosphamide
''',
'''
17. There is no explicit mention of a relationship between the patient's breast cancer recurrence and her previous surgery (radical mastectomy) in the discharge summary.
''',
'''
18. The key symptoms of the patient's breast cancer recurrence mentioned in the discharge summary are:
- Recurrent nodules on the chest wall
- Chest wall recurrence
- Progression of nodal disease
- Lung metastases
''',
'''
19. The discharge summary does not provide information about the specific date when the patient was originally diagnosed with breast cancer.
''',
'''
20. The normalized diagnosis for the patient's breast cancer recurrence is "Breast cancer recurrence."
''',
'''21. "CEA" stands for Carcinoembryonic Antigen in the patient's medical history.
''',
'''
22. The discharge summary does not provide specific details of the patient's surgery.
''',
'''
23. The discharge summary does not mention the patient's white blood cell count at discharge.
''',
'''
24. Brief summary of the patient's hospital course: The patient underwent a palliative resection of chest wall breast cancer recurrences without complications. Pain was managed with medication, and the patient was transferred to the floor for post-operative management. The patient's condition remained stable, and she was discharged home with follow-up appointments and consideration for hospice care.
''',
'''
25. The discharge summary does not explicitly state the patient's current level of consciousness.
''',
'''
26. History of present illness in simpler terms: The patient, who had previously been diagnosed with advanced breast cancer, experienced recurrence of the cancer on the chest wall. Despite undergoing a radical mastectomy and receiving various treatments, the cancer returned. The patient presented for surgery to remove the chest wall recurrences.
''',
'''
27. The discharge summary does not provide detailed features of the patient's breast cancer.
''',
'''
28. Additional information about the patient's condition not mentioned in the discharge summary is not available.
''',
'''
29. Yes, the patient was discharged to a home with a service facility.
''',
'''
30. The discharge medication list does not include Ibuprofen. (d) Ibuprofen was not included in the patient's discharge medication list.
''']

gpt4_7 = [
'''1. The patient's primary diagnosis is Hypotension.
''',
'''
2. The following sentences describe the diagnosis: "History of Present Illness:___ with 3VD, DM, Alzheimer's who presented to ___ clinic today with two days of fatigue, malaise, dizziness, somnolence, and decreased PO intake. He was found by his PCP to be hypotensive with SBP 66 and sent to the ED."; "Hypotension: Patient's only localizing symptom is nausea without vomiting, diarrhea, fever or leukocytosis so infection is unlikely."; "Discharge Diagnosis: Primary diagnosis: Hypotension".
''',
'''
3. The patient's comorbidities include Type 2 Diabetes, Hypertension, Hypercholesterolemia, Dementia (likely multi-infarct), Depression, Erectile Dysfunction, Gastroesophageal Reflux, Back Pain, Hearing Loss, Falls, known CAD-3VD, Chronic Renal Insufficiency, benign distal esophageal stricture, and a history of left carotid and groin stents, as well as a left nephrectomy for benign kidney tumor.
''',
'''
4. The sentences that describe the comorbidities are contained within the "Past Medical History" and "Brief Hospital Course" sections, including "Past Medical History:TYPE 2 DIABETES  HYPERTENSION  HYPERCHOLESTEROLEMIA  DEMENTIA (likely multi-infarct)  DEPRESSION  ERECTILE DYSFUNCTION  GASTROESOPHAGEAL REFLUX  BACK PAIN  HEARING LOSS  FALLS  known CAD- 3VD, without intervention  Chronic Renal Insufficency- ___ to DM2 and HTN  benign distal esophageal stricture  s/p left carotid stent  s/p groin stent  s/p left nephrectomy for benign kidney tumor"
''',
'''
5. The medications mentioned in the discharge summary include Atenolol, Citalopram, Clopidogrel (Plavix), Galantamine, Glipizide, Isosorbide Mononitrate, Lisinopril, Memantine (Namenda), Metformin, Nitroglycerin, Pioglitazone (Actos), Quetiapine (Seroquel), Ranitidine HCl, Simvastatin, Acetaminophen, Aspirin, and petrolatum ointment.
''',
'''
6. The medications are described in the sections titled "Medications on Admission", "Discharge Medications", and also within the "Brief Hospital Course" sections.
''',
'''
7. The labs mentioned in the discharge summary are creatinine, lipase, HCT, troponin, cortisol, LFT's, white count, Iron studies, B12, folate, and RPR.
''',
'''
8. The labs are described in sections such as "History of Present Illness", "Brief Hospital Course", and "Anemia" within the discharge summary.
''',
'''
9. The treatment plan included intravenous fluid hydration to address hypotension and fatigue, likely due to decreased oral intake over several days. Medication changes were made, including the suspension of Atenolol until consultation with the PCP. It is also indicated that the patient continue with a good diet and hydration at home, and that a pending thyroid function test be followed up at the next appointment with the doctor.
''',
'''
10. The sentences that describe the treatment plan are contained within the "Brief Hospital Course", "Discharge Medications", and "Discharge Instructions" sections of the discharge summary.
''',
'''
11. The identified problem was hypotension due to poor oral intake over the past few days, resulting in fatigue and acute renal failure. The treatment plan was to provide intravenous fluid hydration to rectify the hypotension and renal failure. Atenolol was also held due to hypotension and renal failure until the patient could see their primary care physician.
''',
'''
12. The two major problems identified in this discharge summary are hypotension and acute renal failure. The hypotension seems to have caused the renal failure, as the patient's renal function improved with the resolution of the hypotension through fluid hydration.
''',
'''
13. The patient is currently on the following medications: citalopram, clopidogrel, galantamine, glipizide, lisinopril, memantine, metformin, isosorbide mononitrate, nitroglycerin, Actos, quetiapine, ranitidine HCl, simvastatin, acetaminophen, aspirin, and petrolatum ointment for dry skin.
''',
'''
14. The recent primary diagnosis from this visit is hypotension. Past medical history includes type 2 diabetes, hypertension, hypercholesterolemia, dementia, depression, erectile dysfunction, gastroesophageal reflux, back pain, hearing loss, falls, known CAD- 3VD, chronic renal insufficiency, benign distal esophageal stricture, and history of left carotid stent, groin stent, and left nephrectomy for benign kidney tumor.
''',
'''
15. The primary diagnosis of the patient can be classified as a circulatory system disorder, specifically hypotension.
''',
'''
16. The medication that was held until the patient sees their PCP is Atenolol.
''',
'''
17. The discharge summary does not provide a specific date for the patient's last RPR test.
''',
'''
18. The patient has a known 3 Vessel Disease (3VD) part of Coronary Artery Disease (CAD) and he is on medications including clopidogrel, aspirin, isosorbide, and an ACE inhibitor (lisinopril) as a part of his CAD management. Atenolol, a beta blocker also used for CAD, was held due to hypotension and renal failure.
''',
'''
19. The patient's major medical conditions include type 2 diabetes, hypertension, hypercholesterolemia, dementia, depression, erectile dysfunction, gastroesophageal reflux, back pain, hearing loss, falls, known CAD- 3VD, and chronic renal insufficiency.
''',
'''
20. In the context of the patient's medical history, "VD" stands for "Vessel Disease".
''',
'''
21. The patient was admitted due to fatigue and altered mental status secondary to hypotension. This was believed to be due to inadequate oral fluid intake. Hypotension resulted in acute renal failure, which improved with intravenous fluid resuscitation. The patient's atenolol was held due to hypotension and renal failure until they could see their primary care physician.
''',
'''
22. The discharge summary does not provide specific information on the patient's vital signs on admission and at discharge.
''',
'''
23. The patient was brought to the hospital because they were feeling extremely tired and confused, which was caused by low blood pressure.
''',
'''
24. The discharge summary does not mention the name of the attending physician.
''',
'''
25. The patient's major surgical history includes a left carotid stent, groin stent, and left nephrectomy for a benign kidney tumor. No invasive procedures were mentioned during the hospital stay described in the discharge summary.
''',
'''
26. The discharge summary does not mention the patient's lipase level.
''',
'''
27. c. Atenolol was not restarted during the patient's hospital stay.
''',
'''
28. The discharge summary does not mention any instance of the patient experiencing chest pain during their hospital stay.
''',
'''
29. The standard medical term for the patient's diagnosis of 'multi-infarct dementia' is 'Vascular Dementia'.
''',
'''
30. Given the patient's history of hypotension, renal failure, and multiple comorbidities including CAD-3VD, type 2 diabetes, dementia, and chronic renal insufficiency, potential complications to monitor during follow-up care could include recurrent hypotension, further renal function deterioration, worsening of CAD symptoms, and progression of dementia. Moreover, due to the hold on atenolol, monitoring blood pressure and heart rate would be important.
''']

gpt4_8 = [
'''1. The patient's primary diagnosis is Deep Vein Thrombosis.
''',
'''
2. The patient's comorbidities include Congestive Heart Failure (CHF), Atrial Fibrillation (Afib), severe advanced Alzheimer's dementia, osteoporosis, hypertension, irritable bowel syndrome, and malnutrition.
''',
'''
3. Medications mentioned in the discharge summary include Metoprolol Succinate XL, Torsemide, Aspirin, Donepezil, Raloxifene, Multivitamins, Namenda XR (Memantine), Ascorbic Acid, Calcium Carbonate, Vitamin D, Fish Oil (Omega 3), Acetaminophen, Glycopyrrolate, and Hyoscyamine.
''',
'''
4. Sentences describing medications include: "She was given 80 mEq of K and 60mg Enoxaparin Sodium.", "She was initially started on Lovenox for treatment but this was discontinued...", "Home metoprolol was continued at a decreased dose", and "Medications on Admission" and "Discharge Medications" sections.
''',
'''
5. The standardized terminology used to describe the patient's condition include terms like CHF, Afib, Deep Vein Thrombosis, Hypertension, Alzheimer's dementia, osteoporosis, and malnutrition.
''',
'''
6. Sentences describing medications include: "She was given 80 mEq of K and 60mg Enoxaparin Sodium.", "She was initially started on Lovenox for treatment but this was discontinued...", "Home metoprolol was continued at a decreased dose", and "Medications on Admission" and "Discharge Medications" sections.
''',
'''
7. Labs mentioned in the discharge summary include Potassium (K), Creatinine (Cr), CBC, Urinalysis (UA), cTropnT, proBNP, blood glucose, Urea N, Sodium, Chloride, Total CO2, Anion Gap, and various other elements in the CBC panel.
''',
'''
8. Sentences describing the labs include: "Labs were significant for : K 2.8 Cr 0.8CBC...", "UA: WBC 22, moderate leuks, negative nitrites", and "___ 12:00PM   cTropnT-0.03* proBNP-8428*" and various sentences in the "Pertinent Results" section.
''',
'''
9. The treatment plan for the patient is to transition care to comfort-directed measures only and to pursue hospice services on discharge. The patient was initially started on Lovenox for treatment of DVT but this was discontinued. Home metoprolol was continued at a decreased dose for comfort.
''',
'''
10. The patient was diagnosed with Deep Vein Thrombosis and several comorbidities including CHF and Afib. The treatment plan focused on transitioning the patient's care to comfort-directed measures and pursuing hospice services on discharge. The patient was initially started on Lovenox for DVT treatment, but this was later discontinued. Her other medications were continued for comfort.
''',
'''
11. The identified problem of Deep Vein Thrombosis (DVT) led to an initial treatment with Lovenox, but it was discontinued, likely due to the patient's overall declining health and the decision to transition to comfort care.
''',
'''
12. There's no clear causal relationship mentioned between the major problems of Deep Vein Thrombosis (DVT) and Congestive Heart Failure (CHF). They co-exist in this patient's case.
''',
'''
13. The patient's current medications include Metoprolol Succinate XL, Torsemide, Aspirin, Donepezil, Raloxifene, Multivitamins, Namenda XR (Memantine), Ascorbic Acid, Calcium Carbonate, Vitamin D, Fish Oil (Omega 3), Acetaminophen, Glycopyrrolate, and Hyoscyamine.
''',
'''
14. The patient's recent diagnosis from this visit is Deep Vein Thrombosis (DVT). Past medical history includes Congestive Heart Failure (CHF), Atrial Fibrillation (Afib), severe advanced Alzheimer's dementia, osteoporosis, hypertension, irritable bowel syndrome, and malnutrition.
''',
'''
15. The patient, with multiple comorbidities, was diagnosed with Deep Vein Thrombosis and given comfort care measures, including medication adjustments, with the plan to pursue hospice services post-discharge.
''',
'''
16. The patient's past medical history conditions include Congestive Heart Failure (CHF), Atrial Fibrillation (Afib), severe advanced Alzheimer's dementia, osteoporosis, hypertension, irritable bowel syndrome, and malnutrition.
''',
'''
17. The discharge summary doesn't provide specific information regarding when the patient moved into the assisted living facility.
''',
'''
18. There's no explicit mention of a relationship between the patient's CHF and pleural effusions in the discharge summary.
''',
'''
19. The discharge summary doesn't mention any specific symptoms that the patient complained about.
''',
'''
20. The patient's vital signs on admission aren't provided in the given discharge summary.
''',
'''
21. The family history includes coronary artery disease in the patient's father, with the onset at age 60, and Alzheimer's disease in the patient's mother, with the onset at age 75.
''',
'''
22. Yes, "Afib" can be normalized to "Atrial fibrillation".
''',
'''
23. The primary diagnosis for this patient is Deep Vein Thrombosis (DVT).
''',
'''
24. "TTE" stands for Transthoracic Echocardiogram.
''',
'''
25. There is no mention of any falls before the patient presented to the Emergency Department.
''',
'''
26. The patient was discharged on the following medications: Metoprolol Succinate XL, Torsemide, Aspirin, Donepezil, Raloxifene, Multivitamins, Namenda XR (Memantine), Ascorbic Acid, Calcium Carbonate, Vitamin D, Fish Oil (Omega 3), Acetaminophen, Glycopyrrolate, and Hyoscyamine.
''',
'''
27. The patient's current activity status isn't specified in the discharge summary.
''',
'''
28. The condition not mentioned in the patient's past medical history is (C) Diabetes.
''',
'''
29. No, the patient was not placed on anticoagulation for the DVT.
''',
'''
''']

gpt4_9 = [
'''1. The patient's primary diagnosis is mechanical lower back pain attributed to degenerative disease/arthritis of the lumbar spine (Lumbago).
''',
'''
2. The diagnosis is described in these sentences: "___ y/o M with h/o CAD, atrial flutter, asthma, CHF and ESRD on HD who presented with 4 days of gradual onset back pain radiating to the back with difficulty walking."; "Lumbago (mechanical lower back pain attributed to degenerative disease/arthritis of the lumbar spine)."
''',
'''
3. The patient's comorbidities include End Stage Renal Disease (ESRD) on hemodialysis (HD), Coronary Artery Disease (CAD), history of atrial flutter, Hypertension (HTN), and Chronic Obstructive Pulmonary Disease (COPD).
''',
'''
4. The comorbidities are described in these sentences: "___ y/o M with h/o CAD, atrial flutter, asthma, CHF and ESRD on HD who presented with 4 days of gradual onset back pain radiating to the back with difficulty walking."; "ESRD - continued HD."; "CAD/HTN - continued BB, ASA."; "h/o atrial flutter - in NSR."
''',
'''
5. The medications mentioned in the discharge summary are Metoprolol Succinate (Toprol XL), Aspirin, Omeprazole, Calcium Acetate (Phoslo), Sevelamer HCl (Renagel), Docusate Sodium, and Percocet.
''',
'''
6. Medications are described in these sentences: "Medications on Admission: Toprol XL 50 mg Daily, ASA 81 mg PO Daily, Omeprazole 20 mg PO Daily, Phoslo 667 mg PO TID, Docusate, Renagel 1 tab daily."; "Discharge Medications: Metoprolol Succinate 50 mg, Aspirin 81 mg, Omeprazole 20 mg, Calcium Acetate 667 mg, Sevelamer HCl 800 mg, Docusate Sodium 100 mg, Percocet."
''',
'''
7. There are no specific lab tests mentioned in the discharge summary.
''',
'''
8. Not applicable, as there are no specific labs described in the note.
''',
'''
9. The treatment plan for the patient included continued hemodialysis for ESRD, continuation of current medications for CAD, HTN, and atrial flutter, and addition of Percocet as needed for pain management.
''',
'''
10. The treatment plan is described in these sentences: "Back pain - appears to be musculoskeletal in nature, no red flags such as fecal incontinence, urinary retention, neurological exam findings. Xray negative for fracture. Treated with hot packs and prn percocet."; "ESRD - continued HD."; "CAD/HTN - continued BB, ASA."; "h/o atrial flutter - in NSR."; "No changes were made to your home medications, we have only added percocet as needed for pain, as well as recommending the use of hot packs as needed to the area of pain."
''',
'''
11. The patient was diagnosed with mechanical lower back pain due to lumbar spine degeneration. The treatment plan was formulated to address this problem, which included hot packs and Percocet for pain management. In addition, the patient's comorbid conditions such as ESRD, CAD, and atrial flutter were managed with continued hemodialysis and prescribed medications.
''',
'''
12. The discharge summary primarily identifies the patient's lower back pain and the comorbid conditions like ESRD, CAD, atrial flutter, HTN, and COPD. While all these conditions contribute to the overall health of the patient, there is no direct causal relationship indicated between these in the discharge summary.
''',
'''
13. The patient's current medications include Metoprolol Succinate, Aspirin, Omeprazole, Calcium Acetate, Sevelamer HCl, Docusate Sodium, and as-needed Percocet for pain management.
''',
'''
14. The patient's diagnoses include a recent diagnosis of mechanical lower back pain (Lumbago) during the onsite visit. The patient's past medical history includes End Stage Renal Disease (ESRD) on hemodialysis, Coronary Artery Disease (CAD), history of atrial flutter, Hypertension (HTN), and Chronic Obstructive Pulmonary Disease (COPD).
''',
'''
15. The patient's chief complaint is back pain and difficulty walking due to the pain.
''',
'''
16. During the hospital stay, it was determined that the patient's back pain appeared to be musculoskeletal in nature with no red flags such as fecal incontinence, urinary retention, or significant neurological exam findings. The back pain was managed with hot packs and Percocet. The patient's other medical conditions like ESRD, CAD, and atrial flutter were also managed appropriately.
''',
'''
17. The patient's medical conditions mentioned in the summary include mechanical lower back pain, End Stage Renal Disease (ESRD) on hemodialysis, Coronary Artery Disease (CAD), history of atrial flutter, Hypertension (HTN), Chronic Obstructive Pulmonary Disease (COPD), and large scrotal/R inguinal hernia.
''',
'''
18. The patient first presented with back pain four days before being admitted to the hospital.
''',
'''
19. There is no direct relationship indicated in the discharge summary between the patient's Coronary Artery Disease (CAD) and his back pain.
''',
'''
20. The patient, a male with a history of heart disease, irregular heart rhythm, asthma, heart failure, and severe kidney disease, came to the hospital because he had been experiencing back pain for four days. This pain made it difficult for him to walk, and he had never felt this kind of pain before. The pain was worse when he moved, but he didn't have any other symptoms like numbness or weakness in his legs. After not being able to walk around a soda machine because of his back pain, the manager of his building called an ambulance to bring him to the hospital.
''',
'''
21. The keywords related to the patient's diagnosis of lumbago include "back pain", "difficulty walking", "pain exacerbated by movement", "musculoskeletal pain", "moderate arthritis of the lumbar spine", and "no neurological deficits".
''',
'''
22. The patient's condition can be standardized as "Lumbago due to degenerative arthritis of the lumbar spine."
''',
'''
23. ESRD stands for End Stage Renal Disease.
''',
'''
24. The key features of the patient's physical exam include regular heart sounds, non-distended abdomen, no edema or clubbing of extremities, no rashes or jaundice on skin, and intact sensation in upper and lower extremities. There is also noted guarding of straight leg due to pain in the right lower back.
''',
'''
25. The medications listed in the discharge summary include Metoprolol Succinate, Aspirin, Omeprazole, Calcium Acetate, Sevelamer HCl, Docusate Sodium, and Percocet for pain management.
''',
'''
26. The patient's discharge condition is described as stable.
''',
'''
27. c) ESRD - Considering the patient's current presentation, End Stage Renal Disease is the most concerning as it significantly affects his overall health and has implications for pain management.
''',
'''
28. Further evaluation of the patient's back pain could consider an MRI of the lumbar spine to better evaluate the soft tissue structures and any possible nerve involvement.
''',
'''
29. Yes, a herniated disc was ruled out as a cause of the patient's back pain as the patient denies any history of herniated discs and there is no mention of this in the physical examination findings.
''',
'''
30. Yes, a family history of stroke is mentioned in the summary. Both the patient's father and brother died from strokes at an unspecified age.
'''
]

gpt4_result = [gpt4_0, gpt4_1, gpt4_2, gpt4_3, gpt4_4, gpt4_5, gpt4_6, gpt4_7, gpt4_8, gpt4_9]

gpt4 = gpt4_result[note_number-1][index]
    
st.write("**GPT-4**")
st.warning(gpt4)

# st.write("**Alpaca**")
# st.error(alpaca)



