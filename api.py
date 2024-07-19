import json
from openai import OpenAI
client = OpenAI(api_key='')

def comp(PROMPT=''):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        response_format={ "type": "json_object" },
        messages=[
            {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
            {"role": "user", "content": PROMPT}
        ]
    )
    respDict = json.loads(response.choices[0].message.content)
    print(respDict)
    

prompt = """which surgeries are listed here, with their date, using None for unknown: Phone: (650)723-6601 Fax: (650)725-8910

Patient Name: CHASE, JEANINE Subject Code: 09148JC5 Study Date: 09-14-08

Oxygen Saturation

PARAMETER

Mean SaQ2 %
Min SaO2 %
Max Sa02 %

% Duration of SaO2 In

Range :
90 - 100 %
80 - 90 %
70 - 80%
60-70%
50 - 60 %
Below 50 %

PLMs and Sleep Stages

INDEX INDEX TOTAL
0.0
0.0

Total Sleep
Stage |
Stage 2
Stage 3
Stage 4

Stage REM

PLM Events With Arousals PLM Events W/O Arousals

PARAMETER INDEX PARAMETER | INDEX TOTAL

Total Events 0.0 Total Events 0.0
0.0
0.0

NREM 0.0
REM 0.0

15-1664 (Jan-00) 3
Stanford Sleep Disorders Clinic
401 Quarry Road
Stanford, CA 94305

Phone: (650)723-6601 Fax: (650)725-8910

Patient Name: CHASE, JEANINE Subject Code: 09148JC5 Study Date: 09-14-08

Pressure Level Analysis

Pressure TRT REM Non- | Obstr. | Cent. | Mixed | Hypo- | Total Sa02 SaQ2 SaOQ2
(cm H20) (min) | (min) REM | Apnea | Apnea | Apnea } pneas | Events High Low Mean
(min

Recording Technician’s (MR) Comments :

Scoring Technician’s (JA) Comments :

Patient slept mostly in stage 2.

Flow limitations, hypopneas, and apneas noted, often cyclical.
Snoring noted.

15-1664 (Jan-00) 4
LEGS

BODY POS

Stanford Sleep Disorders Clinic
401 Quarry Road
Stanford, CA 94305

Phone: (650)723-6601 Fax: (650)725-8910

Patient Name: CHASE, JEANINE Subject Code: 09148JC5 Study Date: 09-14-08
GRAPHS

STAGING
n
ry
ao
&

22:00 23:00 00:00 01:00 02:00 03:00 04:00 05:00 06:00 07:00

ra Imogliwl w TT Oe ieee ot COG i] \a mm) @ Bawa) ii wi alt
Oo
e wsmel tie) sae) 6§l lc ae uD) oom ton a a tI SS) ie Ll nr
wl
22:00 23:00 00:00 01:00 02:00 03:00 04:00 05:00 06:00 07:00
Both Legs
Righ
Left
Both Legs+Ar
Righf +Arsl
Left + Arsl
22:00 23:00 00:00 01:00 02:00 03:00 04:00 05:00 06:00 07:00
>
or
|
Lu
2
iS
22:00 23:00 00:00 01:00 02:00 03:00 04:00 05:00 06:00 07:00
Supine
Prone
Left
ri
Out of Bed
22:00 23:00 00:00 01:00 02:00 03:00 04:00 05:00 06:00 07:00
20
a
< 10
Oo
0
22:00 23:00 00:00 01:00 02:00 03:00 04:00 05:00 06:00 07:00
20
Tr
iu
=
o 0
22:00 23:00 00:00 01:00 02:00 03:00 04:00 05:00 06:00 07:00

15-1664 (Jan-00) )
-end
Wyatt Jaffe

Mark Twain Medical Center
May 15th, 2023 1:39pm
May 15th, 2023 1:39pm

Mark Twain Medical Center
768 Mountain Ranch Rd.
San Andreas, CA 95249

ED H&P

Patient Sone MR Number: CHOO
154502

Age: 51 DOB: 08/19/1971 Sex: F

Acct Number: MT4401207131

Attending Physician: Admit Date: 05/15/23
KMR Number: Admit Time: 1304

Report Status: Signed

History of Present Illness

Time Seen by Provider: 05/15/23 13:35
Chief Complaint: Ear Complaints

HPI:

Patient is a 51-year-old female who comes in complaining of increasing pain in the right ear for the last 4 days. Patient been trying saline nasal sprays as well as Mucinex without much relief. She has a history of multiple surgeries onher sinuses and jaw for due to sleep apnea. Patient also said over the last week she had a URI and saw her primary who gave her prescription for antibiotics. She says she finished that few days ago. He said that since then she still felt a lot of congestion and now pain in her right ear. No discharge from the ear. No fever. No other significant complaints.
Past Medical Surgical History:

Past Medical-Surgical History Start: 05/15/23 13:05

Freq: Status: Active

Protocol:

Document 05/15/23 13:18 KREIEM (Rec: 05/15/23 13:25 KREIEM EDCO2MEDVDA1002)
Past Medical-Surgical History

Do You Have Any Past Medical or Surgical Yes

History [ACEDMPM]

EENT Medical-Surgical Details/Date MAXILLARY-MANDIBULAR JAW
ADVANCEMENT SURGERY @STANFORD

2012

Respiratory Medical History Sleep apnea

Has Patient Had A Prior Colonoscopy? No.

Has Patient Had a Prior Endoscopy? No

Reproductive surgical history Hysterectomy

LMP 3/11/2018

Pregnant No

Musculoskeletal surgical history Hip Surgery

Patient with History of Venous No.

Thromboembolism (VTE)?

Psychosocial medical disorder Anxiety, Depression

Social History:

Alcohol Frequency Occasionally
Alcohol Use Ever Caused a No
Problem for You or Your Family
Alcohol Use Current
Recreational Drug Use None

Any previous attempts of self No
harm/suicide

Primary Dx or stated complaint No
of emotional/beh disorder

Source of history: Patient

Allergies and Home Meds
Home Medications:

Medication Instructions Recorded

QUEtiapine [Seroquel] 1 tab PO BEDTIME #30 tab 07/02/19
zolpidem [Ambien] 5 mg PO BEDTIME PRN 07/03/19
atorvastatin [Lipitor] 10 mg PO BEDTIME 03/31/21
gabapentin [Gabapentin] 300 mg PO TID 04/20/22
Citalopram Hydrobromide 40 mg PO QAM 03/23/23
[Citalopram HBr]

methylphenidate HC! 30 mg PO QAM 03/23/23
[Methylphenidate HCI ER]

Guaifenesin/Pseudoephedrne HCI 1 each PO BID #14 tab.er.12h 05/15/23
[Mucinex D ER 1,200-120 mg Tab]

Oxymetazoline HCI [Afrin] 1 spray NASAL BID #15 ml 05/15/23

Allergies/Adverse Reactions:

Allergy/AdvReac Type Severity Reaction Status Date / Time

Penicillins Allergy Severe Anaphylaxis Verified 03/23/23 09:57

Reviewed the patient's home medications and allergies:: Yes

ED Review of Systems
Statement: All ROS negative unless mentioned in HPI

Physical Exam
Vital Signs:

Temp Pulse Resp BP Pulse Ox
05/15/23 13:18 99.0 F 100 16 137/85 97

Height: 5 ft 2 in
Weight: 86.636 kg
BMI: 34.9

Pulse Ox: normal

General Appearence: no acute distress, alert, oriented X3, well nourished, well developed, well appearing

Neuro: normal mood, normal affect, normal speech, normal gait, moves all 4 extremities. No: motor weakness, sensory deficit
HEENT: ENT appears normal, normocephalic atraumatic, EOMs intact, PEERL, tympanic membranes* (Clear bilaterally no erythema)
Neck: supple, non-tender, atraumatic, painless ROM

Respiratory: lungs clear, normal air movement, speaks full sentences

Cardiovascular: regular rate & rhythm, normal peripheral pulses, no murmur

MDM & Depart

Differential Diagnosis:

Multiple differential diagnoses were considered in this patient
Reviewed by me today: Medications

Was an EKG Done?: No

ED Course:

Based on history and physical my impression is the patient likely has eustachian tube dysfunction. Recommend more aggressive decongestants with Afrin and pseudoephedrine. These prescriptions were given. Indications given to return. Patient verbalized understanding and agreement with plan and discharge.
Condition: Stable

Plan of Care discussed with: Patient

Clinical Impression/Final Diagnosis:

Eustachian tube dysfunction

Qualifiers:

Laterality: right Qualified Code(s): H69.81 - Other specified disorders of Eustachian tube, right ear

ED Disposition: Discharged
ED H&P Completed: Yes

Report Entered By: Jaffe, Wyatt MD
Electronically Signed: Jaffe, Wyatt MD

Sign Date/Time: 05/15/23 1339
<Electronically signed by Wyatt Jaffe, MD>
Entered D/T: 05/15/23 1337 By:JAFFWY
Report #: 0515-0033"""

comp(prompt)