### How to run the project:

Clone the repository and open it in the command-line interface:

```
git clone https://github.com/tripleten-com/Iris4Friends
```

```
cd iris_for_friends
```

Create and activate a virtual environment:

Windows
```
python -m venv venv
source venv/Scripts/activate
```
Linux/macOS
```
python3 -m venv venv
source venv/bin/activate
```

Refresh PIP

Windows
```
python -m pip install --upgrade pip
```
Linux/macOS
```
python3 -m pip install --upgrade pip
```

Install the dependencies from the requirements.txt file:

```
pip install -r requirements.txt
```

Run migrations:

Windows
```
python manage.py makemigrations
python manage.py migrate
```

Linux/macOS
```
python3 manage.py makemigrations
python3 manage.py migrate
```

Run the project:

Windows
```
python manage.py runserver
```

Linux/macOS
```
python3 manage.py runserver
```
