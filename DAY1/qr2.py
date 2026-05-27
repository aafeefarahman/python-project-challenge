# Customized QR Code Generator using Python
# This script creates a styled QR code with custom
# size, border, color, and high error correction.

import qrcode
from PIL import Image

# Create a QRCode object with custom configurations
qr= qrcode.QRCode(version=1,
error_correction=qrcode.constants.ERROR_CORRECT_H,
box_size=10,
border=4)

# Add data link to the QR code
qr.add_data("https://github.com/aafeefarahman")

# Generate the QR code
qr.make (fit = True)

# Create the QR image with custom colors
img=qr.make_image(fill_color="blue", back_color="white")

# Save the generated QR code image
img.save("Afeefagitqr.png")   