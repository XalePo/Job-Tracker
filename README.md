# Job Application Tracker

This is a job tracking application that I built to learn Django and put into practice the knowledge I gained from the Coursera course. The project allows users to authenticate and manage their own job applications through full CRUD functionality. Each user can create, view, update, and delete their applications, while only having access to their own data.

## Features

- User authentication
  - Sign up
  - Log in
  - Log out
- Full CRUD operations for job applications
- User-specific application tracking
- Search, filter, sort, and pagination
- Success messages for important actions

## Tech Stack

- Python
- Django
- HTML
- CSS
- SQLite

## Purpose

The main purpose of this project was to strengthen my understanding of Django by building a practical application from scratch. Through this project, I practiced working with models, views, templates, authentication, URL routing, forms, pagination, and user-based data filtering.

## Running the Project Locally

1. Clone the repository
2. Create and activate a virtual environment
3. Install the project dependencies
4. Run migrations
5. Start the development server

Example commands:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
