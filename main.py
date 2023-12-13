import pdfkit
from pdf2image import convert_from_path

# URL to PDF
# getting html grom link into pdf
# pdfkit.from_url('http://127.0.0.1:80/index.html','shaurya.pdf')



# PDF to Image
# converting pdf to image
# images = convert_from_path('shaurya.pdf', poppler_path=r"C:\poppler\Library\bin")
 
# for i in range(len(images)):
#     images[i].save('page'+ str(i) +'.jpg', 'JPEG')



# converting img to pdf again

import img2pdf
from PIL import Image

img_path = "page0.jpg"
pdf_path = "shaurya converted.pdf"
image = Image.open(img_path)
pdf_bytes = img2pdf.convert(image.filename)
file = open(pdf_path, "wb")
file.write(pdf_bytes)
image.close()
file.close()
print("Successfully made pdf file")