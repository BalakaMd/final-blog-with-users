---

# Blog Website with users using Flask

This is a simple blog website built using Flask, a Python web framework. The website allows users to register, login,
create, edit, and delete blog posts,leave comments on blog posts, and view blog posts.

## Prerequisites

Before running the application, make sure you have the following installed:

- Python
- Flask
- Flask-Bootstrap
- Flask-CKEditor
- Flask-Gravatar
- Flask-Login
- Flask-SQLAlchemy
- SQLAlchemy

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/BalakaMd/final-blog-with-users.git
   ```

2. Navigate to the project directory:

   ```bash
   cd final-blog-with-users
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Set environment variables for Flask and your database URI. For example:

   ```bash
   export FLASK_KEY="your_secret_key"
   export DB_URI="sqlite:///blog.db"
   ```


## Usage

To run the application, use the following command:

```bash
python main.py
```

Visit `http://localhost:5000` in your web browser to access the blog website.

## Features

- **User Registration**: Users can register for an account with a name, email, and password.

- **User Login**: Registered users can log in to their accounts.

- **Create and Edit Posts**: Logged-in users can create new blog posts and edit their existing posts.

- **View Posts**: All visitors can view the list of blog posts.

- **Leave Comments**: Logged-in users can leave comments on blog posts.

- **Admin Functionality**: An admin (user with ID 1) has special privileges to add, edit, and delete blog posts.

- **Gravatar Integration**: User avatars are generated using Gravatar based on their email addresses.

## Routes

- `/register`: User registration page.

- `/login`: User login page.

- `/logout`: Log out the user.

- `/`: Homepage displaying a list of blog posts.

- `/post/<int:post_id>`: View a specific blog post and leave comments.

- `/new-post`: Create a new blog post (admin only).

- `/edit-post/<int:post_id>`: Edit a blog post (admin only).

- `/delete/<int:post_id>`: Delete a blog post (admin only).

- `/about`: About page.

- `/contact`: Contact page.

## Credits

This project was created by BalakaMd. It is a simple blog website built with Flask and various Flask extensions.
Feel free to use and modify it for your own projects.

---
