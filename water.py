######## 基础准备 ########
import os

os.getcwd()
os.chdir('D:\\Download\\water\\manage')
os.getcwd()  # 获取当前工作目录

from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont('song', 'C:/Windows/Fonts/simsun.ttc'))  # 宋体
from PyPDF2 import PdfFileWriter, PdfFileReader
import xlrd


######## 1.生成水印pdf的函数 ########
def create_watermark(content):
    # 默认大小为21cm*29.7cm
    c = canvas.Canvas('mark.pdf', pagesize=(20 * cm, 20 * cm))
    c.translate(10 * cm,
                10 * cm)  # 移动坐标原点(坐标系左下为(0,0)))
    c.setFont('song', 22)  # 设置字体为宋体，大小22号
    c.setFillColorRGB(0.5, 0.5,
                      0.5)  # 灰色
    c.rotate(45)  # 旋转45度，坐标系被旋转
    c.drawString(-7 * cm, 0 * cm, content)
    c.drawString(7 * cm, 0 * cm, content)
    c.drawString(0 * cm, 7 * cm, content)
    c.drawString(0 * cm, -7 * cm, content)
    c.save()  # 关闭并保存pdf文件


######## 2.为pdf文件加水印的函数 ########
def add_watermark2pdf(input_pdf, output_pdf, watermark_pdf):
    watermark = PdfFileReader(watermark_pdf)
    watermark_page = watermark.getPage(0)
    pdf = PdfFileReader(input_pdf, strict=False)
    pdf_writer = PdfFileWriter()
    for page in range(pdf.getNumPages()):
        pdf_page = pdf.getPage(page)
        pdf_page.mergePage(watermark_page)
        pdf_writer.addPage(pdf_page)
    pdfOutputFile = open(output_pdf, 'wb')
    pdf_writer.encrypt('codeoffer')  # 设置pdf密码
    pdf_writer.write(pdfOutputFile)
    pdfOutputFile.close()



merchant_as_mark_content = "公众号：codeoffer"  # 如果名称太短则重复4个为一行

######## 4.调用前面的函数制作商家水印pdf ########
if __name__ == '__main__':
    create_watermark(merchant_as_mark_content)  # 创造了一个水印pdf：mark.pdf
    filePath = 'D:\\Download\\water\\manage'
    name = os.listdir(filePath)
    for i in name:
        add_watermark2pdf(i, i + '_out.pdf', 'mark.pdf')
        print('———'+i+'————文件已转化完毕———————')

