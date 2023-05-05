import PyPDF2 as pdf
import os

# Get the directory of the current script file
cur_dir = os.path.dirname(os.path.realpath(__file__))

def fetch_all_pdf_files(parent_folder: str):
    target_files = []
    for path, subdirs, files in os.walk(parent_folder):
        for name in files:
            if name.endswith(".pdf"):
                target_files.append(os.path.join(path, name))
    return target_files

pdf_path_folder = os.path.join(cur_dir, "test")

# print(fetch_all_pdf_files(pdf_path_folder))

def merge_pdf(list_of_pdfs, output_filename):
    merger = pdf.PdfMerger()
    with open(output_filename, 'wb') as output:
        for file in list_of_pdfs:
            merger.append(file)
        merger.write(output)

pdf_path_list = fetch_all_pdf_files(pdf_path_folder)
output_path = os.path.join(cur_dir, 'merged.pdf')

merge_pdf(pdf_path_list, output_path)
    
