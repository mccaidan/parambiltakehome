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
    

prompt = """which allergies are listed here: Page 2 of 2

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
tightness with side bending to the right with rotation."""

comp(prompt)