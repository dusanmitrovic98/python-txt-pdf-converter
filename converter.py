import os
from fpdf import FPDF

def convert_to_pdf(input_file):
    filename, extension = os.path.splitext(input_file)
    output_file = filename + ".pdf"

    if extension == ".pdf":
        print("Already a PDF file.")
