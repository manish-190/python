# Print a message (optional)
# print("hello")

#import qrcode as qr1

# Generate the QR code image
#img = qr1.make("https://www.google.com")

# Save the QR code image
#img.save("manish.jpg")
import qrcode
from PIL import Image  # Correct the import statement

# Create a QR code object
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)

# Add data to the QR code
qr.add_data("https://python.com")
qr.make(fit=True)  # Use 'True' instead of 'true'

# Create the image
img = qr.make_image(fill_color="red", back_color="blue")

# Save the QR code image
img.save("manish2.jpg")  # Corrected to save the image properly
