# Parambil Take Home

## Road Map
1. Python script that takes a PDF document as an argument
2. Use PDF processing library to convert PDF to text
3. Call third party LLM API with questions and the PDF as text
4. Receive answers from API response
5. Write answers to .docx underneath respective questions

## Assumptions
* The information in the PDF is about one person
* Security of the third party LLM API is not a concern

## Limitations
* This tool can only handle one PDF at a time in its current state, but could handle multiple with some minor tweaks
* The questions asked to the third party API are hardcoded, which lacks flexibility for future queries without manual changes