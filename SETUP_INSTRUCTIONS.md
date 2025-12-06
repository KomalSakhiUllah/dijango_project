# Setup Instructions

## ⚠️ Python Installation Required

It appears Python is not properly configured on your system. Follow these steps:

### Step 1: Install Python

1. **Download Python:**
   - Go to https://www.python.org/downloads/
   - Download Python 3.8 or higher
   - **IMPORTANT:** During installation, check "Add Python to PATH"

2. **Verify Installation:**
   Open a new PowerShell/Command Prompt and run:
   ```bash
   python --version
   ```
   You should see something like: `Python 3.x.x`

### Step 2: Install Django

Once Python is installed, open PowerShell/Command Prompt in this directory and run:

```bash
pip install -r requirements.txt
```

### Step 3: Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 4: Start the Server

**Option 1: Use the batch file**
```bash
run_server.bat
```

**Option 2: Manual commands**
```bash
python manage.py runserver
```

### Step 5: Access the Application

Open your browser and go to:
```
http://127.0.0.1:8000/
```

You'll see the splash screen which automatically redirects to the login page.

---

## 🚀 Quick Start (After Python is Installed)

If Python is already installed but not in PATH, you may need to:

1. **Find Python installation:**
   - Common locations:
     - `C:\Python3x\python.exe`
     - `C:\Users\YourName\AppData\Local\Programs\Python\Python3x\python.exe`
     - `C:\Program Files\Python3x\python.exe`

2. **Use full path:**
   ```bash
   "C:\Python3x\python.exe" manage.py runserver
   ```

3. **Or add Python to PATH:**
   - Search "Environment Variables" in Windows
   - Edit "Path" variable
   - Add Python installation directory

---

## ✅ Verification Checklist

- [ ] Python is installed (`python --version` works)
- [ ] Django is installed (`pip list | findstr Django`)
- [ ] Migrations are run (`python manage.py migrate`)
- [ ] Server starts without errors
- [ ] Browser can access `http://127.0.0.1:8000/`

---

## 🆘 Troubleshooting

### "python is not recognized"
- Python is not in PATH
- Reinstall Python with "Add to PATH" checked
- Or use full path to python.exe

### "No module named 'django'"
- Run: `pip install -r requirements.txt`

### "ModuleNotFoundError: No module named 'encodings'"
- Python installation is corrupted
- Reinstall Python from python.org

### Port 8000 already in use
- Use a different port: `python manage.py runserver 8001`

---

Need help? Check the main README.md for more details.

