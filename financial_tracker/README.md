# Finance Tracking App

## Overview
This project is a financial tracking application built with Django. It allows users to manage expenses and income, visualize data, and compare total income vs. expenses. The application includes an admin interface for managing financial records and a basic dashboard to display income vs. expense statistics.

## Features
### 1. Models
- **Expense**: Represents an expense with fields for date, item, amount, and a foreign key to the category.
- **Income**: Represents income with fields for date, amount, and a foreign key to the source.
- **Category**: Represents the category of an expense (e.g., Food, Rent, etc.).
- **Source**: Represents the source of income (e.g., Salary, Business, etc.).

### 2. Admin Interface
- Admin can manage `Expense`, `Income`, `Category`, and `Source` through Django's built-in admin interface.

### 3. Forms
- **Expense Form**: Includes fields for date, item, amount, and category.
- **Income Form**: Includes fields for date, amount, and source.

### 4. Views
- **Add Expense**: A form for adding new expense entries.
- **Add Income**: A form for adding new income entries.
- **List Expenses**: Displays a list of expenses with filters for category and date range.
- **List Income**: Displays all income entries.
- **Compare Income vs Expense**: Shows total income, total expense, and balance (savings/overspending).


## Installation Instructions

### Prerequisites

- Python 3.x installed on your system.
- Pip (Python package installer).

### Step-by-step Installation

1. Clone the repository:

   git clone https://github.com/hannahghub123/finance-tracking-app.git

   cd finance-tracking-app

3. Create and activate a virtual environment (optional but recommended):

    python -m venv venv
    source venv/bin/activate  # Unix/Mac
    .\venv\Scripts\activate  # Windows

4. Install required dependencies:

    pip install -r requirements.txt

5. Run the Django migrations:

    python manage.py migrate

6. Create a superuser account for accessing the admin panel:

    python manage.py createsuperuser

7. Run the Django development server:

    python manage.py runserver

8. Access the app at http://127.0.0.1:8000/ and the admin interface at http://127.0.0.1:8000/admin/.
