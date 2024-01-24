@echo off
call .\env\Scripts\activate
set FLASK_APP=main.py
cd .\app\
flask run

@echo off
call .\env\Scripts\activate
cd .\app\
set FLASK_APP=index.py
flask run