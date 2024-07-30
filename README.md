# Movie Review App

A comprehensive Django application designed for browsing, reviewing, and managing movies. The app provides functionalities for users to search for movies, view detailed movie information, add and manage reviews, and interact with a news section. It also includes user authentication for account management.

## Table of Contents

- [Movie Review App](#movie-review-app)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Features](#features)
  - [Installation and Setup](#installation-and-setup)
    - [Prerequisites](#prerequisites)
    - [Installation Steps](#installation-steps)
  - [Usage](#usage)
  - [Development Notes](#development-notes)
  - [License](#license)

## Introduction

The Movie Review App is a Django-based web application that allows users to explore a collection of movies. Users can search for movies by title, view detailed information, and read or write reviews. It includes user authentication features such as login, registration, and logout, making it a robust platform for movie enthusiasts to interact with movie content and reviews.

This project serves as a practical example for learning Django fundamentals, including CRUD operations, user authentication, and template rendering.

## Features

- **Movie Search and Display**: 
  - Search for movies by title.
  - View a list of movies with their titles, descriptions, and images.
  - Access detailed information about each movie, including links to movie trailers if available.

- **Review Management**:
  - Add new reviews to movies.
  - Edit or delete your own reviews.
  - View a list of reviews for each movie, including the reviewer's username and review date.

- **User Authentication**:
  - Register a new account.
  - Log in to your account.
  - Log out of your account.
  
- **News Section**:
  - View news articles related to the app.
  - Sort news articles by date to see the latest updates.

- **Responsive Design**:
  - A clean, responsive design built with Bootstrap 5 to ensure a good user experience on various devices.

## Installation and Setup

### Prerequisites

Ensure you have the following software installed:

- Python 3.x
- Django 4.x
- Bootstrap 5.x (via CDN in templates)
- SQLite (or another database if configured)

### Installation Steps

1. **Clone the Repository**

    ```bash
    git clone https://github.com/ehsanshafi3i/movie-review.git
    cd movie-review/
    ```

2. **Create and Activate a Virtual Environment**

    ```bash
    python -m venv venv
    source venv/bin/activate   # For Windows: venv\Scripts\activate
    ```
3. **Apply Database Migrations**

    Apply database migrations to set up the database schema:

    ```bash
    python manage.py migrate
    ```

4. **Create a Superuser (Optional)**

    Create an admin user to access the Django admin interface:

    ```bash
    python manage.py createsuperuser
    ```

5. **Run the Local Development Server**

    Start the development server:

    ```bash
    python manage.py runserver
    ```

6. **Access the Application**

    Open your web browser and navigate to `http://127.0.0.1:8000/` to start using the application.

## Usage

- **Home Page**:
  - Search for movies using the search bar.
  - Browse the list of movies and view basic details.
  - Click on a movie to see detailed information and reviews.

- **Movie Details Page**:
  - View detailed information about a selected movie.
  - Add a new review if logged in.
  - View existing reviews and manage them if they are your own.

- **Add Review Page**:
  - Fill out a form to submit a new review for a movie.

- **Update Review Page**:
  - Edit an existing review using the form provided.

- **Login Page**:
  - Log into your account with your username and password.

- **Register Page**:
  - Create a new user account by filling out the registration form.

- **News Page**:
  - View news articles related to the app.
  - Use sorting options to view articles in chronological order.

## Development Notes

- **Settings**:
  - Configuration settings can be modified in `settings.py`, including database settings, static files, and other environment variables.

- **Templates**:
  - HTML templates are located in the `templates` directory. They use Bootstrap for styling and can be customized as needed.

- **Models**:
  - Models for movies, reviews, and news are defined in `models.py`. You can extend or modify these models to suit additional requirements.

- **Static Files**:
  - Static files like CSS and JavaScript are managed by Django. Ensure that `STATIC_URL` and `STATICFILES_DIRS` are properly configured in `settings.py`.

- **Forms**:
  - Forms for user registration, login, and review management are defined in `forms.py`. They handle user input and validation.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). See the [LICENSE](LICENSE) file for more details.

---

For more information, support, or to report issues, please visit the [Issues](https://github.com/ehsanshafi3i/movie-review/issues) page on GitHub.
