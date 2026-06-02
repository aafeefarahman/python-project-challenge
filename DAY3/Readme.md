# Typing Speed Test using Python

## Project Overview

The Typing Speed Test is a simple Python mini-project that measures a user's typing speed and accuracy. The program displays a random paragraph, records the time taken by the user to type it, calculates typing speed, and counts typing errors by comparing the typed text with the original paragraph.

---

## Objectives

- Measure typing speed.
- Calculate typing accuracy.
- Practice Python functions and loops.
- Understand string comparison and time handling.
- Build a simple console-based application.

---

## Technologies Used

- Python 3
- `time` module
- `random` module

---

## Features

✔ Random paragraph generation

✔ Typing speed calculation

✔ Error detection

✔ Multiple test attempts

✔ User-friendly console interface

---

## How It Works

1. A random paragraph is selected from a predefined list.
2. The paragraph is displayed on the screen.
3. The timer starts when the user begins typing.
4. The user types the paragraph and presses Enter.
5. The timer stops.
6. The program calculates:
   - Typing Speed (characters per second)
   - Number of Errors

7. The user can choose to take the test again.

---

## Functions Used

### `mistake(paratest, usertest)`

This function compares the original paragraph with the user's input character by character.

**Purpose:**

- Detect typing mistakes.
- Count total errors.

---

### `speed_time(time_s, time_e, userinput)`

This function calculates typing speed.

**Formula:**

```text
Typing Speed = Number of Characters Typed / Time Taken
```

**Purpose:**

- Measure typing performance.
- Return speed in characters per second.

---

## Program Flow

```text
Start Program
      ↓
Select Random Paragraph
      ↓
Display Paragraph
      ↓
Start Timer
      ↓
User Types Text
      ↓
Stop Timer
      ↓
Calculate Speed
      ↓
Calculate Errors
      ↓
Display Results
      ↓
Test Again? (Yes/No)
      ↓
Exit Program
```

---

## Sample Output

```text
********** TYPING SPEED TEST **********

lorem ipsum dolor sit amet consectetur adipisicing elit

Enter : lorem ipsum dolor sit amet consectetur

Speed : 4 w/sec
Error : 12

Ready to test : yes / no : yes
```

---

## Concepts Used

- Functions
- Lists
- Loops
- Conditional Statements
- Exception Handling
- String Indexing
- Time Measurement
- Random Selection

---
