"""
pdf extract
"""

import PyPDF2
import re

# assign file

file_name = "ruka_Q.pdf"
pdf = open(file_name, "rb")
doc = PyPDF2.PdfFileReader(file_name)


# number of pages
totalPages = doc.numPages
print(totalPages)

# extract text
page = doc.getPage(0)
print(page.extractText())

# search term
