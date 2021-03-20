/#install PyPDF2 module(pip install PyPDF2)
import PyPDF2
pdf=input('enter pdf path: ')
a=PyPDF2.PdfFileReader(pdf)
print('document info: ')
print(a.documentInfo)
no=a.getNumPages()
print('total pages: ')
print(no)
string =""
for i in range(1,no):
    string += a.getPage(i).extractText()

with open("text.txt","w",encoding='utf-8') as f:
    f.write(string)
print('pdf converted to text sucessfully.....')