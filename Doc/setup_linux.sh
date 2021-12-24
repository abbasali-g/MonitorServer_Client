#!/bin/bash
apt update -y
apt install -y python3-dev
apt install -y python3-pip
pip3 install --upgrade setuptools
sudo apt install gcc gcc-8 g++-8
apt install -y unixodbc-dev
sudo apt install libodbc1
#sudo apt install python3-pyodbc
#pip3 install  pyodbc
#pip3 install --user pyodbc
pip3 install pymssql
pip3 install pymysql
pip3 install psutil
pip3 install urllib3
pip3 install py-dmidecode
pip3 install requests
pip3 install simple-crypt

#install mssql odbc driver version for ubuntu 18.4
curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
curl https://packages.microsoft.com/config/ubuntu/18.04/prod.list > /etc/apt/sources.list.d/mssql-release.list
#exit
apt-get update
ACCEPT_EULA=Y apt-get install msodbcsql17
# optional: for bcp and sqlcmd
ACCEPT_EULA=Y apt-get install mssql-tools
echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bash_profile
echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc
source ~/.bashrc
#end of install mssql odbc driver

#install mysql odbc driver
File=mysql-connector-odbc-8.0.19-linux-ubuntu18.04-x86-64bit.tar.gz
if [ ! -f "$File" ]; then
  echo "$File not exists, please download the file and copy here"
  exit
fi
tar xvf mysql-connector-odbc-8.0.19-linux-ubuntu18.04-x86-64bit.tar.gz
cp mysql-connector-odbc-8.0.19-linux-ubuntu18.04-x86-64bit/bin/* /usr/local/bin
cp mysql-connector-odbc-8.0.19-linux-ubuntu18.04-x86-64bit/lib/* /usr/local/lib
chmod 777 /usr/local/lib/libmy*
#apt-get install libodbc1
dpkg -i libodbc1_2.3.6-0.1+b1_amd64.deb
#apt-get install odbcinst1debian2
dpkg -i odbcinst1debian2_2.3.6-0.1+b1_amd64.deb
#Registers the Unicode driver:
myodbc-installer -a -d -n "MySQL ODBC 8.0 Driver" -t "Driver=/usr/local/lib/libmyodbc8w.so"
#Registers the ANSI driver
myodbc-installer -a -d -n "MySQL ODBC 8.0" -t "Driver=/usr/local/lib/libmyodbc8a.so"
