# Bulk Sponsorship Email Sender

A simple Python automation script that sends personalized emails to multiple organizations using Gmail SMTP.

## Why I Built This

While working on sponsorship outreach for a hackathon at IIIT Hyderabad and BITS Pilani, I needed a way to send the same sponsorship proposal to multiple companies without manually composing and sending each email one by one without using mail merge so i thought why not experiment with python code.

This project automates the process by:

- Sending emails to multiple recipients from a single script
- Personalizing each email with the company name
- Reducing manual effort during sponsorship outreach
- Tracking which emails were successfully sent

## Features

- Bulk email sending using Gmail SMTP
- Personalized email greetings
- Support for multiple company email addresses
- Success and failure tracking
- Easy customization of email subject and content

## Technologies Used

- Python
- smtplib (Simple Mail Transfer Protocol)
- Gmail SMTP Server

## Project Structure

```text
├── multipleemail.py
├── README.md
```

## How It Works

1. Store recipient email addresses in a Python dictionary.
2. Connect securely to Gmail's SMTP server.
3. Authenticate using a Gmail App Password.
4. Loop through all recipients.
5. Send a personalized email to each organization.
6. Display the sending status in the terminal.

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-repository-link>
cd bulk-email-sender
```

### 2. Install Python

Make sure Python 3.x is installed on your system.

Verify installation:

```bash
python --version
```

### 3. Configure Sender Details

Inside the script, replace:

```python
sender_email = "your_email@gmail.com"
app_password = "your_app_password"
```

with your own Gmail address and App Password.

## Generating a Gmail App Password

Google no longer allows less secure apps to access Gmail using your normal password. Instead, you must create an App Password.

### Step 1: Enable 2-Step Verification

1. Open your Google Account.
2. Navigate to Security.
3. Enable 2-Step Verification.

### Step 2: Generate an App Password

1. Go to Google Account → Security.
2. Open App Passwords.
3. Select:
   - App: Mail
   - Device: Other (Custom Name)

4. Enter a name such as:

```text
Bulk Email Sender
```

5. Click Generate.
6. Google will provide a 16-character password.

Example:

```text
abcd efgh ijkl mnop
```

Use it in Python without spaces:

```python
app_password = "abcdefghijklmnop"
```

### Important Security Note

Never:

- Upload your App Password to GitHub
- Share your App Password publicly
- Commit credentials directly to a repository

If an App Password is exposed, revoke it immediately and generate a new one.

## Running the Script

Execute:

```bash
python main.py
```

Example output:

```text
✓ Sent to Adobe
✓ Sent to Replit
✓ Sent to GitHub Education
✓ Sent to Cloudflare

All emails sent successfully!
```

## Use Cases
- Sponsorship outreach
- Event promotion
- Community engagement
- Club announcements
- Startup outreach
- Internship opportunity communication

## Disclaimer

Please use this project responsibly and avoid sending unsolicited or spam emails. Always ensure recipients are relevant to your outreach purpose.

-- Built to simplify sponsorship outreach and automate repetitive email communication.
