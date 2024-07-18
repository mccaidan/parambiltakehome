# Parambil Take Home

## Tool Usage
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
```
~~pip install PyPDF2~~

## Road Map
1. Python script that takes a PDF document as an argument
2. Use PDF processing library to convert PDF to text
3. Call third party LLM API with questions and the PDF as text
4. Receive answers from API response
5. Write answers to .docx underneath respective questions

## Assumptions
* The information in the PDF is about one person
* Security of the third party LLM API is not a concern
* The input of the PDF can be a command line argument, as it's cleaner than using the input() function

## Limitations
* This tool can only handle one PDF at a time in its current state, but could handle multiple with some minor tweaks
* The questions asked to the third party API are hardcoded, which lacks flexibility for future queries without manual changes
* Non-character information in the PDF will not get translated to text well


## Future Options
Could use Unstructured package: https://unstructured.io/blog/how-to-process-pdf-in-python

Could directly process PDFs with some of these products and their APIs:
* https://pdf.ai/
* https://www.chatpdf.com/
* https://www.veryfi.com/
