#!/usr/bin/env python3

"""
A simple Python application that reads EasyPark PDF receipts, and renames the files
"""
import argparse
import sys

from datetime import date, datetime
from PyPDF2 import PdfReader
from glob import glob
from os import rename, path
from re import compile

DATE_PATTERN = compile(r"\d{4}\.\d{2}\.\d{2}")
PRICE_PATTERN = compile(r"\d{1,2}\.\d{2} AUD")

PARSER = argparse.ArgumentParser(
    prog="EasyPark - PDF",
    description="Renames EasyPark PDFs",
    epilog="Any issues, contact Kim!",
)

PARSER.add_argument("-d", "--dir", default="easypark", dest="receipt_dir")

ARGS = PARSER.parse_args()


def rename_pdf(directory_path, receipt):
    """
    extracts and parses a PDF

    :directory_path: path to EasyPark receipts directory
    :receipt: the receipt to rename
    """
    pdf = PdfReader(receipt, strict=False)
    page = pdf.pages[0]
    text = page.extract_text()

    extractDate = DATE_PATTERN.findall(text)
    extractPrice = PRICE_PATTERN.findall(text)

    pdf_date = date.strftime(datetime.strptime(extractDate[1], "%Y.%m.%d"), "%Y-%m-%d")
    pdf_price = extractPrice[0].replace(".", "").replace(" AUD", "")

    rename_args = directory_path + "parking_" + pdf_date + "_" + pdf_price + ".pdf"

    # Rename the file as `parking_date_price.pdf`
    rename(receipt, rename_args)
    print('Successfully renamed: "%s" to "%s"' % (receipt, rename_args))


def main():
    # File path must have the "/" at the end to read all parking files
    directory_path = path.join(ARGS.receipt_dir, "")
    print("Looking for receipts in: %s" % (directory_path))

    receipts = glob(directory_path + "Parking_*.pdf")

    if not receipts:
        print("No receipts found. Exiting.")
        sys.exit(1)

    for receipt in receipts:
        rename_pdf(directory_path, receipt)


if __name__ == "__main__":
    main()
