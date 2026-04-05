## The Highbury Experience
- Course: User Interfaces: Programming and Evaluation  
- Project 1: A restaurant menu and ordering system inspired by Arsenal Football Club.
- Group 7
    - Sarafroz Bekmurodova  
    - Cardo Khaledi  
    - William Lagerqvist

## Overview
- The Highbury Experience is a desktop user interface application built with Python and Tkinter.
- The system simulates a restaurant menu and ordering experience, designed to work across tablet and mobile form factors, 
  with a strong focus on usability and interaction design.

## Features (MVP)
- Browse menu categories (Starters, Mains, Desserts, Beverages)  
- View item details (description, allergens, dietary information)  
- Add and remove items from an order  
- Modify item quantities  
- View current order summary  
- Display total price (with optional tipping)  

### Key Focus Areas
- User Interface (UI) design  
- Interaction design  
- MVC-based architecture  
- Usability and HCI principles

## Notes
- No real backend is implemented, as per course requirements.
- The system simulates state using in-memory structures.
- Focus is on interaction, usability, and structure, not production deployment  
- This project is not about building a full production system, it is about designing 
  and implementing a well-structured, user-centered interface.

## Status
- Core UI implemented  
- MVC structure established  
- Key features functional  
- Ready for demonstration  

## Design Approach
The system is designed using an HCI-driven process:
- Personas and Scenarios to define user needs 
- Requirement specification based on user context  
- Low-fidelity prototyping (Sprint 0)  
- Iterative refinement of UI and interaction flow  

The design emphasizes:
- Simplicity and clarity of navigation  
- Low cognitive load  
- Visibility of system state (order overview)  
- Consistency across different screen sizes  

## Architecture
The system follows a layered MVC-inspired architecture:
- Model: Domain data and state (menu, order) 
- View: Tkinter UI components (rendering only)  
- Controller: Handles user interaction and flow  
- Service: Business logic (order handling, calculations)  
- Repository: Data abstraction

## Architectural Goals
- Clear separation of concerns  
- Maintainability and extensibility  
- Decoupling UI from business logic and data  
- This structure allows future changes (e.g., new UI or data source) without major refactoring.

## Requirements
- Python 3.10+
- Tkinter (included in standard Python distribution)  
- To verify Tkinter: python -m tkinter

## Development Setup
- Install Python
- (Optional) Virtual Environment, python -m venv venv
- Activate:
    - Windows: venv\Scripts\activate
    - Mac/Linux: source venv/bin/activate
- Dependencies: pip install -r requirements.txt.

## How to Run the Application
1. Navigate to the `src` directory  
2. Run the application: python main.py