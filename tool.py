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

surgeriesDict = {}
medicationsDict = {}
allergiesDict = {}

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


def addToSurgeriesDict(surgeryNameLower, surgeryDate, pageNum):
    if surgeryNameLower in surgeriesDict:
        surgeriesDict[surgeryNameLower]['datesList'].append(surgeryDate)
        surgeriesDict[surgeryNameLower]['pagesList'].append(pageNum)
    else:
        surgeriesDict[surgeryNameLower] = {
            'datesList': [surgeryDate],
            'pagesList': [pageNum]
        }
    print('Added to surgeries: ', (surgeryNameLower, surgeryDate, pageNum))


def processSurgeriesDict(sDict, pageNum, text):
    if 'surgeries' in sDict:
        if isinstance(sDict['surgeries'], list):
            for s in sDict['surgeries']:
                if isinstance(s, dict):
                    if 'surgery' in s and 'date' in s:
                        #print('potential surgery: ', s['surgery'])
                        if s['surgery'].lower() in text.lower():
                            addToSurgeriesDict(s['surgery'].lower(), s['date'], pageNum)


def addToMedicationsDict(medicationNameLower, startDate, endDate, pageNum):
    if medicationNameLower in medicationsDict:
        medicationsDict[medicationNameLower]['datesList'].append((startDate, endDate))
        medicationsDict[medicationNameLower]['pagesList'].append(pageNum)
    else:
        medicationsDict[medicationNameLower] = {
            'datesList': [(startDate, endDate)],
            'pagesList': [pageNum]
        }
    print('Added to medications: ', (medicationNameLower, startDate, endDate, pageNum))


def processMedicationsDict(mDict, pageNum, text):
    if 'medications' in mDict:
        if isinstance(mDict['medications'], list):
            for m in mDict['medications']:
                if isinstance(m, dict):
                    if 'medication' in m and 'startDate' in m and 'endDate' in m:
                        #print('potential medication: ', m['medication'])
                        if m['medication'].lower() in text.lower():
                            addToMedicationsDict(m['medication'].lower(), m['startDate'], m['endDate'], pageNum)


def addToAllergiesDict(allergyNameLower, pageNum):
    if allergyNameLower in allergiesDict:
        allergiesDict[allergyNameLower]['pagesList'].append(pageNum)
    else:
        allergiesDict[allergyNameLower] = {
            'pagesList': [pageNum]
        }
    print('Added to allergies: ', (allergyNameLower, pageNum))


def processAllergiesDict(aDict, pageNum, text):
    if 'allergies' in aDict:
        if isinstance(aDict['allergies'], list):
            for a in aDict['allergies']:
                if isinstance(a, dict):
                    if 'allergyName' in a:
                        #print('potential allergy: ', a['allergyName'])
                        if a['allergyName'].lower() in text.lower():
                            addToAllergiesDict(a['allergyName'].lower(), pageNum)


def printDicts():
    print()
    print(json.dumps(surgeriesDict, indent=4))
    print('------------------------------------------------------------')
    print(json.dumps(medicationsDict, indent=4))
    print('------------------------------------------------------------')
    print(json.dumps(allergiesDict, indent=4))
    print('------------------------------------------------------------')

def writeDicts():
    with open('program_dicts.txt', "a") as output_file:
        output_file.write(json.dumps(surgeriesDict, indent=4))
        output_file.write('------------------------------------------------------------')
        output_file.write(json.dumps(medicationsDict, indent=4))
        output_file.write('------------------------------------------------------------')
        output_file.write(json.dumps(allergiesDict, indent=4))

def writeToWordDoc():
    # TODO WRITE OUTPUT FILE HERE
    pass

def main(pdfName):
    outdir = Path(__file__).parent.resolve()
    #text_file = outdir / Path("out_text.txt")
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
                processSurgeriesDict(getDictionaryResponseFromAPI(prompt), pageNumber, text)
                
                # Medications Section
                prompt = f"""{PROMPT_MEDICATIONS} {text}"""
                processMedicationsDict(getDictionaryResponseFromAPI(prompt), pageNumber, text)
                
                # Allergies Section
                prompt = f"""{PROMPT_ALLERGIES} {text}"""
                processAllergiesDict(getDictionaryResponseFromAPI(prompt), pageNumber, text)
                
                print(pageNumber)
                pageNumber += 1
                
                # if (pageNumber == 32):
                #     printDicts()
                #     writeDicts()
                #     print('DONE')
                #     quit()

        printDicts()
        writeDicts()
        
        writeToWordDoc()

if __name__ == "__main__":
    main(sys.argv[1])
