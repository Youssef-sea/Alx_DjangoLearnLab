1. Project Setup and Installation
Follow these steps to get the project running on your local machine.

Prerequisites
Python 3.8+

pip (Python package installer)

A virtual environment (recommended)

Installation Steps
Clone the repository:

Bash

git clone <repository_url>
cd social_media_api
Create and activate a virtual environment:

Bash

# On Windows
python -m venv venv
.\venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
Install project dependencies:

Bash

pip install -r requirements.txt
# Or, if you don't have a requirements.txt file yet:
pip install django djangorestframework Pillow
Run database migrations:
This step sets up the database schema, including the custom user model and authentication tables.

Bash

python manage.py makemigrations accounts
python manage.py migrate
Start the development server:

Bash

python manage.py runserver
The API will be running at http://127.0.0.1:8000/.

2. API Endpoints and Usage
The API currently supports user registration, login, and profile management. All endpoints are prefixed with /api/accounts/.

User Registration
Endpoint: /api/accounts/register/

Method: POST

Description: Creates a new user account. Upon successful creation, it returns a unique authentication token.

Request Body (JSON):

JSON

{
    "username": "unique_username",
    "email": "user@example.com",
    "password": "strong_password123",
    "bio": "Optional user bio"
}
Success Response:

JSON

{
    "token": "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b",
    "user": {
        "username": "unique_username",
        "email": "user@example.com",
        "bio": "Optional user bio"
    }
}
User Authentication (Login)
Endpoint: /api/accounts/login/

Method: POST

Description: Authenticates a user with their username and password and returns a token for future requests.

Request Body (JSON):

JSON

{
    "username": "unique_username",
    "password": "strong_password123"
}
Success Response:

JSON

{
    "token": "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"
}
User Profile
Endpoint: /api/accounts/profile/

Method: GET, PUT, PATCH

Authentication: Requires a Token in the Authorization header.

Authorization: Token <your_token>

Description: Retrieves and updates the profile of the currently authenticated user.

GET Request (Retrieve):

Returns the user's profile information.

PUT/PATCH Request (Update):

Request Body (JSON):

JSON

{
    "bio": "New bio content",
    "profile_picture": "<image_file>"
}
username and email are read-only and cannot be updated through this endpoint.

3. User Model Overview
The CustomUser model is the foundation of the user system. It extends Django's built-in AbstractUser and includes the following fields:

username: (inherited) A unique identifier for the user.

email: (inherited) User's email address.

bio: A TextField for a short description of the user.

profile_picture: An ImageField to store a profile photo.

followers: A many-to-many relationship with itself (self). The symmetrical=False attribute allows a user to follow another user without the other user automatically following back. This field tracks the users who are following the current user.