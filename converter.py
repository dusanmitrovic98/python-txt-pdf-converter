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

    print("Conversion not supported.")


def convert_from_pdf(input_file):
    filename, extension = os.path.splitext(input_file)
    output_file = filename + ".docx"

    if extension == ".pdf":
        if os.system("pdftotext -v") == 0:
            os.system(f"pdftotext {input_file} {output_file}")
            print("File converted from PDF.")
            return

        print("pdftotext utility not found. Conversion from PDF not supported.")
        return
    
    print("Conversion not supported.")

# Specify the file path here
file_path = "file.txt"

# Convert to PDF
convert_to_pdf(file_path)

# Convert from PDF
# convert_from_pdf(file_path)
