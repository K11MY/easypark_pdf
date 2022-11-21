from PyPDF2 import PdfReader
from glob import glob
from os import rename
from re import findall

def extract_pdf(file_path): 
    # Get receipts
    receipts = glob(file_path+"Parking_*.pdf")
    # Date pattern
    datePattern = r'\d{4}\.\d{2}\.\d{2}'
    # Time pattern 
    timePattern = r'\d{2}\:\d{2}'
    # Iterate over the receipts list 
    for receipt in receipts:
        # Read the pdf 
        pdf = PdfReader(receipt, strict=False)
        # Read the first page
        page = pdf.pages[0]
        # Extract the text from the pdf
        text = page.extract_text()
        # Extract all dates from the pdf
        extractDate = findall(datePattern, text)
        # Extract time 
        extractTime = findall(timePattern, text)
        # Get date and replace the '.' in the date with no spaces
        date = extractDate[1].replace('.','')
        # Get start time / end time and replace ':' with no space
        startTime = extractTime[0].replace(':','')
        endTime = extractTime[1].replace(':','')
        # Rename the file as Parking_date_startTime_endTime.pdf
        rename(receipt, file_path + 'Parking_'+date+'_'
                    + startTime + '_' + endTime +'.pdf')

if __name__ == "__main__":
    # File path must have the "/" at the end to read all parking files
    file_path = "Easypark/"
    extract_pdf(file_path)


