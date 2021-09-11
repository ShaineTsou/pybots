# Watermark all the files
import PyPDF2
import sys
import os

inputs = sys.argv[1:len(sys.argv) - 1]
watermark = sys.argv[len(sys.argv) - 1]


def create_watermark(inputs, watermark):
    watermark_page = PyPDF2.PdfFileReader(watermark).getPage(0)

    for pdf in inputs:
        pdf_reader = PyPDF2.PdfFileReader(pdf)
        pdf_writer = PyPDF2.PdfFileWriter()
        root = os.path.splitext(pdf)[0]

        for page in range(pdf_reader.getNumPages()):
            page = pdf_reader.getPage(page)
            page.mergePage(watermark_page)
            pdf_writer.addPage(page)

        with open(f'{root}-watermarked.pdf', 'wb') as output:
            pdf_writer.write(output)


if __name__ == '__main__':
    create_watermark(inputs, watermark)
