from reportlab.graphics.barcode import code128
from reportlab.lib.units import mm
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import A4
from reportlab.graphics import renderPDF
import sys, getopt

def draw(canvas: Canvas, code: int):
    canvas.setPageSize(A4)
    canvas.bottomup = 1
    canvas.drawString(100,750,"Faktura testowa " + str(code))
    barcode = code128.Code128(code)
    barcode.drawOn(canvas, 100, 600)
    canvas.setFontSize(8)
    canvas.drawString(118, 590, str(code))
    canvas.showPage()
    canvas.save()

def generatePdf(intitcode: int, count: int):
    for i in range(count):
        fv = Canvas("fv" + str(intitcode + i) + ".pdf", pagesize=A4)
        draw(fv, i)

def main():
    try:
        args = sys.argv[1:]
        if sys.argv[1] == '-h':
            print (f"Usage: {sys.argv[0]} <12 digits code> <count - how many labels to generate>")
            sys.exit()
        if sys.argv[1:] is None:
            print (f'Usage: {sys.argv[0]} <12 digits code> <count - how many labels to generate>')
            sys.exit()
        elif len(sys.argv[1]) != 12:
            print('First argument has to be a 12 digit number')
            sys.exit()
        elif int(sys.argv[2]) > 20:
            print('Well, lets not exagerrate')
            sys.exit()

    except IndexError:
        raise SystemExit(f"Usage: {sys.argv[0]} <12 digits code> <count - how many labels to generate>")

    generatePdf(int(sys.argv[1]), int(sys.argv[2]))


if __name__ == '__main__':
    main()

