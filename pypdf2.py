import PyPDF2
read_pdf = PyPDF2.PdfReader('SampleHealthRecord_Redacted.pdf')
for page in read_pdf.pages: print(page.extract_text())

# Prompt: which medications are listed here, with their start date and end date:


# Not bad at converting to text, aim for better