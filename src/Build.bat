@echo off
rd /s /q ..\drafts
pelican content -s pelicanconf.py -o ..\
pause
