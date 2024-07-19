import sys
import platform
from tempfile import TemporaryDirectory
from pathlib import Path
import pytesseract
from pdf2image import convert_from_path
from PIL import Image
#import openai
#openai.api_key = '<API_KEY>'

outdir = Path(__file__).parent.resolve() # Directory of script
text_file = outdir / Path("out_text.txt")

# Store all the pages of the PDF in a variable
image_file_list = []

def main(pdfName):
    pdfLocation = str(outdir) + '/' + pdfName

    with TemporaryDirectory() as tempdir:

        pdf_pages = convert_from_path(pdfLocation, 500)
        # Read in the PDF file at 500 DPI

        for page_enumeration, page in enumerate(pdf_pages, start=1):
            filename = f"{tempdir}/page_{page_enumeration:03}.jpg"

            # Save the image of the page in system
            page.save(filename, "JPEG")
            image_file_list.append(filename)

        with open(text_file, "a") as output_file:
            # Open the file in append mode

            for image_file in image_file_list:
                # Recognize the text as string in image using pytesserct
                text = str(((pytesseract.image_to_string(Image.open(image_file)))))
                text = text.replace("-\n", "")
                output_file.write(text)

if __name__ == "__main__":
    main(sys.argv[1])