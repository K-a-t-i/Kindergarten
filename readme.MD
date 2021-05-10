Project set up on windows 
python 3.8
Using google cloud platform and cloud based database postgresql


Every Time You Develop on Your Project
https://github.com/DrAdamRoe/foundations-project-template/blob/main/readme.MD
Every time you restart your computer or reopenVSCode, you'll have to do a few things. Instructions for macOS and Linux distributions assume you are using a Bash shell. Instructions for Windows assume you are using the Command Prompt. Instructions for other shells can be found online.

    • Activate your virtual environment for this project:
      Windows: venv\Scripts\activate.bat
    • Point Flask to your application:
      macOS/Linux: export FLASK_APP=main.py
      Windows: set FLASK_APP=main.py
    • Enable hot reloading, debug mode, and other useful features for local development:
      macOS/Linux: export FLASK_ENV=development
      Windows: set FLASK_ENV=development
    • run your flask application:
      flask run


$ export/set FLASK_APP=applicaton.py 
$ python -m flask run
 * Running on http://127.0.0.1:5000/

$ set FLASK_ENV=development
$ This launches a very simple builtin server, which is good enough for testing but probably not what you want to use in production. 
$ This does the following things:
    1. it activates the debugger
    2. it activates the automatic reloader
    3. it enables the debug mode on the Flask application.

You can also control debug mode separately from the environment by exporting FLASK_DEBUG=1.

export FLASK_DEBUG=1 
environment Variable to run application.py
FLASK_APP=application.py
python -m flask run

To test your app:
pytest --doctest-modules
To Lint your app:
flake8 --exclude venv
