import sys
import platform
import pytesseract
from pdf2image import convert_from_path
from PIL import Image
from tempfile import TemporaryDirectory
from pathlib import Path
import openai

openai.api_key = '<API_KEY>'
outdir = Path(__file__).parent.resolve() # Directory of script

def main(pdfName):
    print(pdfName)
    print(outdir)

if __name__ == "__main__":
    main(sys.argv[1])