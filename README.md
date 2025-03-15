# Flask Blog Application 📝🚀

## 📌 About the Project
This is a **Flask-based Blog Application** that allows users to **create, manage, and share blog posts** with a seamless user experience. The application includes **user authentication, profile management, and password reset functionalities**, making it a complete blogging platform.

## ✨ Features

### 🔐 User Authentication & Profile Management
- **Register & Login System** with Flask-Login 🔑
- **Secure Password Hashing** using Flask-Bcrypt 🛡️
- **Update Profile Picture** with Image Upload Functionality 📷
- **Forgot Password?** Email-based password reset using Flask-Mail 📧

### 📝 Blog Post Management
- **Create, Read, Update, and Delete (CRUD) Posts** 📃
- **Posts Sorted by Latest First** 🕒
- **User-Specific Posts Page** – See posts by a particular user 👥
- **Dynamic Post URLs** for easy sharing 🔗

### 🖥️ Frontend & UI
- **Flask-Jinja2 Templating** for dynamic content rendering 🌐
- **Bootstrap 5 for Responsive UI** 🎨
- **Flash Messages for Better User Experience** 💬

## 📂 Database & Security
- **SQLite / PostgreSQL Support** 🛢️
- **SQLAlchemy ORM for Database Handling** 🏛️
- **Session Management & Secure Cookies** 🍪

## ⚙ Tech Stack
- **Backend:** Flask, SQLAlchemy, Flask-WTF, Flask-Login
- **Frontend:** HTML, CSS, Bootstrap, Jinja2 Templating
- **Database:** SQLite / PostgreSQL
- **Security:** Flask-Bcrypt, Flask-Mail, CSRF Protection

## 🚀 Installation & Setup

### 1 Clone the Repository
```bash
git clone https://github.com/vipulc2580/Flask_Blog_Application.git
cd Flask_Blog_Application
```

## 2 Create & Activate Virtual Environment
To set up a virtual environment, run the following commands:

```python
  python -m venv venv
  source venv/bin/activate  # (Mac/Linux)
  venv\Scripts\activate  # (Windows)
```


## 3 Set Up Environment Variables

```bash
  SECRET_KEY=your_secret_key
  MAIL_SERVER=smtp.gmail.com
  MAIL_PORT=587
  MAIL_USE_TLS=True
  MAIL_USERNAME=your_email@gmail.com
  MAIL_PASSWORD=your_app_password
``` 
##  4 Initialize the Database
``` python
>>> from flaskblog import db
>>> db.create_all()
>>> exit()
``` 
## 5 Run the Flask Application
``` python 
  flask run
```
