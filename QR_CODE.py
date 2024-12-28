#INSTALL THE QRCODE LIBRARY

import qrcode

#I DON'T GET THIS HOW DID I WRITE THIS WITHOUT ANY EXPLANATION
qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_L,
                   box_size=20,
                   border=2)

qr.add_data("https://www.Iftikhar_CV.com/books")
qr.make(fit=True)

img = qr.make_image(fill_color= "black", back_color= "white")
img.save("advanced png")
