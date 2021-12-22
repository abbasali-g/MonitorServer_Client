@echo off
set LOGFILE=c:\dtec_install.log
echo Installing python3 >> %LOGFILE%
echo Installing python3 ...
python-3.8.2.exe  >> %LOGFILE%
echo result: %ERRORLEVEL% >> %LOGFILE%
echo upgading pip -- if exists ...
python -m pip install --upgrade pip
set /p DUMMY=Hit  python installation done, Press ENTER to continue...

echo installing setuptools
pip3 install setuptools >> %LOGFILE%
echo result: %ERRORLEVEL%


echo installing pyodbc
pip3 install pyodbc >> %LOGFILE%
echo result: %ERRORLEVEL%

echo installing urllib3
pip3 install urllib3 >> %LOGFILE%
echo result: %ERRORLEVEL%

echo installing psutil
pip3 install psutil >> %LOGFILE%
echo result: %ERRORLEVEL%

echo installing py-dmidecode
pip3 install py-dmidecode >> %LOGFILE%
pip3 install dmidecode >> %LOGFILE%
echo result: %ERRORLEVEL%

echo installing wmi
pip3 install wmi  >> %LOGFILE%
echo result: %ERRORLEVEL% >> %LOGFILE%

echo installing mssql driver
msodbcsql.msi  >> %LOGFILE%
echo result: %ERRORLEVEL% >> %LOGFILE%
