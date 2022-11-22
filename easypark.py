from PyPDF2 import PdfReader
from glob import glob
from os import rename
from re import findall

def extract_pdf(filePath): 
    # Get receipts
    receipts = glob(filePath+"Parking_*.pdf")
    # Date pattern
    datePattern = r'\d{4}\.\d{2}\.\d{2}'
    # Price pattern
    pricePattern = r'\d{1,2}\.\d{2} AUD'
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
        # Extract price 
        extractPrice = findall(pricePattern, text)
        # Get date and replace the '.' in the date with no spaces
        date = extractDate[1].replace('.','')
        # Clean up the price and leave it as cents.
        price = extractPrice[0].replace('.','').replace(' AUD','')
        # Rename the file as Parking_date_startTime_endTime.pdf
        rename(receipt, filePath + 'Parking_' + date + '_' + price +'.pdf')

if __name__ == "__main__":
    # File path must have the "/" at the end to read all parking files
    filePath = "Easypark/"
    extract_pdf(filePath)


