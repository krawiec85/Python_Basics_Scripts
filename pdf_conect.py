import PyPDF2, os

from pdf_page_connector import pdfWriter, pdfFiles

for filename in pdfFiles:
    if filename.endswith('.pdf'):
        print(f'Processing {filename}...')
        pdfReader = PyPDF2.PdfFileReader(open(filename, 'rb'))
        numPages = pdfReader.numPages
        print(f'Number of pages: {numPages}')
pdfOutput = open('output.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()
