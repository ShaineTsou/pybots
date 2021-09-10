# Usage: python3 pdf-merger.py [file_1], [file_2], [file_3]...

import PyPDF2
import sys

# Store input file into files
inputs = sys.argv[1:]


def merge_pdfs(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)

    merger.write('merged.pdf')


if __name__ == '__main__':
    merge_pdfs(inputs)
