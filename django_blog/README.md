# Django Blog Project

A full-featured blog application built with Django, allowing users to create, read, update, and delete their own posts. This project includes a comprehensive user authentication system and robust blog post management features.

## 🌟 Features

* **User Authentication**: Secure user registration, login, and logout.
* **Profile Management**: Authenticated users can view and edit their profile details.
* **Post Management**: Full CRUD (Create, Read, Update, Delete) functionality for blog posts.
* **Permissions**: Only authenticated users can create posts, and only the author can edit or delete their own posts.
* **Responsive Design**: A simple and clean user interface that is mobile-friendly.

***

## 🚀 Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing.

### Prerequisites

* Python 3.8+
* pip

### Installation

1.  **Clone the repository**:
    ```bash
    git clone [https://github.com/Alx_DjangoLearnLab/django_blog.git](https://github.com/Alx_DjangoLearnLab/django_blog.git)
    cd django_blog
    ```

2.  **Create and activate a virtual environment**:
    ```bash
    # On macOS and Linux
    python3 -m venv venv
    source venv/bin/activate

    # On Windows
    python -m venv venv
    venv\Scripts\activate
    ```

3.  **Install project dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
    (Note: If you don't have a `requirements.txt` file, you can create one by running `pip freeze > requirements.txt` after installing Django.)

4.  **Run migrations**:
    ```bash
    python manage.py makemigrations blog
    python manage.py migrate
    ```

5.  **Create a superuser** (for accessing the Django admin panel):
    ```bash
    python manage.py createsuperuser
    ```

6.  **Run the development server**:
    ```bash
    python manage.py runserver
    ```

7.  Open your browser and navigate to `http://127.0.0.1:8000/`.

***

## ⚙️ Project Structure

* `django_blog/`: The project's core settings.
* `blog/`: The main application.
    * `models.py`: Defines the **Post** model.
    * `views.py`: Contains the **class-based views** for post CRUD operations and user authentication.
    * `urls.py`: Manages URL routing for the blog app.
    * `templates/`: All HTML templates, including those for posts, login, and registration.
    * `static/`: Stores static files like CSS and images.

***

## 🛡️ Permissions and Access Control

This project uses Django's built-in authentication and mixins to manage user permissions.

* **Login Required**: Only authenticated users can **create, update, or delete posts**. Unauthenticated users will be redirected to the login page.
* **Author-Only Access**: **Only the author of a post** can edit or delete it. An unauthorized user attempting to modify another user's post will receive a `403 Forbidden` error.

***

## 👨‍💻 Contributing

Contributions are welcome! If you have suggestions for new features, bug reports, or code improvements, please open an issue or submit a pull request.

***

## 📜 License

This project is licensed under the MIT License.