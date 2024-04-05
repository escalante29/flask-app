# flask-app
Flask App

Based on: https://testdriven.io/courses/learn-flask/

➜  flask-app git:(main) python3 -m venv venv
➜  flask-app git:(main) source venv/bin/activate

(venv) ➜  flask-app git:(main) ✗ pip install Flask
(venv) ➜  flask-app git:(main) ✗ pip install --upgrade pip
(venv) ➜  flask-app git:(main) ✗  pip freeze | grep "Flask==" >> requirements.txt

(venv) ➜  flask-app git:(main) ✗ flask --app app --debug run