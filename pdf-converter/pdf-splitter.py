# Usage: python3 pdf-splitter.py [file]

from PyPDF2 import PdfFileReader, PdfFileWriter
from pathlib import Path
import sys

file = sys.argv[1]
file_name = Path(file).stem


def split_pdf(file):
    pdf_reader = PdfFileReader(file)

    for page in range(pdf_reader.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf_reader.getPage(page))

        output = f'{file_name}-p{page + 1}.pdf'
        with open(output, 'wb') as output_pdf:
            pdf_writer.write(output_pdf)


if __name__ == '__main__':
    split_pdf(file)
