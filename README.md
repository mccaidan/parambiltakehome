# Parambil Take Home

## Tool Usage
After adding in your OpenAI API key in line 11
```
python3 tool.py <Full_PDF_Name_Here>
```
### Commands run in setup
```
python3 -m venv ./env
source env/bin/activate
pip install pytesseract
pip install pdf2image
pip install openai
pip install python-docx
brew install poppler
brew install tesseract
```

### Code from
https://www.geeksforgeeks.org/python-reading-contents-of-pdf-using-ocr-optical-character-recognition/

## General Road Map
1. Python script that takes a PDF document as a command line argument
2. Uses PDF processing library to convert PDF to text
3. Calls third party LLM API (OpenAI) with prompts and resultant text from PDF
4. Receives answers from API response
5. Writes answers to .docx underneath respective questions

## Assumptions
* The information in the PDF is about one person
* Security of the third party LLM API is not a concern
* The input of the PDF can be a command line argument, as it's cleaner than using the input() function
* Tool won't be run on Windows OS
* PDF is in same directory as script

## Limitations
* This tool can only handle one PDF at a time in its current state, but could handle multiple with some minor tweaks
* The data sent to the API is in text only, which loses information from charts and other visuals
* The prompts sent to the third party API are hardcoded, which lacks flexibility for future queries without manual changes
* OpenAI's engine is not quite good enough at recognizing surgeries, medications, and allergies, so there is a lot of junk in its output, as well as many of the same things listed just with slight differences in name
* Non-character information in the PDF will not get translated to text well


## Future Options/Next Steps
* Add functionality to handle multiple PDFs and multiple output Word docs
* Add ability for user to modify the prompts
* Do more prompt engineering to get better responses
* Use Unstructured package for better data extraction from the PDF: https://unstructured.io/blog/how-to-process-pdf-in-python
* Directly process PDFs with some of these products and their APIs:
    * https://pdf.ai/
    * https://www.chatpdf.com/
    * https://www.veryfi.com/
* Do image preprocessing with numpy and opencv before using OpenAI API to have better data sent to the LLM
* Use threading to increase efficiency instead of waiting for each page processing and each API call to return in order
* Match API response data against lists of known surgeries, medications, and allergies to ensure there are no irrelevant results
* Train an LLM on similar data so it can give better responses in this field
