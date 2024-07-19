import sys
from tempfile import TemporaryDirectory
from pathlib import Path
import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import json
from openai import OpenAI

client = OpenAI(api_key='')

PROMPT_SURGERIES = 'Using only this text, which surgeries are listed here, with their date, using None for unknown. If no surgeries return empty JSON. Use key of surgeries to a list of surgery key and date key: '
PROMPT_MEDICATIONS = 'Using only this text, which medications are listed here, with just their start date and end date, using None for unknown. If no medications return empty JSON. Use key of medications to a list of medication key and startDate key and endDate key: '
PROMPT_ALLERGIES = 'Using only this text, which allergies are listed here. If no allergies return empty JSON. Use key of allergies to a list of only allergyName key: '

surgeriesList = []
medicationsList = []
allergiesList = []

# RETURNS the dictionary of the API response to the prompt
def getDictionaryResponseFromAPI(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        response_format={ "type": "json_object" },
        messages=[
            {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
            {"role": "user", "content": prompt}
        ]
    )
    respDict = json.loads(response.choices[0].message.content)
    return respDict


def processSurgeriesDict(sDict, pageNum):
    if 'surgeries' in sDict:
        if isinstance(sDict['surgeries'], list):
            for s in sDict['surgeries']:
                if isinstance(s, dict):
                    if 'surgery' in s and 'date' in s:
                        tup = (s['surgery'], s['date'], pageNum)
                        surgeriesList.append(tup)
                        print('appended to surgeries: ', tup)


def processMedicationsDict(mDict, pageNum):
    if 'medications' in mDict:
        if isinstance(mDict['medications'], list):
            for m in mDict['medications']:
                if isinstance(m, dict):
                    if 'medication' in m and 'startDate' in m and 'endDate' in m:
                        tup = (m['medication'], m['startDate'], m['endDate'], pageNum)
                        medicationsList.append(tup)
                        print('appended to medications: ', tup)


def processAllergiesDict(aDict, pageNum):
    if 'allergies' in aDict:
        if isinstance(aDict['allergies'], list):
            for a in aDict['allergies']:
                if isinstance(a, dict):
                    if 'allergyName' in a:
                        tup = (a['allergyName'], pageNum)
                        allergiesList.append(tup)
                        print('appended to allergies: ', tup)


def printLists():
    print(surgeriesList)
    print('------------------------------------------------------------')
    print(medicationsList)
    print('------------------------------------------------------------')
    print(allergiesList)
    print('------------------------------------------------------------')

def writeToWordDoc():
    # TODO WRITE OUTPUT FILE HERE
    pass

def main(pdfName):
    outdir = Path(__file__).parent.resolve()
    text_file = outdir / Path("out_text.txt")
    pdfLocation = str(outdir) + '/' + pdfName
    
    image_file_list = []
    
    with TemporaryDirectory() as tempdir:
        pdf_pages = convert_from_path(pdfLocation, 500)
        
        for page_enumeration, page in enumerate(pdf_pages, start=1):
            filename = f"{tempdir}/page_{page_enumeration:03}.jpg"
            page.save(filename, "JPEG")
            image_file_list.append(filename)
        
        pageNumber = 1
        for image_file in image_file_list:
                text = str(((pytesseract.image_to_string(Image.open(image_file)))))
                text = text.replace("-\n", "")
                
                # Surgeries Section
                prompt = f"""{PROMPT_SURGERIES} {text}"""
                processSurgeriesDict(getDictionaryResponseFromAPI(prompt), pageNumber)
                
                # Medications Section
                prompt = f"""{PROMPT_MEDICATIONS} {text}"""
                processMedicationsDict(getDictionaryResponseFromAPI(prompt), pageNumber)
                
                # Allergies Section
                prompt = f"""{PROMPT_ALLERGIES} {text}"""
                processAllergiesDict(getDictionaryResponseFromAPI(prompt), pageNumber)
                
                pageNumber += 1
                
                val = input("Press y to print lists, n otherwise [y/n]: ")
                if val == 'y':
                    printLists()
        
        writeToWordDoc()

if __name__ == "__main__":
    main(sys.argv[1])
    
    
#with open(text_file, "a") as output_file:
#    # Open the file in append mode
#    output_file.write(text)