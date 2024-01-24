@echo off
call .\env\Scripts\activate
cd .\app\
set FLASK_APP=index.py
flask run