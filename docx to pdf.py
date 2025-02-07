import win32com.client
import docx
for file in os.listdir(os.curdir):
    if file.endswith(".docx"):

doc.save(wordFilename)

wdFormatPDF = 17
wordObj = win32com.client.Dispatch('Word.Application')
docObj = wordObj.Documents.Open(wordFilename)
docObj.SaveAs(pdfFilename, FileFormat=wdFormatPDF)
docObj.Close()
wordObj.Quit()