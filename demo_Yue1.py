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
     Azure += answer['text']

        


st.write("\n")
st.markdown("""---""")
st.write("\n")

st.write("**Azure**")
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

gpt4_result = [gpt4_0, gpt4_1, gpt4_2, gpt4_3]

if note_number < 5:
    gpt4 = gpt4_result[note_number-1][index]
    
st.write("**GPT-4**")
st.warning(gpt4)

# st.write("**Alpaca**")
# st.error(alpaca)



