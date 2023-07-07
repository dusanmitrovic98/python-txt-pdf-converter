import os
from fpdf import FPDF

def convert_to_pdf(input_file):
    filename, extension = os.path.splitext(input_file)
    output_file = filename + ".pdf"

    if extension == ".pdf":
        print("Already a PDF file.")
        return

    if extension == ".txt":
        pdf = FPDF()
        pdf.add_page()

        with open(input_file, "r") as file:
            text_content = file.read()

        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, text_content)

        pdf.output(output_file)
        print("File converted to PDF.")
        return

