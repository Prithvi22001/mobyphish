# Mobyphish Website

## Getting Started

Follow these steps to set up a local development environment for the Mobyphish website.

### Prerequisites

Ensure you have Python 3 installed on your system. You can download it from [here](https://www.python.org/downloads/).

### Step-by-Step Guide

1. **Create a Virtual Environment**

   To create a virtual environment, open your terminal or command prompt and run the following command:

   ```sh
   python3 -m venv env
   ```

   This will create a new virtual environment named `env`.

2. **Activate the Virtual Environment**

   Activate the virtual environment by running the appropriate command for your operating system:

   - **For Windows:**

     ```sh
     .\env\Scripts\activate
     ```

   - **For macOS and Linux:**

     ```sh
     source env/bin/activate
     ```

3. **Install Required Packages**

   With the virtual environment activated, install the necessary packages by running:

   ```sh
   pip install -r requirements.txt
   ```

4. **Configure the Database**

   Open the `messaging/settings.py` file and ensure that the database configuration is set to use SQLite3 for local development:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.sqlite3',
           'NAME': BASE_DIR / 'db.sqlite3',
       }
   }
   ```

   Note: The production database uses PostgreSQL, which is configured on the server and not accessible locally.Make sure that is commented out else you would face erro when starting the server.

5. **Run the Development Server**

   Start the local development server by running:

   ```sh
   python3 manage.py makemigrations
   python3 manage.py migrate
   python3 manage.py runserver
   ```

   The website will be accessible at `http://127.0.0.1:8000/`.

---

Feel free to let me know if there are any additional details you need included!
