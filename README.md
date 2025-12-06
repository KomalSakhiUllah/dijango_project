# Task Manager - Mini-Jira Django Web Application

A modern, feature-rich task management web application built with Django, featuring a beautiful UI, comprehensive error handling, and robust validation.

## 🚀 Features

### Authentication
- User signup with email validation
- Secure login/logout
- Password hashing
- Login required decorators
- User-friendly error messages

### Task Management
- Create, read, update, and delete tasks
- Task fields:
  - Title (required, validated)
  - Description
  - Priority (Low/Medium/High)
  - Status (To Do/In-Progress/Completed)
  - Due date (optional)
  - Automatic timestamps
- Search functionality
- Filter by priority and status
- Dashboard with task summary

### Subtask System
- Add multiple subtasks to each task
- Edit and delete subtasks
- Subtask status tracking

### Modern UI/UX
- Bootstrap 5 responsive design
- Custom CSS with animations
- Gradient navbar and buttons
- Card lift effects
- Smooth transitions
- Fade-in animations
- Beautiful splash screen with auto-redirect

### Error Handling & Validation
- Form validation with clear error messages
- Backend exception handling
- Custom error pages (404, 403, 500)
- User ownership verification
- Database constraint handling
- Client-side validation

## 📋 Requirements

- Python 3.8+
- Django 4.2+

## 🛠️ Installation

1. **Clone or navigate to the project directory:**
   ```bash
   cd "django project"
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Create a superuser (optional, for admin access):**
   ```bash
   python manage.py createsuperuser
   ```

5. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

6. **Access the application:**
   - Open your browser and go to: `http://127.0.0.1:8000/`
   - You'll see the splash screen, which automatically redirects to the login page

## 📁 Project Structure

```
django project/
├── manage.py
├── requirements.txt
├── README.md
├── taskmanager/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── tasks/
│   ├── __init__.py
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── migrations/
├── templates/
│   └── tasks/
│       ├── base.html
│       ├── splash.html
│       ├── login.html
│       ├── signup.html
│       ├── dashboard.html
│       ├── task_list.html
│       ├── task_form.html
│       ├── task_detail.html
│       ├── task_confirm_delete.html
│       ├── subtask_form.html
│       ├── subtask_confirm_delete.html
│       ├── 404.html
│       ├── 403.html
│       └── 500.html
└── static/
    └── css/
        └── style.css
```

## 🎨 Color Palette

- Primary Blue: `#1E88E5`
- Light Blue: `#90CAF9`
- Cream: `#FFF8E1`
- Navy: `#0D47A1`
- Soft Gray: `#ECEFF1`

## 🔒 Security Features

- CSRF protection
- SQL injection prevention (Django ORM)
- User authentication required for all task operations
- Ownership verification for all task/subtask operations
- Password validation
- Secure password hashing

## 📝 Usage

1. **Sign Up:** Create a new account
2. **Login:** Sign in with your credentials
3. **Dashboard:** View your task summary and recent tasks
4. **Create Task:** Add a new task with title, description, priority, status, and due date
5. **View Tasks:** Browse all your tasks with search and filter options
6. **Edit/Delete:** Modify or remove tasks and subtasks
7. **Add Subtasks:** Break down tasks into smaller subtasks

## 🐛 Error Handling

The application includes comprehensive error handling:

- **Form Validation:** Client and server-side validation
- **404 Errors:** Custom page for not found resources
- **403 Errors:** Custom page for permission denied
- **500 Errors:** Custom page for server errors
- **User Messages:** Django messages framework for user feedback

## 🧪 Testing

To test the application:

1. Create a user account
2. Create several tasks with different priorities and statuses
3. Add subtasks to tasks
4. Test search and filter functionality
5. Test error scenarios (try accessing non-existent tasks, etc.)

## 📄 License

This project is open source and available for educational purposes.

## 👨‍💻 Development

For development, make sure to:
- Keep DEBUG=True in settings.py (development only)
- Use SQLite3 for local development
- Run `python manage.py collectstatic` if deploying

## 🚀 Deployment Notes

Before deploying to production:
1. Change `SECRET_KEY` in settings.py
2. Set `DEBUG=False`
3. Configure `ALLOWED_HOSTS`
4. Set up a production database (PostgreSQL recommended)
5. Configure static files serving
6. Set up proper security headers

---

**Enjoy managing your tasks!** 🎉

