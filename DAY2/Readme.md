# Day 2 — Email Validator

In this mini project, I built a simple Email Validator using Python.  
The program checks whether an email follows basic validation rules and identifies different types of invalid email formats.

---

# Features

- Checks minimum email length
- Ensures the email starts with an alphabet
- Validates `@` usage
- Checks proper `.` placement
- Detects spaces and invalid characters
- Beginner-friendly validation logic

---

# Validation Rules Used

The program checks whether:

✅ Email length is at least 6 characters  
✅ First character is an alphabet  
✅ Only one `@` symbol exists  
✅ `.` exists in the correct position  
✅ No spaces are present  
✅ No invalid special characters are used  
✅ No uppercase letters are present

---

# How the Code Works

## 1️Take Email Input

```python
email = input("Enter your email: ")
```

The user enters an email address.

---

## 2️. Length Validation

```python
if len(email) >= 6:
```

Checks whether the email length is valid.

---

## 3️. First Character Check

```python
if email[0].isalpha():
```

Ensures the email starts with a letter.

---

## 4️. `@` Validation

```python
if ("@" in email) and (email.count("@") == 1):
```

Checks:

- `@` exists
- only one `@` is present

---

## 5️. Dot (`.`) Validation

```python
if (email[-4] == ".") ^ (email[-3] == "."):
```

Checks proper placement of `.` before domain extensions like:

- `.com`
- `.in`

---

## 6️. Character Validation

The loop checks:

- spaces
- uppercase letters
- digits
- allowed symbols

```python
for i in email:
```

---

# Functions Used

| Function    | Purpose                    |
| ----------- | -------------------------- |
| `input()`   | Takes user input           |
| `len()`     | Checks email length        |
| `isalpha()` | Checks alphabet characters |
| `isdigit()` | Checks numeric characters  |
| `isspace()` | Detects spaces             |
| `count()`   | Counts occurrences of `@`  |

---

# Sample Test Emails

## Valid

afeefa@gmail.com

python_dev@yahoo.in

---

## Invalid

1afeefa@gmail.com

afeefa@@gmail.com

afeefa @gmail.com

# Learning Outcome

Through this project, I practiced:

- Conditional statements
- Nested `if-else`
- String handling
- Loops
- Python validation logic
- Debugging and problem-solving

```

```
