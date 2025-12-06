# Complete Deployment Script for Django Task Manager
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Django Task Manager - Full Deployment" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Step 1: Check Git Status
Write-Host "Step 1: Checking Git status..." -ForegroundColor Yellow
$status = git status --short
if ($status) {
    Write-Host "Uncommitted changes detected. Committing..." -ForegroundColor Yellow
    git add -A
    git commit -m "Update before deployment"
}

# Step 2: Push to GitHub
Write-Host "`nStep 2: Pushing to GitHub..." -ForegroundColor Yellow
Write-Host "You may need to authenticate. Options:" -ForegroundColor Cyan
Write-Host "1. Browser will open for GitHub login" -ForegroundColor White
Write-Host "2. Or use Personal Access Token" -ForegroundColor White
Write-Host ""
$push = Read-Host "Press Enter to push to GitHub (or Ctrl+C to cancel)"
git push -u origin main

if ($LASTEXITCODE -eq 0) {
    Write-Host "`n✅ Successfully pushed to GitHub!" -ForegroundColor Green
} else {
    Write-Host "`n❌ Failed to push. Please check authentication." -ForegroundColor Red
    Write-Host "`nTo create a Personal Access Token:" -ForegroundColor Yellow
    Write-Host "1. Go to: https://github.com/settings/tokens" -ForegroundColor White
    Write-Host "2. Generate new token (classic)" -ForegroundColor White
    Write-Host "3. Select 'repo' scope" -ForegroundColor White
    Write-Host "4. Copy token and use it as password when pushing" -ForegroundColor White
    exit 1
}

# Step 3: Generate Secret Key
Write-Host "`nStep 3: Generating SECRET_KEY for Railway..." -ForegroundColor Yellow
$python = "C:\Users\DELL\AppData\Local\Programs\Python\Python312\python.exe"
$secretKey = & $python -c "import secrets; print(secrets.token_urlsafe(50))"
Write-Host "`nYour SECRET_KEY (save this for Railway):" -ForegroundColor Green
Write-Host $secretKey -ForegroundColor Cyan
Write-Host ""

# Step 4: Railway Deployment Instructions
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Step 4: Deploy to Railway" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "1. Go to: https://railway.app" -ForegroundColor Yellow
Write-Host "2. Sign in with GitHub" -ForegroundColor Yellow
Write-Host "3. Click 'New Project' → 'Deploy from GitHub repo'" -ForegroundColor Yellow
Write-Host "4. Select: KomalSakhiUllah/dijango_project" -ForegroundColor Yellow
Write-Host "5. Add Environment Variables:" -ForegroundColor Yellow
Write-Host "   - SECRET_KEY = $secretKey" -ForegroundColor Cyan
Write-Host "   - DEBUG = False" -ForegroundColor Cyan
Write-Host "6. Add PostgreSQL database (optional)" -ForegroundColor Yellow
Write-Host "7. Wait for deployment (2-5 minutes)" -ForegroundColor Yellow
Write-Host ""
Write-Host "Your app will be live at: https://your-app-name.up.railway.app" -ForegroundColor Green
Write-Host ""

# Open Railway in browser
$openRailway = Read-Host "Open Railway in browser? (Y/N)"
if ($openRailway -eq "Y" -or $openRailway -eq "y") {
    Start-Process "https://railway.app"
}

Write-Host "`n✅ Deployment preparation complete!" -ForegroundColor Green
Write-Host "Your code is on GitHub. Now deploy on Railway!" -ForegroundColor Cyan

