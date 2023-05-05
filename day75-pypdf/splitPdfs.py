import PyPDF2 as pdf
import os
from pathlib import Path

# Get the directory of the current script file
cur_dir = os.path.dirname(os.path.realpath(__file__))


python_pdf = os.path.join(cur_dir, 'python-basics-sample-chapters.pdf')
some_pdf = os.path.join(cur_dir, 'output.pdf')

# to split pdf into multiple pdf pages
def split_pdf(pdf_path):
    if os.path.exists(pdf_path):
        if not pdf_path.endswith('.pdf'):
            print('Not a pdf file')
            return None
        with open(pdf_path, 'rb') as f:
            reader = pdf.PdfReader(f)
            # get all pages
            for page in range(0, len(reader.pages)):
                selected_page = reader.pages[page]
                # writer to write
                writer = pdf.PdfWriter()
                writer.add_page(selected_page) # embading of the page
                filename = os.path.splitext(pdf_path)[0]
                output_filename = f"{filename}_{page}.pdf"
                # save and compile to pdf
                with open(output_filename, "wb") as out:
                    writer.write(out)
                print(f"created a pdf:{output_filename}")
                return None

    print("No file found")
    return None

# split_pdf(python_pdf)

# split a pdf upto a page
def get_pdf_upto(pdf_path, start_page: int = 0, stop_page: int = 0, output_path=cur_dir):
    if os.path.exists(pdf_path):
        if not pdf_path.endswith('.pdf'):
            print('Not a pdf file')
            return None
        if not output_path:
            output_path = str(Path(pdf_path).parent)
        with open(pdf_path, 'rb') as f:
            reader = pdf.PdfReader(f)
            if start_page > len(reader.pages) or stop_page > len(reader.pages):
                print('Start and Stop page must be less than or equal to total pdf pages')
                return None
            # writer to write
            writer = pdf.PdfWriter()
            # get all pages
            for page in range(start_page, stop_page):
                selected_page = reader.pages[page]
                writer.add_page(selected_page) # embading of the page
            #basename will get the file name only then splittext split into two parts
            filename = os.path.splitext(os.path.basename(pdf_path))[0]
            output_filename = f"{output_path}/{filename}_from_{start_page}_to_{stop_page}.pdf"
            with open(output_filename, 'wb') as out:
                writer.write(out)

            return None

    print("No file found")
    return None

get_pdf_upto(some_pdf, 1, 4)

def get_last_pdf_page(pdf_path):
    if os.path.exists(pdf_path):
        if not pdf_path.endswith('.pdf'):
            print('Not a pdf file')
            return None
        with open(pdf_path, 'rb') as f:
            reader = pdf.PdfReader(f)
            # writer to write
            writer = pdf.PdfWriter()
            last_page = len(reader.pages)-1
            selected_page = reader.pages[last_page]
            writer.add_page(selected_page)
            filename = os.path.splitext(pdf_path)[0]
            output_filename = f"{filename}_last_page.pdf"
            with open(output_filename, 'wb') as out:
                writer.write(out)
            print("Done!")
            return None

    print("No file found")
    return None

# get_last_pdf_page(python_pdf)
