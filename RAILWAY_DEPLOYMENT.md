# Railway Deployment Guide

This guide will help you deploy your Django Task Manager application to Railway.

## Prerequisites

1. A GitHub account with your repository: https://github.com/KomalSakhiUllah/dijango_project
2. A Railway account (sign up at https://railway.app)

## Step 1: Push to GitHub

First, make sure your code is pushed to GitHub:

```bash
git init
git add .
git commit -m "Initial commit: Django Task Manager"
git branch -M main
git remote add origin https://github.com/KomalSakhiUllah/dijango_project.git
git push -u origin main
```

## Step 2: Deploy to Railway

### Option A: Deploy via Railway Dashboard

1. **Sign in to Railway:**
   - Go to https://railway.app
   - Sign in with your GitHub account

2. **Create New Project:**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your repository: `KomalSakhiUllah/dijango_project`

3. **Configure Environment Variables:**
   - Go to your project settings
   - Click on "Variables" tab
   - Add these environment variables:
     ```
     SECRET_KEY=your-secret-key-here (generate a strong random key)
     DEBUG=False
     ALLOWED_HOSTS=your-app-name.up.railway.app
     ```

4. **Add PostgreSQL Database (Optional but Recommended):**
   - In Railway dashboard, click "New"
   - Select "Database" → "Add PostgreSQL"
   - Railway will automatically set the `DATABASE_URL` environment variable

5. **Deploy:**
   - Railway will automatically detect your Django project
   - It will run migrations and start the server
   - Your app will be available at: `https://your-app-name.up.railway.app`

### Option B: Deploy via Railway CLI

1. **Install Railway CLI:**
   ```bash
   npm install -g @railway/cli
   ```

2. **Login to Railway:**
   ```bash
   railway login
   ```

3. **Initialize Railway:**
   ```bash
   railway init
   ```

4. **Set Environment Variables:**
   ```bash
   railway variables set SECRET_KEY=your-secret-key-here
   railway variables set DEBUG=False
   railway variables set ALLOWED_HOSTS=your-app-name.up.railway.app
   ```

5. **Add PostgreSQL:**
   ```bash
   railway add postgresql
   ```

6. **Deploy:**
   ```bash
   railway up
   ```

## Step 3: Generate Secret Key

Generate a secure secret key for production:

```python
# Run this in Python
import secrets
print(secrets.token_urlsafe(50))
```

Or use this command:
```bash
python -c "import secrets; print(secrets.token_urlsafe(50))"
```

## Step 4: Configure Static Files

Railway will automatically collect static files during deployment. The `whitenoise` package is already included in `requirements.txt` to serve static files.

## Step 5: Access Your Application

Once deployed, Railway will provide you with a URL like:
```
https://your-app-name.up.railway.app
```

Visit this URL to access your Task Manager application!

## Troubleshooting

### Static Files Not Loading
- Make sure `whitenoise` is in `requirements.txt`
- Check that `STATIC_ROOT` is set correctly
- Railway should run `collectstatic` automatically

### Database Issues
- If using PostgreSQL, make sure the database service is added
- Check that `DATABASE_URL` is set automatically by Railway
- Run migrations: `railway run python manage.py migrate`

### Application Not Starting
- Check Railway logs for errors
- Verify all environment variables are set
- Make sure `ALLOWED_HOSTS` includes your Railway domain

## Custom Domain (Optional)

1. In Railway dashboard, go to your service
2. Click "Settings" → "Networking"
3. Add your custom domain
4. Update `ALLOWED_HOSTS` to include your custom domain

## Monitoring

- View logs in Railway dashboard
- Check metrics and usage
- Set up alerts if needed

---

**Your Task Manager is now live on Railway! 🚀**

