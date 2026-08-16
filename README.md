# Django Blog Website 🚀

## Overview

This is my first Django Blog Website developed using **Python, Django, Bootstrap 5, and SQLite3**.

The purpose of this project is to learn web application development with Django and create a functional blog system with user authentication, profile management, and blog post management features.

---

## Features

### User Management

- User Registration
- User Login / Logout
- User Dashboard
- Profile Edit
- Profile Image Upload
- Change Password

### Blog Management

- Create Blog Posts
- Edit Blog Posts
- Delete Blog Posts
- View Blog Details
- Search Blog Posts

---

## Technologies

### Backend

- Python 3.13.14
- Django 6.0.7

### Frontend

- HTML5
- CSS3
- Bootstrap 5

### Database

- SQLite3

### Other

- Pillow (Image Processing)

---

## Project Structure

```text
django-blog-project/
│
├── home/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   └── static/
│
├── mysite/
│   ├── settings.py
│   └── urls.py
│
├── media/
│
├── manage.py
├── requirements.txt
└── README.md
```

---

## Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/Muthukate0426/django-blog-project.git
```

### 2. Go to the project folder

```bash
cd django-blog-project
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Apply database migrations

```bash
python manage.py migrate
```

### 7. Run the development server

```bash
python manage.py runserver
```

Open your browser and visit:

```text
http://127.0.0.1:8000/
```

---

## Future Improvements

- Add comment system
- Add categories and tags
- Deploy the website online
- Improve the UI design
- Add more security features

---

## Author

**Muthukate0426**

Django Blog Website Project 🚀
