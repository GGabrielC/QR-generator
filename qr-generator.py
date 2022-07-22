import qrcode
import sys

# Link for website
input_data = sys.argv[1]
print(input_data)

#Creating an instance of qrcode
qr = qrcode.QRCode(
        version=1,
        box_size=30,
        border=5)
qr.add_data(input_data)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')
img.save('QR code.png')