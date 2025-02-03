import PyPDF2
import os
import uuid

print("Rozpoczęcie procesu...")
merger = PyPDF2.PdfMerger()

for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
        print(f"Dodawanie pliku: {file}")
        merger.append(file)

output_filename = "Razem.pdf"
merger.write(output_filename)
merger.close()
print(f"Proces zakończony. Plik {output_filename} został utworzony.")

