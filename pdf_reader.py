import PyPDF2
import re
pdfFileObject = open('The_Living_World.pdf', 'rb')    
pdfReader = PyPDF2.PdfFileReader(pdfFileObject)  
Total_pdf_pages = pdfReader.numPages
print("Total number of pages that this pdf has are")
print(Total_pdf_pages)
User_Input = print("Please enter how any pages you want to fetch from the provided pdf (it starts at zero)") 
user_response = int(input())
for all_pages in range(0,user_response):
    pageObj = pdfReader.getPage(all_pages)
    result = pageObj.extractText()
    result1 = re.sub(r'Aakash Educational Services Pvt. Ltd.', "", result)
    result2 = re.sub(r'- Regd. Office : Aakash Tower, 8, ', "", result1)
    result3 = re.sub(r'Pusa Road,', "", result2)
    result4 = re.sub(r'New Delhi-1',"", result3)
    result5 = re.sub(r'10005 Ph.011-47623456', "", result4)
    print(result5)


''' This is just a way of getting rid of garbage, I could use a better approach but I included all those results for better understanding of the algorithm. This way we can extract data of our choice from the pdf of our choice'''
