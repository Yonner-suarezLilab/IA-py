@echo off
call .\env\Scripts\activate
set FLASK_APP=main.py
cd .\app\
flask run
