import PyPDF2
from pathlib import Path

outdir = Path(__file__).parent.resolve()
text_file = outdir / Path("out_text2.txt")

read_pdf = PyPDF2.PdfReader('SampleHealthRecord_Redacted.pdf')

with open(text_file, "a") as output_file:
    for page in read_pdf.pages:
        output_file.write(page.extract_text())
        print(page.extract_text())

# Not bad at converting to text, but only saw 1 "SURGERY", so probably not the best choice for this