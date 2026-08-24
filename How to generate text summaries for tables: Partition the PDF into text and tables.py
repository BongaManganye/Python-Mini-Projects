#RAG python
# How to generate text summaries for tables: Partition the PDF into text and tables

import os
from unstructured.partition.pdf import partition_pdf

pdf_file_path ="../datasets/pdf_files/adult_data_article.pdf"

tables = []
texts = []

#partition the PDF file into its elements
raw_pdf_elemets = partition_pdf(
    filename=raw_pdf_elements = partition_pdf(
        filename=pdf_file_path,
        strategy="hi_res",
)

for element in raw_pdf_elements:
    if "unstructured".documents.elements.Table" in
str(type(element)):
        tables.append(str(element))
)
