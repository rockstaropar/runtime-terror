from PyPDF2 import PdfReader
reader = PdfReader("/storage/emulated/0/Download/CBSE-RESULT-2022.pdf")
page = reader.pages[0]
text = page.extract_text()
print(text)