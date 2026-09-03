# Django Blog Website 🚀

## Overview

This is my first Django Blog Website developed using **Python, Django, Bootstrap 5, and SQLite3**.

The purpose of this project is to learn web application development with Django and create a functional blog system with user authentication, profile management, and blog post management features.

---

## Features

### User Management

* User Registration
* User Login / Logout
* User Dashboard
* Profile Edit
* Profile Image Upload
* Change Password

### Blog Management

* Create Blog Posts
* Edit Blog Posts
* Delete Blog Posts
* View Blog Details
* Search Blog Posts

### Access Control

* Login required for creating blog posts
* Users can edit their own posts
* Users can delete their own posts
* Authentication-based page access

---

## Technologies

### Backend

* Python 3.13.14
* Django 6.0.7

### Frontend

* HTML5
* CSS3
* Bootstrap 5
* JavaScript

### Database

* SQLite3

### Other

* Pillow (Image Processing)
* Git
* GitHub
* Render

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
├── manage.py
├── requirements.txt
├── build.sh
├── db.sqlite3
└── README.md
```

---

## Live Demo 🌐

The website is deployed online using **Render**.

👉 **Live Demo:**
https://django-blog-project-iiqb.onrender.com/

> Note: The free hosting service may take some time to start after a period of inactivity.

---

## GitHub Repository 💻

👉 **Source Code:**
https://github.com/Muthukate0426/django-blog-project

The complete source code is available on GitHub.

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

## What I Learned 📚

Through this project, I learned how to:

* Build web applications using Django
* Create Django models and database structures
* Implement user authentication
* Handle forms and user input
* Upload and manage images
* Implement CRUD operations
* Create search functionality
* Use Django templates
* Organize a Django project
* Use Git and GitHub for version control
* Deploy a Django application online

---

## Future Improvements 🔮

* Add comment system
* Add categories and tags
* Improve the UI design
* Add pagination
* Improve security features
* Migrate from SQLite to PostgreSQL for production

---

## Author 👨‍💻

**Nirma**

IT Engineer Student | Web Development

Interested in building web applications using **Python, Django, HTML, CSS, and JavaScript**.

---

⭐ Thank you for visiting my project!
