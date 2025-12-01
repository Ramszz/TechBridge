✅ 1. Create a README.md for your backend (copy–paste ready)

This file goes here:

TechBridge/backend/README.md


Copy the entire text below:

README.md (Backend) — TechBridge / GuideOra
Backend Framework: Django + Django REST Framework
Auth: JWT (SimpleJWT)
Database: SQLite (default)
🚀 1. Getting Started
1.1. Create and activate virtual environment

From the backend folder:

python -m venv venv


Activate:

Windows PowerShell

venv\Scripts\activate

📦 1.2. Install dependencies
pip install -r requirements.txt

▶️ 1.3. Run the development server
python manage.py runserver


Server will start at:

http://127.0.0.1:8000/

🔐 2. Authentication (JWT)
2.1. Login → Get Access Token

POST

http://127.0.0.1:8000/api/token/


Body:

{
  "username": "your_username",
  "password": "your_password"
}


Response contains:

access

refresh

Use access in all protected routes:

Authorization: Bearer <access_token>

👤 3. User Roles

There are 3 roles in the system:

student

alumni

admin (Django superuser → is_superuser=true)

Used by frontend routing:

students → student dashboard

alumni → alumni dashboard

admin → admin panel

🔗 4. API Endpoints
4.1. Authentication
Method	Endpoint	Description
POST	/api/token/	Get JWT tokens
POST	/api/token/refresh/	Refresh access token
4.2. User Registration & Profile
Method	Endpoint	Description
POST	/api/users/register/	Register student/alumni
GET	/api/users/me/	Get logged-in user profile
PATCH	/api/users/me/	Update own profile
4.3. Public Directories
Method	Endpoint	Description
GET	/api/users/students/	List all students
GET	/api/users/alumni/	List all alumni

Supports filters:

?branch=CSE
?q=python

4.4. Admin Management (Superuser only)
Method	Endpoint	Description
GET	/api/users/manage/	List all users
GET	/api/users/manage/<username>/	Get single user
PATCH	/api/users/manage/<username>/	Edit user
DELETE	/api/users/manage/<username>/	Delete user

Admin must use token:

Authorization: Bearer <admin_access_token>

📂 5. Project Structure
backend/
│── manage.py
│── requirements.txt
│── techbridge/ (Django project)
│── users/ (custom auth)
│     ├── models.py
│     ├── serializers.py
│     ├── views.py
│     ├── urls.py
│── venv/

🧪 6. Testing with Thunder Client

Use the following sequence:

Register → /api/users/register/

Login → /api/token/

Me → /api/users/me/

List alumni → /api/users/alumni/

List students → /api/users/students/

Admin list → /api/users/manage/

Admin delete → /manage/<username>/

Admin patch → /manage/<username>/

✔️ Backend Complete — Ready for Frontend Integration
✨ END OF README.md
