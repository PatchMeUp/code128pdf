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

def generatePdf(codes: list):
    for code in codes:
        x = re.findall('[0-9]+', code)
        text = re.findall('[A-Za-z]+', code)
        fv = Canvas(code + ".pdf", pagesize=A4)
        draw(fv, code)

def main():
    codes = ['tsl12345',
'TSL21 ',
'tsl220',
'tsl221',
'tsl222',
'TSL244',
'TSL25 ',
'tsl263',
'TSL263',
'tsl264',
'TSL264',
'tsl265',
'tsl265',
'tsl266',
'tsl268',
'tsl268',
'tsl269',
'TSL282',
'TSL301',
'tsl303',
'TSL304',
'TSL37',
'TSL8 ']
    generatePdf(codes)


if __name__ == '__main__':
    main()

