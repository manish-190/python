import qrcode
from PIL import manish

qr=qrcode.QRCode(Version=1,
error_correction=qrcode.constants.ERROR.CORRECT_H,box_size=10,border=4)

qr.add_data("https://google.com")
qr.make(fit=true)
img=qr.make_image(fill_color="red",back_color="blue")
image.save(man.jpg)
