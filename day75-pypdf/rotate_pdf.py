import PyPDF2 as pdf
import os

# Get the directory of the current script file
cur_dir = os.path.dirname(os.path.realpath(__file__))

def rotate_pdf(pdf_path, output_path = cur_dir, page_num: int = 0, rotation: int = 90):

    if rotation%90 != 0:
        print("Rotation must be multiple of 90")
        return None

    if os.path.isfile(pdf_path) and pdf_path.endswith('.pdf'):
        with open(pdf_path, 'rb') as f:
            reader = pdf.PdfReader(f)
            writer = pdf.PdfWriter()
            writer.add_page(reader.pages[page_num])
            # to rotate
            writer.pages[page_num].rotate(rotation)
            #basename will get the file name only then splittext split into two parts
            filename = os.path.splitext(os.path.basename(pdf_path))[0]
            output_filename = f"{output_path}/{filename}_{rotation}_rotated.pdf"
            with open(output_filename, 'wb') as out:
                writer.write(out)
            print("rotated successfully")
    else:
        print("no pdf file found")

pdf_path = os.path.join(cur_dir, 'output.pdf')
rotate_pdf(pdf_path, rotation=270)