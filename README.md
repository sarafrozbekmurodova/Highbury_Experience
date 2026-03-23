# The Highbury Experience 🔴⚪

**Project 1 – User Interfaces: Programming and Evaluation (HCI)**
A premium restaurant menu and ordering system inspired by Arsenal Football Club.

---

## Overview

The Highbury Experience is a **desktop UI application** built with Python and Tkinter.
It simulates a restaurant menu and ordering system designed for both tablet and mobile interfaces.

The focus of this project is:

- User Interface design
- Interaction design
- MVC architecture
- Usability (HCI principles)

---

## Features (MVP)

- Browse menu categories (starters, mains, desserts, beverages)
- View item details (description, allergens, dietary info)
- Add items to order
- View and update current order
- Display total price (with optional tipping)

---

## Design Approach

This project is based on:

- Personas and Scenarios (HCI-driven design)
- Sprint 0 prototyping (low-fidelity UI design)
- MVC (Model-View-Controller) architecture

Documentation can be found in:

```
docs/
```

---

## 🏗 Project Structure

```
Highbury_Experience/
│
├── README.md
│
├── docs/
│   ├── 01_Personas_and_Scenarios.md
│   ├── 02_Sprint0_MVP_Screens.md
│   └── 03_Project_Summary_and_Next_Steps.md
│
├── src/
│   ├── main.py
│   ├── app.py
│   │
│   ├── model/
│   ├── view/
│   ├── controller/
│   └── data/
│
├── tests/
└── assets/
```

---

## Requirements

- Python **3.10+** (recommended)
- Tkinter (included with standard Python installation)

To verify Tkinter:

```bash
python -m tkinter
```

---

## How to Run the Application

1. Navigate to the `src` folder:

2. Run the application:

```bash
python main.py
```

---

## Development Setup

1. Install Python

Download from:
https://www.python.org/downloads/

Verify installation:

```bash
python --version
```

---

### 2. (Optional but Recommended) Create Virtual Environment

```bash
python -m venv venv
```

Activate:

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

---

### 3. Install Dependencies

Currently, no external dependencies are required.
(Tkinter is included with Python)

---

### 4. Open in VS Code

* Open folder: `HighburyExperience`
* Select Python interpreter (venv if used)

---

## 🧩 Architecture

The system follows a simplified MVC pattern:

* **Model** → Data and business logic (menu, order)
* **View** → Tkinter UI components
* **Controller** → Interaction logic

---

## 👥 Collaboration

This project is designed for group collaboration.

Guidelines:

* Keep structure clean (respect MVC separation)
* Document major changes
* Ensure all members understand the code
* Use Git for version control

---

## 🧪 Testing

Basic tests can be added in:

```
tests/
```

(Currently minimal – to be extended)

---

## 📅 Status

* Project structure created
* Sprint 0 (Personas, Scenarios, UI design) in progress
* Sprint 1 (UI implementation) in progress

---

## ⚠️ Notes

* No real backend is implemented (as per course requirements)
* Focus is on UI behavior and interaction

---

## 💬 Authors


Course: User Interfaces: Programming and Evaluation
Group 7

- Sarafroz Bekmurodova
- Cardo Khaledi
- William Lagerqvist


---

## 🏆 Final Note

This project is not about building a full system —
it is about building a **well-designed interface**.

---
