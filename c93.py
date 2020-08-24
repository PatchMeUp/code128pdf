from reportlab.graphics.barcode import code128
from reportlab.graphics.barcode import code93
from reportlab.lib.units import mm
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import A4
from reportlab.graphics import renderPDF
import sys, getopt, re

def draw(canvas: Canvas, code: str):
    canvas.setPageSize(A4)
    canvas.bottomup = 1
    canvas.drawString(100,750,"Dokument testowy " + code)
    #barcode = code128.Code128(code)
    barcode = code93.Standard93(code)
    barcode.drawOn(canvas, 100, 600)
    canvas.setFontSize(8)
    canvas.drawString(118, 590, code)
    canvas.showPage()
    canvas.save()

def generatePdf(initcode: str, count: int):
    x = re.findall('[0-9]+', initcode)
    text = re.findall('[A-Za-z]+', initcode)
    counter = int(x[0])
    for i in range(counter, counter + count):
        fv = Canvas(text[0] + str(i) + ".pdf", pagesize=A4)
        draw(fv, text[0] + str(i))

def main():
    try:
        args = sys.argv[1:]
        if sys.argv[1] == '-h':
            print (f"Usage: {sys.argv[0]} <12 digits code> <count - how many labels to generate>")
            sys.exit()
        if sys.argv[1:] is None:
            print (f'Usage: {sys.argv[0]} <12 digits code> <count - how many labels to generate>')
            sys.exit()
        #elif len(sys.argv[1]) != 12:
        #    print('First argument has to be a 12 digit number')
        #    sys.exit()
        elif int(sys.argv[2]) > 200:
            print('Well, lets not exagerrate')
            sys.exit()

    except IndexError:
        raise SystemExit(f"Usage: {sys.argv[0]} <12 digits code> <count - how many labels to generate>")

    generatePdf(sys.argv[1], int(sys.argv[2]))


if __name__ == '__main__':
    main()

