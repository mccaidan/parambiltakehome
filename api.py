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
    

promptNothing = """
A
Ww
Ti R
Sleep pie tle
n1
3%
H2
11% NS
ws
Sere Event :[C]
4
33
lew Everts [6.0
OCVAHLA
4
ws
Spue ws.

Cae

S‘ewslorw = [12 Ri

CHASE JEANNE, Mesarenen date 4292019
Recording Parameters

1. An 11 lead electroencephalogram (EEG) to measure global neural encephalographic actmty
using electrodes placed on the scalp.

2. Electrooculogram (EOG) to measure eye movements using electrodes placed near the outer
canthus of each eye.

3. A submental electromyogram (EMG) to measure submental electromyographic activity using
electrodes placed over the mentalis, submentalis muscle, and/or masseter regions.

4. Rhythm electrocardiogram (ECG). Modified V2 placement.

5. Nasal and/or oral airflow via both thermistor and nasal pressure sensor.

6. Respiratory Effort by chest-wall and abdominal movement measured using respiratory inductive
plethysmography, endoesophageal pressure and/or by intercostal EMG.

7. Gas exchange (oxygen saturation [SpO2]) by oximetry or transcutaneous monitoring.

8. Bilateral anterior tibialis muscle activity, motor activity-movement using EMG.

9. Body positions by directly applied sensors or by direct observation.

10. Photoplethysmography and Pulse Rate

11. Video w/infrared lighting (704x576 @ 30fps)

12. Audio (8KHz)

Optional
"""

promptSurgery = """
Phone: (650)723-6601 Fax: (650)725-8910

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
Report #: 0515-0033
"""

promptMedication = """
Tab08/20/2020Medication Instructions Qty Status Started Stopped IndicationDoctor
ﬂuticasone nasal 0.05 mg/inh spray1 Spray Spray, NASAL, Daily, Qty: 16 gm,
Reﬁlls: 6, USE 1 SPRAY TO EACH NOSTRIL
DAILY, Maintenance, Route to Pharmacy
Electronically, CVS/pharmacy #953916 g 08/18/2020
zolpidem 10 mg oral tablet1 Tab Tab, PO, qHS, 30 Day, Qty: 30 Tab,
Reﬁlls: 4, TAKE 1 TABLET BY MOUTH AT
BEDTIME AS NEEDED FOR SLEEP, 01/03/21
13:59:00 PST, Acute, Route to Pharmacy
Electronically, CVS/pharmacy #9539, MDD
(major depressive disorder), recurrent, in full
remission30
Tab08/06/2020 01:59
PM01/03/2021
01:59 PM
QUEtiapine 50 mg oral tablet1 Tab Tab, PO, qHS, Qty: 30 Tab, Reﬁlls: 4,
TAKE 1 TABLET BY MOUTH EVERY DAY AT
BEDTIME FOR MOOD AND INSOMNIA,
Maintenance, Route to Pharmacy
Electronically, CVS/pharmacy #9539, MDD
(major depressive disorder), recurrent, in full
remission30
Tab08/06/2020 01:59
PM01/03/2021
01:59 PM
buPROPion 100 mg/12 hours (SR) oral
tablet, extended release1 Tab Tab, ER, PO, BID, Qty: 60 Tab, Reﬁlls: 3,
1 tab qam for 3 days then 1 tab BID
discontinue celexa and Ritalin, Maintenance,
Route to Pharmacy Electronically,
CVS/pharmacy #9539, MDD (major depressive
disorder), recurrent episode, mild60
Tab08/06/2020 01:59
PM12/04/2020
01:59 PM
loratadine 10 mg oral tablet1 Tab, PO, Daily, Qty: 90 Tab, Reﬁlls: 3,
Maintenance, Route to Pharmacy
Electronically, CVS/pharmacy #953990
Tab07/09/2020
atorvastatin 10 mg oral tablet1 Tab Tab, PO, Daily, Qty: 90 Tab, Reﬁlls: 3,
TAKE 1 TABLET BY MOUTH EVERY DAY,
Maintenance, Route to Pharmacy
Electronically, CVS/pharmacy #953990
Tab07/09/2020
loratadine 10 mg oral tablet1 Tab, PO, Daily, Qty: 30 Tab, Reﬁlls: 6,
Maintenance, 30, Route to Pharmacy
Electronically, CVS STORE 0953930
Tab06/11/2020
citalopram 20 mg oral tablet2 Tab Tab, PO, qHS, Qty: 60 Tab, 4,
Maintenance, Route to Pharmacy
Electronically, CVS/pharmacy #9539, MDD
(major depressive disorder), recurrent, in full
remission60
Tab05/06/2020 03:03
PM10/03/2020
03:03 PMMedication Instructions Qty Status Started Stopped IndicationDoctor
methylphenidate 10 mg oral tablet1 Tab Tab, PO, qAM, Qty: 30 Tab, 0, 1/2 to 1
tab qam PRN focus, Maintenance, Route to
Pharmacy Electronically, CVS/pharmacy
#9539, ADHD30
Tab05/06/2020 03:03
PM06/05/2020
03:03 PM
QUEtiapine 50 mg oral tablet1 Tab Tab, PO, qHS, Qty: 30 Tab, 4, TAKE 1
TABLET BY MOUTH EVERY DAY AT BEDTIME
FOR MOOD AND INSOMNIA, Maintenance,
Route to Pharmacy Electronically,
CVS/pharmacy #9539, MDD (major depressive
disorder), recurrent, in full remission30
Tab05/06/2020 03:03
PM10/03/2020
03:03 PM
zolpidem 10 mg oral tablet1 Tab Tab, PO, qHS, 30 Day, Qty: 30 Tab, 4,
TAKE 1 TABLET BY MOUTH AT BEDTIME AS
NEEDED FOR SLEEP, 10/03/20 15:03:00 PDT,
Acute, Route to Pharmacy Electronically,
CVS/pharmacy #9539, MDD (major depressive
disorder), recurrent, in full remission30
Tab05/06/2020 03:03
PM10/03/2020
03:03 PM
citalopram 20 mg oral tablet2 Tab Tab, PO, qHS, Qty: 60 Tab, 4, 1.5 tabs
qhs for 1 week then 2 tabs qhs, Maintenance,
Route to Pharmacy Electronically,
CVS/pharmacy #9539, MDD (major depressive
disorder), recurrent, in full remission60
Tab04/01/2020 11:57
AM08/29/2020
11:57 AM
citalopram 20 mg oral tablet2 Tab Tab, PO, qHS, Qty: 60 Tab, 4, 1.5 tabs
qhs for 1 week then 2 tabs qhs, Maintenance,
Route to Pharmacy Electronically,
CVS/pharmacy #9539, MDD (major depressive
disorder), recurrent, in full remission60
Tab03/10/2020 02:30
PM08/07/2020
02:30 PM
zolpidem 10 mg oral tablet1 Tab Tab, PO, qHS, 30 Day, Qty: 30 Tab, 4,
TAKE 1 TABLET BY MOUTH AT BEDTIME AS
NEEDED FOR SLEEP, 08/07/20 14:30:00 PDT,
Acute, Route to Pharmacy Electronically,
CVS/pharmacy #9539, MDD (major depressive
disorder), recurrent, in full remission30
Tab03/10/2020 02:30
PM08/07/2020
02:30 PM
methylphenidate 10 mg oral tablet1 Tab Tab, PO, qAM, Qty: 30 Tab, 0, 1/2 to 1
tab qam PRN focus, Maintenance, Route to
Pharmacy Electronically, CVS/pharmacy
#9539, ADHD30
Tab03/10/2020 02:30
PM04/09/2020
02:30 PMMedication Instructions Qty Status Started Stopped IndicationDoctor
QUEtiapine 50 mg oral tablet1 Tab Tab, PO, qHS, Qty: 30 Tab, 4, TAKE 1
TABLET BY MOUTH EVERY DAY AT BEDTIME
FOR MOOD AND INSOMNIA, Maintenance,
Route to Pharmacy Electronically,
CVS/pharmacy #9539, MDD (major depressive
disorder), recurrent, in full remission30
Tab03/10/2020 02:30
PM08/07/2020
02:30 PM
tiZANidine 4 mg oral tablet1 Tab, PO, Daily, 30 Tab, 2, Soft Stop, Route to
Pharmacy Electronically, CVS/pharmacy #953930
Tab02/14/2020
ﬂuticasone nasal 0.05 mg/inh spray1 Spray, NASAL, Daily, 16 mL, 5, Soft Stop,
Route to Pharmacy Electronically,
CVS/pharmacy #953916
mL02/03/2020
methylphenidate 10 mg oral tablet1 Tab Tab, PO, qAM, Qty: 30 Tab, 0, 1/2 to 1
tab qam PRN focus, Maintenance, Route to
Pharmacy Electronically, CVS/pharmacy
#9539, ADHD30
Tab12/31/2019 10:22
AM01/30/2020
10:22 AM
zolpidem 10 mg oral tablet1 Tab Tab, PO, qHS, 30 Day, Qty: 30 Tab, 4,
TAKE 1 TABLET BY MOUTH AT BEDTIME AS
NEEDED FOR SLEEP, 05/29/20 10:22:40 PDT,
Acute, Route to Pharmacy Electronically,
CVS/pharmacy #9539, MDD (major depressive
disorder), recurrent, in full remission30
Tab12/31/2019 10:22
AM05/29/2020
10:22 AM
citalopram 20 mg oral tablet1 Tab Tab, PO, qHS, Qty: 30 Tab, 4,
Maintenance, Route to Pharmacy
Electronically, CVS/pharmacy #9539, MDD
(major depressive disorder), recurrent, in full
remission30
Tab12/31/2019 10:22
AM05/29/2020
10:22 AM
QUEtiapine 50 mg oral tablet1 Tab Tab, PO, qHS, Qty: 30 Tab, 4, TAKE 1
TABLET BY MOUTH EVERY DAY AT BEDTIME
FOR MOOD AND INSOMNIA, Maintenance,
Route to Pharmacy Electronically,
CVS/pharmacy #9539, MDD (major depressive
disorder), recurrent, in full remission30
Tab12/31/2019 10:22
AM05/29/2020
10:22 AM
atorvastatin 10 mg oral tablet= 1 Tab, ORAL, DAILY, *NEEDS AN
APPOINTMENT*, # 30 Tab, 0 Reﬁll(s),
Maintenance, Pharmacy: CVS/pharmacy
#9539, 157.48, cm, 12/18/18 13:38:00 PST,
Height/Length (cm), 83.92, kg, 12/18/18
13:38:00 PST, Dose calculation weight (kg)30
Tab12/30/2019
Flovent Diskus 50 mcg/inh inhalation
powder120
Each11/21/2019
ﬂuticasone nasal 0.05 mg/inh spray 11/20/2019Medication Instructions Qty Status Started Stopped IndicationDoctor
tiZANidine 4 mg oral tablet1 Tab Tab, PO, Daily, Qty: 30 Tab, 2,
Maintenance, Route to Pharmacy
Electronically, CVS/pharmacy #953930
Tab11/19/2019
ﬂuticasone 50 mcg/inh inhalation powder1 Puﬀ Pwd, INH, Daily, Qty: 120 Each, 6,
Maintenance, Route to Pharmacy
Electronically, CVS/pharmacy #9539120
Each11/19/2019
loratadine 10 mg oral tablet1 Tab Tab, PO, Daily, Qty: 30 Tab, 6, TAKE 1
TABLET BY MOUTH EVERY DAY, Maintenance,
Route to Pharmacy Electronically,
CVS/pharmacy #953930
Tab11/04/2019
citalopram 20 mg oral tablet30
Tab09/26/2019 02:58
PM02/23/2020
02:58 PM
methylphenidate 10 mg oral tablet30
Tab09/26/2019 02:58
PM10/26/2019
02:58 PM
QUEtiapine 50 mg oral tablet30
Tab09/26/2019 02:58
PM02/23/2020
02:58 PM
zolpidem 10 mg oral tablet30
Tab09/26/2019 02:58
PM02/23/2020
02:58 PM
atorvastatin 10 mg oral tablet TAKE 1 TABLET BY MOUTH EVERY DAY 09/25/2019
loratadine 10 mg oral tablet 09/25/2019
estradiol 1 mg oral tablet TAKE 1 TABLET BY MOUTH EVERY DAY 09/25/2019
tiZANidine 4 mg oral tablet30
Tab08/26/2019
zolpidem (AMBIEN) 10 mg tablet completed08/12/2019Historical
Provider
zolpidem (AMBIEN) 10 mg tablet active 08/12/2019Guadalupe
Marie
Robles
estradiol (ESTRACE) 1 mg tablet stopped08/09/2019 12:00
AM11/02/2022
12:00 AM
ﬂuticasone propionate (FLONASE) 50
mcg/actuation SpSn spraycompleted07/25/2019Historical
Provider
ﬂuticasone propionate (FLONASE) 50
mcg/actuation SpSn sprayUSE 1 SPRAY TO EACH NOSTRIL DAILY active 07/25/2019Guadalupe
Marie
Robles
Zolpidem (Ambien) 10 MG Tab every bedtime active 07/03/2019
Zolpidem (Ambien) 10 MG Tab every bedtime active 07/03/2019
Citalopram Hydrobromide (Citalopram
Hbr) 20 MG Tabletonce daily 30 completed07/02/2019 05:52
PM03/23/2023
09:59 AM
Quetiapine (Seroquel) 50 MG Tab Take one tab at bedtime 30 active 07/02/2019Medication Instructions Qty Status Started Stopped IndicationDoctor
Citalopram Hydrobromide (Citalopram
Hbr) 20 MG Tabletonce daily 30 active 07/02/2019
Loratadine (Claritin) 10 MG Tab once daily completed05/31/2019 10:18
AM03/31/2021
05:59 PM
Azithromycin (Z-Pack (Zithromax)) 250
MG Packet500MG PO X 1; 250MG PO THERAFTER UNTIL
COMPLETEDcompleted05/31/2019 10:18
AM07/02/2019
01:34 PM
Guaifenesin (Mucinex) 600 MG Tab once daily completed05/31/2019 10:18
AM03/31/2021
05:59 PM
Loratadine (Claritin) 10 MG Tab once daily completed05/31/2019 12:00
AM03/31/2021
05:59 PM
Azithromycin (Z-Pack (Zithromax)) 250
MG Packet500MG PO X 1; 250MG PO THERAFTER UNTIL
COMPLETEDcompleted05/31/2019 12:00
AM07/02/2019
01:34 PM
Guaifenesin (Mucinex) 600 MG Tab once daily completed05/31/2019 12:00
AM03/31/2021
05:59 PM
QUEtiapine (SEROQUEL) 50 mg tablet completed05/08/2019Historical
Provider
"""

promptAllergy = """


Page 2 of 2

-end002421772

Stanford Hospital and Clinics
300 Pasteur Drive
Stanford, CA 94305

NAME: Chase, Jeanine NEW PATIENT VISIT

NUMBER: 177-57-97 ACCOUNT NUMBER: 060017757972
ATTENDING: Michael Fredericson, M.D.

DATE: 06/17/2004

****%* ALLERGIES*****THE PATIENT IS ALLERGIC TO PENICILLIN, THIS CAUSES
SWELLING OF HER AIRWAY AND SHE CANNOT DIGEST WHEAT OR SOY.

IDENTIFICATION: The patient is a 31-year-old female with complaints of right groin pain.

HISTORY OF PRESENT ILLNESS: Ms. Chase comes to clinic today complaining of right groin
pain and tightness. The patient states that she injured her gluteus medius during a yoga position
where she tried to put her right foot behind her head. She feels she also strained her back a little at
the same time. She was evaluated by Dr. Saal on February 15, 2004. He diagnosed her as having
chronic gluteus medius tendinitis as suggested by calcifications adjacent to the greater trochanter on
x-ray. He also did a lumbar spine x-ray, which revealed normal findings. The patient was referred
to a Pilates class for core strengthening and flexibility exercises and she was also referred to the
Sports Medicine Institute for deep tissue massage. She has been going to SMI working with Rob
Finney over the last two years. The patient also notes that she switched for a short time to the
Sports Massage Center and was treated with a Stem machine but felt like her injury was getting
worse so she returned to the Sports Medicine Institute. Today she states her pain level is 0/10. She
states that she would like to return to cycling but notes that activities such as cycling cause a
rubbing sensation in the nght groin area as well as she feels the need for popping her hip frequently.
The patient notes worsening of her symptoms with cycling, prolonged electrical use, and any hip
adductor or hip abductor muscle exercises.

PAST MEDICAL HISTORY: As noted above.
PAST SURGICAL HISTORY: None.
MEDICATIONS: None.

FAMILY HISTORY: The patient’s father is 73 and has stomach problems. Her mother is 63 and
has a bad knee. She has one sibling who is 30 and has stress problems. She had another sibling
who was 30 and had drug and Vicodin problems, who is deceased secondary to suicide. The
patient’s grandparents both have diabetes and are ages 98 and 85.

SOCIAL HISTORY: The patient denies tobacco use or illicit drug use. She states that she drinks

alcohol once a month. She eats a balanced diet and her weight is stable. She was born in California
and currently works as a hair stylist. She lives alone.

nim

Page 1 of 3Original for Scanning

002421772

Stanford Hospital and Clinics
300 Pasteur Drive
Stanford, CA 94305

NAME: Chase, Jeanine NEW PATIENT VISIT

NUMBER: 177-57-97 ACCOUNT NUMBER: 060017757972
ATTENDING: Michael Fredericson, M.D.

DATE: 06/17/2004

REVIEW OF SYSTEMS: The patient is in good general health lately. She notes some recent
weight changes secondary to dietary changes. She otherwise denies other constitutional symptoms.
She denies eyes, ears, nose, mouth, or throat disorders. She denies respiratory, cardiovascular, or
gastrointestinal problems. She denies neurologic, psychiatric, endocrine, hematologic, or lymphatic
disorders. The patient notes some burning with urination but denies any other genitourinary
disorders. The patient notes some changing moles but no other integumentary disorders. She states
she has joint stiffness, pain and cramping, weakness of muscles and joints, and some back pain.
The patient also notes allergic reaction to medications and that she has had her tetanus booster
within the last ten years. Her other immunizations are up to date.

PHYSICAL EXAMINATION: On physical examination the patient is a pleasant woman in no
acute distress. She has genu varus alignment of her lower extremities and pes planus bilaterally
with the too many toes sign bilaterally. She has no pain with single leg squat and no pain with
single leg hop. She is non-tender with resisted hip flexion, hip adduction, or hip abduction. She has
a negative fabere test. She has tenderness of the right paraspinal muscles at the level of L5. She has
pain with internal rotation, hip flexion, and adduction of the right groin. She has a positive Sculler
test. The patient is slightly guarded at the right hip with internal rotation. She has good range of
motion of both hips bilaterally. She has a little snapping in the groin with internal rotation and hip
flexion. The patient is non-tender at the SI joint and sacrurn. The patient has excessive pronation
with ambulation. She has weakness of the hip flexors and hip abductors and a negative Thomas
test. She is non-tender at the greater trochanter on the right. She has a negative femoral cutaneous
stretch test. She has no pain with lumbar forward flexion or hyperextension. She has some
tightness with side bending to the right with rotation.
"""

comp(promptNothing)