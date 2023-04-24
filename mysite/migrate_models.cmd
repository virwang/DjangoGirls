@REM 連結model 與資料庫
@REM 導向 ./mysite/
@REM cd mysite 
@REM 建立model
python manage.py makemigrations
@REM 寫入資料庫
python manage.py  migrate