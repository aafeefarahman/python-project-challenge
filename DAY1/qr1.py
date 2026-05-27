# This script creates a simple QR code for a given URL
import qrcode as qr 
# Generate QR code
img = qr.make ("https://github.com/aafeefarahman")
# Save the generated QR code image
img.save ("qr.png")
 
