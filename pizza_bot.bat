@echo off

call %~dp0pizza_ShotaUAshota\venv\Scripts\activate

cd %~dp0pizza_ShotaUAshota

set TOKEN=6298594790:AAFoAx5cxwck9bz8iZKaUhEyhepDKPyogJw

python pizza_bot.py

pause