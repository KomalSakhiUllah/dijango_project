# Task Manager Django Project - Setup and Run Script
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Task Manager - Django Application" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Find Python
$pythonPath = "C:\Users\DELL\AppData\Local\Programs\Python\Python312\python.exe"
if (-not (Test-Path $pythonPath)) {
    Write-Host "Python not found at expected location. Searching..." -ForegroundColor Yellow
    $pythonPath = Get-Command python -ErrorAction SilentlyContinue | Select-Object -ExpandProperty Source
    if (-not $pythonPath) {
        Write-Host "ERROR: Python not found. Please install Python first." -ForegroundColor Red
        pause
        exit 1
    }
}

Write-Host "Using Python: $pythonPath" -ForegroundColor Green
Write-Host ""

# Step 1: Install Django
Write-Host "Step 1: Installing Django..." -ForegroundColor Yellow
& $pythonPath -m pip install Django --quiet
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: Failed to install Django" -ForegroundColor Red
    pause
    exit 1
}
Write-Host "Django installed successfully!" -ForegroundColor Green
Write-Host ""

# Step 2: Create migrations
Write-Host "Step 2: Creating database migrations..." -ForegroundColor Yellow
& $pythonPath manage.py makemigrations
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: Failed to create migrations" -ForegroundColor Red
    pause
    exit 1
}
Write-Host "Migrations created!" -ForegroundColor Green
Write-Host ""

# Step 3: Apply migrations
Write-Host "Step 3: Applying migrations..." -ForegroundColor Yellow
& $pythonPath manage.py migrate
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: Failed to apply migrations" -ForegroundColor Red
    pause
    exit 1
}
Write-Host "Migrations applied!" -ForegroundColor Green
Write-Host ""

# Step 4: Start server
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Starting development server..." -ForegroundColor Cyan
Write-Host "Server will be available at: http://127.0.0.1:8000/" -ForegroundColor Green
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Yellow
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

& $pythonPath manage.py runserver

