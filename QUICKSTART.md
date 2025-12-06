# Quick Start Guide

## 🚀 Getting Started in 5 Steps

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Create Database Tables
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 3: Create Admin User (Optional)
```bash
python manage.py createsuperuser
```

### Step 4: Run the Server
```bash
python manage.py runserver
```

### Step 5: Open in Browser
Navigate to: `http://127.0.0.1:8000/`

You'll see the splash screen, which automatically redirects to the login page after 2.5 seconds.

## ✨ First Steps

1. **Sign Up** - Create your account
2. **Login** - Sign in with your credentials
3. **Create Task** - Add your first task
4. **Add Subtask** - Break down tasks into smaller pieces
5. **Explore** - Use search and filters to manage your tasks

## 🎯 Key Features to Try

- ✅ Create tasks with different priorities
- ✅ Search for tasks by title or description
- ✅ Filter by priority or status
- ✅ Add subtasks to organize work
- ✅ View dashboard statistics
- ✅ Edit and delete tasks

## 🐛 Testing Error Handling

Try these to see error handling in action:
- Access a non-existent task (404)
- Try to create duplicate task titles
- Submit forms with invalid data
- Try to access another user's tasks (403)

Enjoy your Task Manager! 🎉

