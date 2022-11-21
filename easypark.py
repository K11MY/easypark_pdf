from PyPDF2 import PdfFileReader
import os 
import re
import glob

def extract_pdf(file_path): 
    # Get receipts
    receipts = os.listdir(file_path)
    # Set the regex pattern to read the file 
    pattern = r'[\d]{4}.[\d]{1,2}.[\d]{1,2}'
    # Iterate through the receipts list
    for receipt in receipts:
        # Read the pdf 
        pdf = PdfFileReader(file_path + receipt)
        # Read the first page
        page = pdf.pages[0]
        # Extract the text from the pdf
        text = page.extract_text()
        # extract all dates from the pdf
        extract_date = re.findall(pattern, text)
        # replace the '.' in the date with no spaces
        date = extract_date[3].replace('.','')
        # rename the file
        os.rename(file_path + receipt, file_path + 'Parking_'+date+'.pdf')

if __name__ == "__main__":
    # File path must have the "/" at the end to read all parking files
    file_path = "Easypark/"
    extract_pdf(file_path)



