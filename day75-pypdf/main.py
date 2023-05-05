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
    # info = reader.metadata
    # print(info)

    # number of pages in pdf file
    # prev reader.getNumPages()
    # print(len(reader.pages))

    # to extract text
    # prev reader.pages[0].extractText()
    # print(reader.pages[2].extract_text())

# function to get metadata
def get_pdf_metadata(file_path):
    if os.path.exists(python_pdf):
        with open(file_path, 'rb') as f:
            reader = pdf.PdfReader(f)
            info = reader.metadata
        return info
    print("No pdf file found!")
    return None

def extract_text_from_pdf(file_path):
    if os.path.exists(python_pdf):
        with open(file_path, 'rb') as f:
            reader = pdf.PdfReader(f)
            results = []
            for page in range(0, len(reader.pages)):
                selected_page = reader.pages[page]
                text = selected_page.extract_text()
                results.append(text)
            return ' '.join(results)
    print("No pdf file found!")
    return None

resume_pdf = os.path.join(cur_dir, 'Muhammad\'s Resume.pdf')
print(get_pdf_metadata(resume_pdf))
print(extract_text_from_pdf(resume_pdf))
