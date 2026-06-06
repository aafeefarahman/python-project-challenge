# SnapShot Pro

## Introduction

SnapShot Pro is a desktop screenshot utility developed entirely in Python. The application provides a simple and efficient way to capture screenshots with customizable filenames, configurable delays, automatic file organization, and screenshot history tracking.

The project was built to explore desktop automation, graphical user interface development, file management, and event-driven programming while creating a practical tool that can be used in everyday workflows.

---

## Features

- Full-screen screenshot capture
- Custom screenshot filenames
- Configurable capture delay
- Automatic date-wise screenshot organization
- Screenshot history tracking
- Desktop notifications
- Modern dark-themed user interface
- Quick access to saved screenshots

---

## Technologies Used

### Programming Language

- Python 3

### Libraries

| Library       | Purpose                               |
| ------------- | ------------------------------------- |
| CustomTkinter | Modern desktop GUI development        |
| PyAutoGUI     | Screen capture automation             |
| Pillow (PIL)  | Image handling support                |
| Plyer         | Desktop notifications                 |
| JSON          | Screenshot history storage            |
| OS Module     | File and directory management         |
| Datetime      | Timestamp generation and organization |

---

## Project Structure

```text
SnapShot-Pro/
│
├── screenshot_pro.py
├── history.json
│
└── Screenshots/
    └── YYYY-MM-DD/
        ├── screenshot1.png
        ├── screenshot2.png
```

---

## Installation

Install the required dependencies:

```bash
pip install pyautogui pillow customtkinter plyer
```

Run the application:

```bash
python screenshot_pro.py
```

---

## Insights

Through the development of SnapShot Pro, several important software engineering concepts were explored:

- Desktop GUI development using Python
- Screen automation and event handling
- File and directory management
- JSON-based data persistence
- User experience design for desktop applications
- Notification systems and system integration
- Modular application structure and maintainable code design

This project demonstrates how Python can be used beyond scripting and data analysis to build complete desktop applications with real-world utility.

---

## Future Enhancements

- Region-based screenshot selection
- Global keyboard shortcuts
- OCR-based text extraction from screenshots
- Copy screenshots directly to clipboard
- Screenshot annotation and editing tools
- Exportable screenshot history
- Standalone executable packaging

---
