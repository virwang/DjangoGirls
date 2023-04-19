@REM 切換至虛擬環境，並打包專案
@REM 定義檔案名稱
set "filename=mysite"
@REM 啟動虛擬機
python -m venv djangogirls_venv
@REM 打包zip
python -m zipfile -c %filename%.zip mysite