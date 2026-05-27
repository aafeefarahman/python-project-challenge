# Day 1 — QR Code Generator

A simple yet customizable QR Code Generator built using Python
This project explores how QR codes can be generated, customized, and saved as images using Python.

---

## What This Project Does

- Converts links/text into QR codes
- Saves QR codes as image files
- Supports custom colors and styling
- Demonstrates both basic and advanced implementations

---

## Files Included

### `basic_qr.py`

A minimal QR code generator using just a few lines of code.

### `custom_qr.py`

A customized QR generator with:

- color customization
- border settings
- error correction
- size configuration

---

## Functions Used

| Function       | Purpose                           |
| -------------- | --------------------------------- |
| `qr.make()`    | Generates a simple QR code        |
| `QRCode()`     | Creates a customizable QR object  |
| `add_data()`   | Adds data/link into the QR code   |
| `make()`       | Builds the QR structure           |
| `make_image()` | Creates the QR image with styling |
| `save()`       | Saves the QR image file           |

---

## How It Works

1. Import the required libraries
2. Add the link/text
3. Generate the QR code
4. Customize the design (optional)
5. Save the QR image

---

## Learning Outcome

Through this project, I practiced:

- Working with Python libraries
- Understanding functions and parameters
- Image generation using Python
- Difference between basic and customized implementations
