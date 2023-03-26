import PyPDF2
import os

path = r"C:\Users\Abhishek Bajpai\Documents\Velocitai digital\PythonDSA\Advanced Concepts\pyPDF\first.pdf"
if not os.path.exists(path):
    print(path, " not found")
    exit(0)
with open(path, "rb") as file:
    #ReadBinary very important
    reader=PyPDF2.PdfReader(file)
    print(len(reader.pages))
    page=reader.pages[0]
    page.rotate(90)
    
    writer=PyPDF2.PdfWriter()
    writer.add_page(page)
    
    with open("rotated.pdf", "wb") as output:
        writer.write(output)

