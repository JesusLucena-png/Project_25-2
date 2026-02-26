# Console Calculator in Python

A console application developed in Python that allows users to perform basic mathematical operations in a safe, controlled way with proper error handling.

This project was developed following the Scrum methodology (short sprints) and version control using Git.

---

## Objective

To develop a Python console application that works as a basic calculator, allowing the user to perform simple mathematical operations without the system crashing due to input errors.

---

## Functional Scope (MVP)

The application allows users to:

* Add
* Subtract
* Multiply
* Divide
* Exit the program

### Implemented Validations

* Verification that the entered values are numbers (`try / except`)
* Division by zero validation
* Menu option validation
* The program never crashes due to user errors
* Allows multiple operations until the user decides to exit

---

## Technical Requirements

* Language: **Python**
* Mandatory use of:

  * `if / elif / else`
  * `try / except`
* Code organized into functions
* Main file: `main.py`
* Clear console messages

---

## Project Structure

```
calculator/
│── main.py
│── README.md
```

---

## Scrum Methodology

The project was developed in short sprints:

### Sprint 1

* Display menu
* Implement addition and subtraction
* Basic error handling

### Sprint 2

* Add multiplication and division
* Division by zero validation
* Organize code into functions

### Sprint 3

* Improve user experience
* More robust validations
* Code cleaning and refactoring

---

## Git Workflow

Branch structure used:

* `main`
* `develop`
* `feature/menu`
* `feature/processes`
* `feature/validations`

Practices applied:

* `git checkout -b`
* `git merge`
* Simple conflict resolution
* Clear and descriptive commits

Example of a good commit:

```
feat: add division by zero validation
```

---

## User Story

**As a user**
I want to perform basic mathematical operations
So that I can get results without the system crashing due to errors

---

## Acceptance Criteria

* The program must never close due to an input error.
* It must continue running until the user chooses to exit.
* It must display clear and understandable messages.
* The code must be organized into functions.

---

## Optional Improvements

* Counter of completed operations
* Simple operation history
* Exit confirmation
* Additional refactoring

---

## Authors

* Jesus Lucena
* Aura Alean
* Nicholas De la Rosa
* Jhon Salgado
* Yasir Quintero

Academic project / professional practice