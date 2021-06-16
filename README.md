# Social Web

*This is a simple social web app that uses **Django** as a backend framework*


**Requirements**

+ Python3.9, Django3.1.7

1. Create a virtual enviroment for this project with the command **python3 -m venv venv**.

2. Activate venv via the command: __source venv/bin/activate__. if successfully,
 your terminal will now say **venv** at the begining of each line.
3. You must copy a sample of .env-sample in .env file with **cp .env-sample .env**.

3. install all of the required packages and extensions with **pip3 install -r requirements.txt**.

4. Run the following command to get the database ready to go

 python3 manage.py migrate


*Everything should be ready! You can run the server via the command (python manage.py runserver) and this site will be available at http://localhost:8000*
