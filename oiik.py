import qrcode

#Data to be encoded in QR code

data = "www.youtube.com"

#Create a QRCode instance

qr = qrcode.QRCode(
     version=1, # Controls the size 
     error_correction=qrcode.constants.ERROR_CORRECT_L, #Controls error conrection level
     box_size=10,
     border=4,
)

#Add data to the qr code

qr.add_data(data)
qr.make(fit=True)

#Create an image from the QR Code

img = qr.make_image(fill_color='Black', back_color='white')

# Save the image
img.save("qrcode_example.png")

#Display the image
img.show()