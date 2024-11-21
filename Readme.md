# Expense Tracker API

A Django-based API for managing users and their expenses. The application includes CRUD operations for expenses, filtering by date range, and generating category-based summaries for expenses.

---

## Features

- **User Management**:
  - Add and manage users with `username` and `email`.
- **Expense Management**:
  - Create, retrieve, update, and delete expenses.
  - Filter expenses by a specific date range.
  - Get category-wise expense summaries for a given month.

---

## Technology Stack

| Component          | Technology            |
| ------------------ | --------------------- |
| **Backend**        | Django                |
| **API Framework**  | Django REST Framework |
| **Database**       | SQLite (default)      |
| **Python Version** | 3.x                   |

---

## Prerequisites

| Step | Task                            | Command/Details                                                                        |
| ---- | ------------------------------- | -------------------------------------------------------------------------------------- |
| 1    | Install Python                  | Download and install Python 3.x from [python.org](https://www.python.org/downloads/).  |
| 2    | Install `pip`                   | Python's package installer is included in Python 3.x. Run `pip` to check installation. |
| 3    | (Optional) Install `virtualenv` | Run `pip install virtualenv` for virtual environments.                                 |

---

## Setup Instructions

Follow the steps below to set up the project:

| Step | Description                               | Command/Details                                                                                                              |
| ---- | ----------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| 1    | **Clone the repository**                  | `git clone https://github.com/EmeraldDev110/pageloot-django-test.git`                                                        |
| 2    | **Navigate to the project directory**     | `cd expense_tracker`                                                                                                         |
| 3    | **Create a virtual environment**          | `python -m venv venv`<br>Activate it:<br>- On Linux/Mac: `source venv/bin/activate`<br>- On Windows: `venv\Scripts\activate` |
| 4    | **Install dependencies**                  | `pip install -r requirements.txt`                                                                                            |
| 5    | **Run migrations to set up the database** | `python manage.py makemigrations`<br>`python manage.py migrate`                                                              |
| 6    | **Run the development server**            | `python manage.py runserver`                                                                                                 |

After step 6, the server will start at `http://127.0.0.1:8000/`.

---

## API Endpoints

| Endpoint                                                                                   | Method | Description                                                       |
| ------------------------------------------------------------------------------------------ | ------ | ----------------------------------------------------------------- |
| `/api/users/`                                                                              | GET    | List all users                                                    |
| `/api/users/`                                                                              | POST   | Create a user                                                     |
| `/api/expenses/`                                                                           | GET    | List all expenses                                                 |
| `/api/expenses/`                                                                           | POST   | Create an expense                                                 |
| `/api/expenses/{id}/`                                                                      | GET    | Retrieve a specific expense                                       |
| `/api/expenses/{id}/`                                                                      | PUT    | Update a specific expense                                         |
| `/api/expenses/{id}/`                                                                      | DELETE | Delete a specific expense                                         |
| `/api/expenses/list_by_date_range/?user_id={id}&start_date=YYYY-MM-DD&end_date=YYYY-MM-DD` | GET    | List expenses for a user within a date range                      |
| `/api/expenses/category_summary/?user_id={id}&month=YYYY-MM`                               | GET    | Get category-wise expense summary for a user for a specific month |

---

## Validation

| Field      | Rule                                                   |
| ---------- | ------------------------------------------------------ |
| `amount`   | Must be a **positive number**                          |
| `category` | Must be one of: `Food`, `Travel`, `Utilities`, `Other` |

---
