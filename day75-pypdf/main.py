import PyPDF2 as pdf
import os

# Get the directory of the current script file
cur_dir = os.path.dirname(os.path.realpath(__file__))

python_pdf = os.path.join(cur_dir, 'python-basics-sample-chapters.pdf')
if os.path.exists(python_pdf):
    # get info of the open pdf file
    file = open(python_pdf, 'rb')
    reader = pdf.PdfReader(file)
    # before 3.0.0 version we use reader.getDocumentInfo()
    info = reader.metadata
    print(info)

    # number of pages in pdf file
    # prev reader.getNumPages()
    print(len(reader.pages))

    # to extract text
    # prev reader.pages[0].extractText()
    print(reader.pages[2].extract_text())
