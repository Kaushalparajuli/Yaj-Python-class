# Python Development Environment Setup Guide
## Complete Setup for macOS, Linux, and Windows

**Last Updated:** November 2025  
**Python Version:** 3.11+ (Recommended: 3.12)  
**Target Audience:** PHP Developers transitioning to Python/Django

---

## Table of Contents

1. [macOS Setup](#macos-setup)
2. [Linux Setup](#linux-setup)
3. [Windows Setup](#windows-setup)
4. [Virtual Environment Setup (All Platforms)](#virtual-environment-setup)
5. [IDE and Code Editor Setup](#ide-and-code-editor-setup)
6. [Essential Python Packages](#essential-python-packages)
7. [Django Project Setup](#django-project-setup)
8. [Database Setup](#database-setup)
9. [Troubleshooting](#troubleshooting)
10. [Verification Checklist](#verification-checklist)

---

## macOS Setup

### Method 1: Using Homebrew (Recommended)

#### Step 1: Install Homebrew
```bash
# Check if Homebrew is installed
brew --version

# If not installed, install Homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Add Homebrew to your PATH (for Apple Silicon Macs)
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"
```

#### Step 2: Install Python
```bash
# Update Homebrew
brew update

# Install Python 3.12
brew install python@3.12

# Verify installation
python3 --version
# Should output: Python 3.12.x

# Check pip installation
pip3 --version
```

#### Step 3: Set Python 3 as Default (Optional)
```bash
# Add to ~/.zshrc or ~/.bash_profile
echo 'alias python=python3' >> ~/.zshrc
echo 'alias pip=pip3' >> ~/.zshrc

# Reload shell configuration
source ~/.zshrc
```

### Method 2: Using Official Installer

#### Step 1: Download Python
1. Visit https://www.python.org/downloads/
2. Download the latest Python 3.12.x macOS installer
3. Choose the appropriate installer:
   - **macOS 64-bit universal2 installer** (for both Intel and Apple Silicon)

#### Step 2: Install Python
1. Open the downloaded `.pkg` file
2. Follow the installation wizard
3. Check "Add Python to PATH" if prompted
4. Complete the installation

#### Step 3: Verify Installation
```bash
# Open Terminal and verify
python3 --version
pip3 --version

# Install certificates (important for SSL)
/Applications/Python\ 3.12/Install\ Certificates.command
```

### Method 3: Using pyenv (Advanced - For Multiple Python Versions)

```bash
# Install pyenv via Homebrew
brew install pyenv

# Add pyenv to shell configuration
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc

# Reload shell
source ~/.zshrc

# Install Python 3.12
pyenv install 3.12.0

# Set as global version
pyenv global 3.12.0

# Verify
python --version
```

### Additional macOS Setup

#### Install Xcode Command Line Tools
```bash
xcode-select --install
```

#### Install PostgreSQL (for Django projects)
```bash
# Using Homebrew
brew install postgresql@15

# Start PostgreSQL
brew services start postgresql@15

# Create a database
createdb myproject_db
```

#### Install Git
```bash
brew install git
git --version
```

---

## Linux Setup

### Ubuntu/Debian-based Systems

#### Step 1: Update Package List
```bash
sudo apt update
sudo apt upgrade -y
```

#### Step 2: Install Python 3.12
```bash
# Add deadsnakes PPA for latest Python versions
sudo apt install software-properties-common -y
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt update

# Install Python 3.12
sudo apt install python3.12 -y

# Install pip for Python 3.12
sudo apt install python3.12-venv python3.12-dev -y

# Install pip separately if needed
curl -sS https://bootstrap.pypa.io/get-pip.py | python3.12

# Verify installation
python3.12 --version
pip3.12 --version
```

#### Step 3: Set Python 3.12 as Default (Optional)
```bash
# Update alternatives
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.12 1
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.12 1

# Verify
python3 --version
python --version
```

#### Step 4: Install Build Dependencies
```bash
# Essential development tools
sudo apt install build-essential libssl-dev libffi-dev python3-dev -y

# For PostgreSQL support
sudo apt install libpq-dev -y

# For image processing (Pillow)
sudo apt install libjpeg-dev zlib1g-dev -y
```

### Fedora/RHEL/CentOS-based Systems

```bash
# Update system
sudo dnf update -y

# Install Python 3.12
sudo dnf install python3.12 -y

# Install development tools
sudo dnf groupinstall "Development Tools" -y
sudo dnf install python3.12-devel -y

# Install pip
sudo dnf install python3.12-pip -y

# Verify
python3.12 --version
```

### Arch Linux

```bash
# Update system
sudo pacman -Syu

# Install Python
sudo pacman -S python python-pip

# Verify
python --version
pip --version
```

### Using pyenv on Linux (Recommended for Multiple Versions)

```bash
# Install dependencies (Ubuntu/Debian)
sudo apt install -y make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev \
libffi-dev liblzma-dev

# Install pyenv
curl https://pyenv.run | bash

# Add to ~/.bashrc or ~/.zshrc
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc

# Reload shell
source ~/.bashrc

# Install Python
pyenv install 3.12.0
pyenv global 3.12.0

# Verify
python --version
```

### Additional Linux Setup

#### Install PostgreSQL
```bash
# Ubuntu/Debian
sudo apt install postgresql postgresql-contrib -y
sudo systemctl start postgresql
sudo systemctl enable postgresql

# Fedora/RHEL
sudo dnf install postgresql-server postgresql-contrib -y
sudo postgresql-setup --initdb
sudo systemctl start postgresql
sudo systemctl enable postgresql

# Create database
sudo -u postgres createdb myproject_db
sudo -u postgres createuser myuser
```

#### Install Git
```bash
# Ubuntu/Debian
sudo apt install git -y

# Fedora/RHEL
sudo dnf install git -y

# Verify
git --version
```

---

## Windows Setup

### Method 1: Using Official Installer (Recommended)

#### Step 1: Download Python
1. Visit https://www.python.org/downloads/windows/
2. Download **Python 3.12.x Windows installer (64-bit)**
3. Choose the executable installer

#### Step 2: Install Python
1. Run the downloaded `.exe` file
2. **IMPORTANT:** Check "Add python.exe to PATH" at the bottom
3. Click "Install Now" (or choose "Customize installation" for advanced options)
4. If customizing:
   - Check all "Optional Features"
   - Check "Add Python to environment variables"
   - Choose installation directory (default is fine)
5. Wait for installation to complete
6. Click "Disable path length limit" if prompted (recommended)
7. Click "Close"

#### Step 3: Verify Installation
```powershell
# Open Command Prompt or PowerShell
python --version
# Should output: Python 3.12.x

pip --version
# Should output: pip xx.x.x
```

### Method 2: Using Microsoft Store

1. Open Microsoft Store
2. Search for "Python 3.12"
3. Click "Get" or "Install"
4. Python will be added to PATH automatically
5. Verify in Command Prompt:
```powershell
python --version
```

### Method 3: Using Windows Package Manager (winget)

```powershell
# Open PowerShell as Administrator
winget install Python.Python.3.12

# Verify
python --version
```

### Method 4: Using Chocolatey

```powershell
# Install Chocolatey first (if not installed)
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

# Install Python
choco install python312 -y

# Refresh environment variables
refreshenv

# Verify
python --version
```

### Additional Windows Setup

#### Update pip
```powershell
python -m pip install --upgrade pip
```

#### Install Build Tools for Windows (for packages that need compilation)
1. Download "Build Tools for Visual Studio" from:
   https://visualstudio.microsoft.com/downloads/
2. Run the installer
3. Select "Desktop development with C++"
4. Install

#### Install Git for Windows
```powershell
# Using winget
winget install Git.Git

# Or download from
https://git-scm.com/download/win
```

#### Install PostgreSQL
1. Download from https://www.postgresql.org/download/windows/
2. Run the installer
3. Set password for postgres user
4. Default port: 5432
5. Complete installation

Or using Chocolatey:
```powershell
choco install postgresql -y
```

#### Set Up Windows Terminal (Recommended)
```powershell
# Install Windows Terminal from Microsoft Store
# Or using winget
winget install Microsoft.WindowsTerminal
```

### Configuring PATH (if not automatically added)

```powershell
# Check current PATH
echo $env:PATH

# Add Python to PATH manually (if needed)
# Replace C:\Python312 with your installation path
[Environment]::SetEnvironmentVariable("Path", "$env:Path;C:\Python312;C:\Python312\Scripts", "User")
```

---

## Virtual Environment Setup

Virtual environments isolate project dependencies (similar to `node_modules` in Node.js or `vendor` in PHP).

### Creating a Virtual Environment

#### macOS/Linux
```bash
# Navigate to your project directory
cd ~/projects/myproject

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Your prompt should change to show (venv)
(venv) username@computer:~/projects/myproject$

# Deactivate when done
deactivate
```

#### Windows (Command Prompt)
```cmd
# Navigate to project directory
cd C:\projects\myproject

# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate.bat

# Your prompt should change to show (venv)
(venv) C:\projects\myproject>

# Deactivate when done
deactivate
```

#### Windows (PowerShell)
```powershell
# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\Activate.ps1

# If you get an execution policy error:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Then try activating again
venv\Scripts\Activate.ps1

# Deactivate when done
deactivate
```

### Alternative: Using virtualenvwrapper (macOS/Linux)

```bash
# Install virtualenvwrapper
pip3 install virtualenvwrapper

# Add to ~/.bashrc or ~/.zshrc
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/projects
source /usr/local/bin/virtualenvwrapper.sh

# Reload shell
source ~/.bashrc

# Create new environment
mkvirtualenv myproject

# Activate environment
workon myproject

# Deactivate
deactivate

# Delete environment
rmvirtualenv myproject

# List all environments
lsvirtualenv
```

### Alternative: Using conda (All Platforms)

```bash
# Download and install Miniconda
# https://docs.conda.io/en/latest/miniconda.html

# Create environment
conda create -n myproject python=3.12

# Activate environment
conda activate myproject

# Deactivate
conda deactivate

# List environments
conda env list

# Remove environment
conda env remove -n myproject
```

---

## IDE and Code Editor Setup

### Visual Studio Code (Recommended)

#### Installation

**macOS:**
```bash
brew install --cask visual-studio-code
```

**Linux:**
```bash
# Ubuntu/Debian
sudo snap install code --classic

# Or download from https://code.visualstudio.com/
```

**Windows:**
```powershell
# Using winget
winget install Microsoft.VisualStudioCode

# Or download from https://code.visualstudio.com/
```

#### Essential Python Extensions

1. **Python** (by Microsoft) - IntelliSense, linting, debugging
2. **Pylance** - Fast language server
3. **Python Indent** - Correct Python indentation
4. **autoDocstring** - Generate docstrings
5. **Django** - Django template support
6. **Better Comments** - Improved comment highlighting
7. **GitLens** - Enhanced Git integration
8. **Thunder Client** - API testing (like Postman)

#### VS Code Setup
```bash
# Open VS Code
code .

# Install extensions via command line
code --install-extension ms-python.python
code --install-extension ms-python.vscode-pylance
code --install-extension njpwerner.autodocstring
code --install-extension batisteo.vscode-django
```

#### Configure VS Code settings.json
```json
{
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": true,
    "python.formatting.provider": "black",
    "python.linting.lintOnSave": true,
    "editor.formatOnSave": true,
    "python.testing.pytestEnabled": true,
    "[python]": {
        "editor.defaultFormatter": "ms-python.black-formatter",
        "editor.formatOnSave": true,
        "editor.codeActionsOnSave": {
            "source.organizeImports": true
        }
    }
}
```

### PyCharm (Professional IDE)

#### Installation

**macOS:**
```bash
brew install --cask pycharm-ce  # Community Edition (Free)
# or
brew install --cask pycharm     # Professional (Paid)
```

**Linux:**
```bash
# Download from https://www.jetbrains.com/pycharm/download/
# Or use snap
sudo snap install pycharm-community --classic
```

**Windows:**
- Download from https://www.jetbrains.com/pycharm/download/
- Run the installer
- Follow installation wizard

#### PyCharm Setup
1. Open PyCharm
2. Configure Python Interpreter:
   - File → Settings → Project → Python Interpreter
   - Add interpreter → Virtualenv Environment
   - Select your virtual environment
3. Enable Django support:
   - Settings → Languages & Frameworks → Django
   - Enable Django Support
   - Set Django project root

### Sublime Text

```bash
# macOS
brew install --cask sublime-text

# Ubuntu/Debian
wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -
sudo apt install sublime-text

# Windows
winget install SublimeHQ.SublimeText.4
```

---

## Essential Python Packages

### Installing Common Packages

```bash
# Make sure virtual environment is activated
# Install essential packages

# Upgrade pip first
pip install --upgrade pip

# Django and Django REST Framework
pip install django djangorestframework

# Database drivers
pip install psycopg2-binary  # PostgreSQL
pip install mysqlclient      # MySQL

# Environment variables
pip install python-decouple python-dotenv

# API and HTTP
pip install requests

# Testing
pip install pytest pytest-django pytest-cov

# Code quality
pip install black pylint flake8 mypy

# Utilities
pip install python-dateutil pillow

# CORS headers for Django
pip install django-cors-headers

# Authentication
pip install djangorestframework-simplejwt

# Debugging
pip install django-debug-toolbar ipython

# Task queue
pip install celery redis
```

### Creating requirements.txt

```bash
# After installing all packages
pip freeze > requirements.txt

# To install from requirements.txt
pip install -r requirements.txt
```

### Example requirements.txt for Django Project

```txt
Django==4.2.7
djangorestframework==3.14.0
psycopg2-binary==2.9.9
python-decouple==3.8
requests==2.31.0
pillow==10.1.0
django-cors-headers==4.3.0
djangorestframework-simplejwt==5.3.0
celery==5.3.4
redis==5.0.1
gunicorn==21.2.0

# Development dependencies
pytest==7.4.3
pytest-django==4.7.0
pytest-cov==4.1.0
black==23.11.0
pylint==3.0.2
flake8==6.1.0
mypy==1.7.1
django-debug-toolbar==4.2.0
ipython==8.18.1
```

---

## Django Project Setup

### Step-by-Step Django Setup

```bash
# 1. Create project directory
mkdir myproject
cd myproject

# 2. Create virtual environment
python3 -m venv venv

# 3. Activate virtual environment
# macOS/Linux:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# 4. Upgrade pip
pip install --upgrade pip

# 5. Install Django
pip install django

# 6. Create Django project
django-admin startproject config .
# The dot (.) creates project in current directory

# 7. Create an app
python manage.py startapp users

# 8. Run migrations
python manage.py migrate

# 9. Create superuser
python manage.py createsuperuser

# 10. Run development server
python manage.py runserver

# Visit http://127.0.0.1:8000/
```

### Project Structure

```
myproject/
├── venv/                  # Virtual environment (don't commit)
├── config/                # Project configuration
│   ├── __init__.py
│   ├── settings.py       # Project settings
│   ├── urls.py          # Main URL configuration
│   ├── asgi.py          # ASGI config
│   └── wsgi.py          # WSGI config
├── users/                # App
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── manage.py             # Django management script
└── requirements.txt      # Project dependencies
```

### Essential Django Settings

```python
# config/settings.py

# Add apps to INSTALLED_APPS
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Third-party apps
    'rest_framework',
    'corsheaders',
    
    # Local apps
    'users',
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # Add CORS
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'myproject_db',
        'USER': 'myuser',
        'PASSWORD': 'mypassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# REST Framework settings
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}

# CORS settings
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]
```

### Using Environment Variables

```bash
# Install python-decouple
pip install python-decouple

# Create .env file in project root
touch .env
```

**.env file:**
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
DATABASE_NAME=myproject_db
DATABASE_USER=myuser
DATABASE_PASSWORD=mypassword
DATABASE_HOST=localhost
DATABASE_PORT=5432
ALLOWED_HOSTS=localhost,127.0.0.1
```

**settings.py:**
```python
from decouple import config, Csv

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='', cast=Csv())

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DATABASE_NAME'),
        'USER': config('DATABASE_USER'),
        'PASSWORD': config('DATABASE_PASSWORD'),
        'HOST': config('DATABASE_HOST'),
        'PORT': config('DATABASE_PORT'),
    }
}
```

---

## Database Setup

### PostgreSQL Setup

#### macOS
```bash
# Install PostgreSQL
brew install postgresql@15

# Start PostgreSQL service
brew services start postgresql@15

# Create database and user
createdb myproject_db
psql postgres

# In psql:
CREATE USER myuser WITH PASSWORD 'mypassword';
ALTER ROLE myuser SET client_encoding TO 'utf8';
ALTER ROLE myuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE myuser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE myproject_db TO myuser;
\q
```

#### Linux (Ubuntu/Debian)
```bash
# Install PostgreSQL
sudo apt install postgresql postgresql-contrib -y

# Start service
sudo systemctl start postgresql
sudo systemctl enable postgresql

# Create database and user
sudo -u postgres psql

# In psql:
CREATE DATABASE myproject_db;
CREATE USER myuser WITH PASSWORD 'mypassword';
ALTER ROLE myuser SET client_encoding TO 'utf8';
ALTER ROLE myuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE myuser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE myproject_db TO myuser;
\q
```

#### Windows
```powershell
# Using installer from postgresql.org
# Or using Chocolatey:
choco install postgresql -y

# After installation, use pgAdmin or psql
# Open SQL Shell (psql)

CREATE DATABASE myproject_db;
CREATE USER myuser WITH PASSWORD 'mypassword';
GRANT ALL PRIVILEGES ON DATABASE myproject_db TO myuser;
```

### SQLite (Default for Django)

No installation needed! Django uses SQLite by default for development.

```python
# settings.py (default)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

### MySQL Setup

#### macOS
```bash
brew install mysql
brew services start mysql
mysql_secure_installation

# Create database
mysql -u root -p
CREATE DATABASE myproject_db;
CREATE USER 'myuser'@'localhost' IDENTIFIED BY 'mypassword';
GRANT ALL PRIVILEGES ON myproject_db.* TO 'myuser'@'localhost';
FLUSH PRIVILEGES;
```

#### Linux
```bash
sudo apt install mysql-server -y
sudo mysql_secure_installation

sudo mysql
CREATE DATABASE myproject_db;
CREATE USER 'myuser'@'localhost' IDENTIFIED BY 'mypassword';
GRANT ALL PRIVILEGES ON myproject_db.* TO 'myuser'@'localhost';
FLUSH PRIVILEGES;
```

---

## Troubleshooting

### Common Issues and Solutions

#### Issue: "python: command not found"

**Solution:**
```bash
# Try python3 instead
python3 --version

# Or add alias (macOS/Linux)
echo 'alias python=python3' >> ~/.bashrc
source ~/.bashrc
```

#### Issue: pip install fails with permission error

**Solution:**
```bash
# Never use sudo with pip in virtual environment
# Make sure virtual environment is activated
source venv/bin/activate

# Then install
pip install package_name
```

#### Issue: SSL certificate error on macOS

**Solution:**
```bash
# Run the certificate installer
/Applications/Python\ 3.12/Install\ Certificates.command
```

#### Issue: ModuleNotFoundError after installing package

**Solution:**
```bash
# Make sure virtual environment is activated
which python  # Should point to venv/bin/python

# Reinstall the package
pip install --upgrade --force-reinstall package_name
```

#### Issue: Django command not found

**Solution:**
```bash
# Make sure Django is installed in the active environment
pip install django

# Use python -m django instead
python -m django --version
python manage.py runserver
```

#### Issue: PostgreSQL connection refused

**Solution:**
```bash
# Check if PostgreSQL is running
# macOS
brew services list

# Linux
sudo systemctl status postgresql

# Start if not running
brew services start postgresql@15  # macOS
sudo systemctl start postgresql     # Linux
```

#### Issue: Port 8000 already in use

**Solution:**
```bash
# Run on different port
python manage.py runserver 8080

# Or find and kill process using port 8000
# macOS/Linux
lsof -i :8000
kill -9 PID

# Windows
netstat -ano | findstr :8000
taskkill /PID PID /F
```

#### Issue: Virtual environment not activating on Windows PowerShell

**Solution:**
```powershell
# Change execution policy
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Then activate
venv\Scripts\Activate.ps1
```

---

## Verification Checklist

Use this checklist to verify your setup is complete:

### Basic Setup
- [ ] Python 3.11+ installed and in PATH
- [ ] `python --version` or `python3 --version` works
- [ ] pip installed and working
- [ ] Virtual environment created successfully
- [ ] Virtual environment activates without errors

### Development Tools
- [ ] Code editor/IDE installed (VS Code, PyCharm, etc.)
- [ ] Python extensions installed in editor
- [ ] Git installed and configured
- [ ] Terminal/command prompt configured

### Python Packages
- [ ] Django installed in virtual environment
- [ ] Django REST Framework installed
- [ ] Database driver installed (psycopg2, mysqlclient, etc.)
- [ ] Development tools installed (black, pylint, pytest)
- [ ] requirements.txt created

### Django Project
- [ ] Django project created
- [ ] Can run `python manage.py runserver`
- [ ] Can access http://127.0.0.1:8000/
- [ ] Admin interface accessible at /admin/
- [ ] Superuser created
- [ ] Database connected and migrations work

### Database
- [ ] Database server installed (PostgreSQL/MySQL/SQLite)
- [ ] Database created
- [ ] Database user created with permissions
- [ ] Django can connect to database
- [ ] Migrations run successfully

### Final Tests

```bash
# Test Python
python --version
# Expected: Python 3.11+ or 3.12+

# Test pip
pip --version
# Expected: pip xx.x.x

# Test Django
python -m django --version
# Expected: 4.2.x or higher

# Test virtual environment
which python  # macOS/Linux
where python  # Windows
# Should point to your venv directory

# Test database connection
python manage.py dbshell
# Should connect to your database

# Test running server
python manage.py runserver
# Should start without errors

# Test creating superuser
python manage.py createsuperuser
# Should create user successfully

# Test admin access
# Visit http://127.0.0.1:8000/admin/
# Should be able to login
```

---

## Quick Command Reference

### Virtual Environment Commands

```bash
# Create
python -m venv venv

# Activate
source venv/bin/activate          # macOS/Linux
venv\Scripts\activate.bat         # Windows CMD
venv\Scripts\Activate.ps1         # Windows PowerShell

# Deactivate
deactivate

# Delete (just remove folder)
rm -rf venv                       # macOS/Linux
rmdir /s venv                     # Windows
```

### pip Commands

```bash
# Install package
pip install package_name

# Install from requirements
pip install -r requirements.txt

# Update package
pip install --upgrade package_name

# Uninstall package
pip uninstall package_name

# List installed packages
pip list

# Show package info
pip show package_name

# Create requirements file
pip freeze > requirements.txt
```

### Django Commands

```bash
# Create project
django-admin startproject projectname

# Create app
python manage.py startapp appname

# Run server
python manage.py runserver
python manage.py runserver 8080  # Custom port

# Database migrations
python manage.py makemigrations
python manage.py migrate
python manage.py showmigrations

# Create superuser
python manage.py createsuperuser

# Django shell
python manage.py shell

# Collect static files
python manage.py collectstatic

# Run tests
python manage.py test

# Database shell
python manage.py dbshell
```

---

## Next Steps

After completing this setup:

1. **Complete the Python Crash Course** - Work through the syllabus
2. **Build a Django Project** - Start with a simple CRUD application
3. **Learn Django REST Framework** - Build APIs
4. **Set up deployment** - Learn Docker, Gunicorn, Nginx
5. **Join Python communities** - Reddit, Discord, Stack Overflow

---

## Additional Resources

### Documentation
- Python: https://docs.python.org/3/
- Django: https://docs.djangoproject.com/
- DRF: https://www.django-rest-framework.org/

### Learning Platforms
- Real Python: https://realpython.com/
- Django for Beginners: https://djangoforbeginners.com/
- Python Package Index: https://pypi.org/

### Communities
- r/Python: https://reddit.com/r/python
- r/django: https://reddit.com/r/django
- Django Discord: https://discord.gg/django
- Python Discord: https://discord.gg/python

---

**Happy Coding! 🐍🚀**

*If you encounter any issues not covered in this guide, please refer to the official documentation or reach out to the Python/Django community for support.*
