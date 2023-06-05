# movies_app
#Appsilon Home work Assignment
# Developer Details
-  Name : Ugwuegbu Nnamdi Godfrey
-  Email : nugwuegbu089@gmail.com
records of movies from after 2013 on wikidata using SPARQL 

# Dependencies
Python 3.7+
Django 4.x

# DBMS
Mysql Database

# Installation Process
- Git glone repo
- create .env file and replace the content using the content of .env.example ensure that your Database credentials are correct
- create the virtual environment venv 
- run pip install -r requirements from terminal
- apply migrations using python manager makemigrations and python manage.py migrate
- open javascript file name : fixed_values.js in static/js folder , replace the IP address 127.0.0.1:8000 with your app URL and port number
- create a user using python manage.py createsuperuser and then follow prompts
- launch the app on the displayed port on the terminal
- login with the user created earlier
- load wikidata using the loadData Button the dashbaord when u are loggedIn and wait for the data to load
- you will see the records loaded when the loading completes


