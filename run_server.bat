@echo off
echo ========================================
echo Task Manager - Django Application
echo ========================================
echo.

echo Step 1: Installing Django...
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)

echo.
echo Step 2: Creating database migrations...
python manage.py makemigrations
if errorlevel 1 (
    echo ERROR: Failed to create migrations
    pause
    exit /b 1
)

echo.
echo Step 3: Applying migrations...
python manage.py migrate
if errorlevel 1 (
    echo ERROR: Failed to apply migrations
    pause
    exit /b 1
)

echo.
echo Step 4: Starting development server...
echo.
echo ========================================
echo Server starting at http://127.0.0.1:8000/
echo Press Ctrl+C to stop the server
echo ========================================
echo.
python manage.py runserver

