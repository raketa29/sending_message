import pyAesCrypt
from PyPDF3 import PdfFileWriter, PdfFileReader
from getpass import getpass

# password = input("Input password to the file crypt:   ").strip()

# pyAesCrypt.encryptFile("data.txt", "data.txt.aes", password)

# pyAesCrypt.decryptFile("data.txt.aes", "data.txt", password)


pdfwriter = PdfFileWriter()
pdf = PdfFileReader("git-cheat-sheet-education.pdf")

for page in range(pdf.numPages):
    pdfwriter.addPage(pdf.pages[page])

password = getpass(prompt="Input password: ", stream=None)

pdfwriter.encrypt(password)

with open("protected.pdf", "wb") as file:
    pdfwriter.write(file)

