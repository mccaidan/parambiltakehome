import json
from openai import OpenAI
client = OpenAI(api_key='')

def comp(PROMPT=''):
    print('Function called')
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
    

prompt = """which medications are listed here, with just their start date and end date, using None for unknown: Tab08/20/2020Medication Instructions Qty Status Started Stopped IndicationDoctor
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
10:22 AM"""

comp(prompt)