# !/usr/bin/env python3
import sys
import json
import os
import base64
import subprocess
import platform
import datetime
import time
import glob
import decimal

#import Thirdparty packages
import pymssql
import pymysql
import lib.python3_8.site_packages.DateConvertor as dt
import psutil
import dmidecode
import requests
from requests.auth import HTTPBasicAuth
import urllib3


# global variable
logPath             = None
errorLogPath        = None

#workingDirectory = "/d/DtecMonitor/Monitoring_ClientSide_Git/Monitoring_ClientSide/"
saveToFile          = None
project_isonline    = None
offline_history     = None
offline_sitePath    = None
sitepath            = None
sqltype             = None
token               = None
WsvUser             = None
WsvPass             = None
sql_server          = None
sql_username        = None
sql_password        = None
sql_database_name   = None
sql_port            = None

# end of global variable

def writeErrorToFile(msg):
    # try:
    # file = open("/home/abbas/Desktop/"+str(datetime.datetime.now().dsudo apt install libodbc1ate())+".txt", "a+")
    file = open(errorLogPath + "Error_" + str(datetime.datetime.now().date()) + ".txt", "a+")
    file.write(str(datetime.datetime.now()) + ":" + str(msg) + "\r\n")
    file.close()
    # except Exception as exx:>
    #   print(exx)

def writeLogToFile(msg):
    # try:
    # file = open("/home/abbas/Desktop/"+str(datetime.datetime.now().date())+".txt", "a+")
    file = open(logPath + "Log_" + str(datetime.datetime.now().date()) + ".txt", "a+")
    file.write(str(datetime.datetime.now()) + ":" + str(msg) + "\r\n")
    file.close()
    # except Exception as exx:
    #   print(exx)

def asymetricAbbas(txt):
    # Ab sa li
    newText = txt
    newText = base64.b64encode(str(txt).encode("utf-8"))
    newText = str(newText).replace("A", "Ab").replace("s", "sa").replace("l", "li")
    return newText

def asymetricAbbas2(txt):
    # Ab sa li
    newText = txt
    newText = base64.b64encode(str(newText).encode("utf-8"))
    newText = str(newText).replace("c", "zc").replace("a", "ya").replace("B", "yB").replace("A", "FA").replace("s","XU").replace("L", "LI").replace("1", "91").replace("2", "82").replace("3", "73").replace("4", "64")
    return newText

def de_asymetricAbbas2(txt):
    # Ab sa li
    newText = txt
    newText = str(newText).replace("b'", "").replace("'", "").replace('b"', '').replace('"', '').replace("zc",
                                                                                                         "c").replace(
        "ya", "a").replace("yB", "B").replace("FA", "A").replace("XU", "s").replace("LI", "L").replace("91",
                                                                                                       "1").replace(
        "82", "2").replace("73", "3").replace("64", "4")
    newText = base64.b64decode(str(newText)).decode("utf-8")
    newText = newText.replace("'", "").replace('"', '')
    return newText

def doPing(hostname):
    # ping = os.system("ping -c 1 " + hostname)
    param = '-n' if platform.system().lower() == 'windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', hostname]
    subprocess.call(command)

def emptyResult(projectname):
    json_response = "{"
    json_response += "'projectname':'" + projectname + "'"
    json_response += ",'dbcon':2"
    json_response += ",'cpu_percent':'0'"
    json_response += ",'mem_percent':'0'"
    json_response += ",'disk':'0'"
    json_response += ",'webservice':'2'"
    json_response += ",'users':'Server Not Rechable'"
    json_response += ",'backup':'2'"
    json_response += "}"
    json_response = json_response.replace("'", "\"")
    siteContent = "b'"+asymetricAbbas(json_response)+"'"
    return siteContent


def saveData(sitelist): 
    global offline_sitePath
    global sitepath
    global sql_server
    global sql_username
    global sql_password
    global sql_database_name
    global sql_port

    # if project has access to internet
    if (project_isonline == "1"):
        try:
            if (saveToFile == "1"):
                f = open(sitepath, "w")
                f.write("<html><body>" + sitelist + "</body></html>")
                f.close()
            if (saveToFile == "0"):  # write to database

                if (sqltype == "Mssql"):
                    conn = pymssql.connect(server=de_asymetricAbbas2(sql_server) ,user=de_asymetricAbbas2(sql_username) ,password=de_asymetricAbbas2(sql_password),database=de_asymetricAbbas2(sql_database_name) ,port=sql_port)
                    cursor = conn.cursor(as_dict=True)
               
                if (sqltype == "Mysql"):
                    conn = pymysql.connect(host=de_asymetricAbbas2(sql_server) ,user=de_asymetricAbbas2(sql_username) ,password=de_asymetricAbbas2(sql_password),database=de_asymetricAbbas2(sql_database_name) ,port=int(sql_port),cursorclass=pymysql.cursors.DictCursor)
                    cursor = conn.cursor()

                
                # delete the Old History
                cursor.execute("delete from sitescan; ")
                cursor.execute(
                    "insert into sitescan(sitecontent,regDateTime) values('" + sitelist.replace("b'", "").replace("###", "").replace(
                        "'", "") + "','" + str(datetime.datetime.now()) + "');")

                conn.commit()
                conn.close()
        except Exception as fileex:
            writeErrorToFile("save data isonline:"+str(fileex))

    # if project type os offline, then save file per scan
    if (project_isonline == "0"):
        try:
            if (saveToFile == "1"):
                offline_sitePath = offline_sitePath + "sitescan_" + str(datetime.datetime.now().date()) + "_" + str(
                    datetime.datetime.now().time())[0:5].replace(":", "-") + ".dtec"
                f = open(offline_sitePath, "w")
                f.write("<html><body>" + sitelist + "</body></html>")
                f.close()
                fileList = glob.glob(offline_sitePath + "*.dtec")
                now = time.time()
                for filePath in fileList:
                    try:
                        if os.stat(filePath).st_mtime < now - (int(offline_history) * 86400):
                            os.remove(filePath)
                    except Exception as ex:
                        writeErrorToFile("save data project online =1"+str(ex))

            if (saveToFile == "0"):  # write to database
                
                if (sqltype == "Mssql"):
                    conn = pymssql.connect(server=de_asymetricAbbas2(sql_server) ,user=de_asymetricAbbas2(sql_username) ,password=de_asymetricAbbas2(sql_password),database=de_asymetricAbbas2(sql_database_name) ,port=sql_port)
                    cursor = conn.cursor(as_dict=True)
               
                if (sqltype == "Mysql"):
                    conn = pymysql.connect(host=de_asymetricAbbas2(sql_server) ,user=de_asymetricAbbas2(sql_username) ,password=de_asymetricAbbas2(sql_password),database=de_asymetricAbbas2(sql_database_name) ,port=int(sql_port),cursorclass=pymysql.cursors.DictCursor)
                    cursor = conn.cursor()

                cursor.execute(
                    "insert into sitescan(sitecontent,regDateTime) values('" + sitelist.replace("b'", "").replace("###", "").replace(
                        "'", "") + "','" + str(datetime.datetime.now()) + "');")
                # delete the Old History
                cursor.execute("delete from sitescan where regDateTime<='" + str(
                    datetime.datetime.now() - datetime.timedelta(days=int(offline_history))) + "'")
                # cursor.execute("delete from sitescan where regDateTime<='" + str(datetime.datetime.now() - datetime.timedelta(seconds=50)) + "'")
                conn.commit
                conn.close()
        except Exception as fileex:
            writeErrorToFile("save end:"+str(fileex))

def monitorSite(project_dict):
    # define vaiables
    global logPath
    global saveToFile
    global project_isonline
    global errorLogPath
    global offline_history
    global offline_sitePath
    global sitepath
    global sqltype
    global token
    global WsvUser            
    global WsvPass
    global sql_server
    global sql_username
    global sql_password
    global sql_database_name
    global sql_port
    
    
    siteContent = ""
      
    # json_file = open('project.config')
    # data = json.load(json_file)

    sql_server = project_dict['SQL_server']
    sql_username = project_dict['SQL_username']
    sql_password = project_dict['SQL_password']
    sql_database_name = project_dict['SQL_database_name']
    sql_port = project_dict['SQL_port']
    projectname = project_dict['projectname']
    sqltype = project_dict['SqlType']  # Mssql or Mssql
    ostype = project_dict['OsType']  # Windows or Linux
    diskpath = eval(project_dict['DiskPath'])  # array of drives or path
    webservice = eval(project_dict['WebService'])  # array of webservice
    dbbackuppath = project_dict['DbBackupPath']
    minimumdisksize = project_dict['MinimumDiskSize']
    lastbackupdate = project_dict['LastBackupDate']  # day
    serial1 = project_dict['Serial1']
    serial2 = project_dict['Serial2']
    
    project_isonline = project_dict['project_isonline']
    offline_history = project_dict['offline_history']
    offline_sitePath = project_dict['offline_sitePath']
    logPath = project_dict['logPath']
    errorLogPath = project_dict['logPath']
    saveToFile = project_dict['saveToFile']
    readFromFile = project_dict['readFromFile']
    

    # end of vaiables

    if(readFromFile == "2"): #read from html file of remote server
        try:
            urllib3.disable_warnings()
            session = requests.Session()
            response = session.get(offline_sitePath,verify=False,)
            siteContent = response.text.replace("<html><body>","").replace("</body></html>","")
            
           
            if (siteContent!="" and len(siteContent)>10 and  not siteContent.startswith("b")):
                siteContent = "b'" + siteContent + "'"
           
            if (siteContent=="" and len(siteContent)<10):
                return emptyResult(projectname)
           
        except Exception as sexxx:
            writeErrorToFile("readFromFile:"+str(sexxx))
            return emptyResult(projectname)

        
        return siteContent


    # siteResponse = siteResponse.Replace("'</body></html>", "").Replace("<html><body>b'", "");
    if (readFromFile == "0"):  # read ready data from database
        try:
            
            query = "select top 1 siteContent from sitescan order by regdatetime desc"  # for sqlserver
            
            if (sqltype == "Mysql"):
                query = "select siteContent from sitescan order by regdatetime desc limit 1"  # for mysql
            
            if (sqltype == "Mssql"):
                conn = pymssql.connect(server=de_asymetricAbbas2(sql_server) ,user=de_asymetricAbbas2(sql_username) ,password=de_asymetricAbbas2(sql_password),database=de_asymetricAbbas2(sql_database_name) ,port=sql_port)
                cursor = conn.cursor(as_dict=True)
               
            if (sqltype == "Mysql"):
                conn = pymysql.connect(host=de_asymetricAbbas2(sql_server) ,user=de_asymetricAbbas2(sql_username) ,password=de_asymetricAbbas2(sql_password),database=de_asymetricAbbas2(sql_database_name) ,port=int(sql_port),cursorclass=pymysql.cursors.DictCursor)
                cursor = conn.cursor()
            
            
            cursor.execute(query)
           
            row = cursor.fetchone()
           
            siteContent = str(row['siteContent'])
          
            conn.close()
         
            
            if (siteContent!="" and len(siteContent)>10 and  not siteContent.startswith("b")):
                siteContent = "b'" + siteContent + "'"
           
            if (siteContent=="" and len(siteContent)<10):
                return emptyResult(projectname)

        except Exception as sexx:
            writeErrorToFile("readFromFile == 0"+str(sexx))

        return siteContent

    # Actual Read Data
    errmsg = ""
    json_response = "{"
    try:  # connect to database
        json_response += "'projectname':'" + projectname + "'"
        if (sqltype != "false"):

           

            if (sqltype == "Mssql"):
                conn = pymssql.connect(server=de_asymetricAbbas2(sql_server) ,user=de_asymetricAbbas2(sql_username) ,password=de_asymetricAbbas2(sql_password),database=de_asymetricAbbas2(sql_database_name) ,port=sql_port)
                cursor = conn.cursor(as_dict=True)
               
            if (sqltype == "Mysql"):
                conn = pymysql.connect(host=de_asymetricAbbas2(sql_server) ,user=de_asymetricAbbas2(sql_username) ,password=de_asymetricAbbas2(sql_password),database=de_asymetricAbbas2(sql_database_name) ,port=int(sql_port),cursorclass=pymysql.cursors.DictCursor)
                cursor = conn.cursor()
                
            conn.close()
            json_response += ",'dbcon':1"
        else:
            json_response += ",'dbcon':2"


    except Exception as sqlex:
        json_response += ",'dbcon':0"
        errmsg += "DbCon=" + str(sqlex)
        writeErrorToFile("connect to database:"+str(sqlex))
       

    try:  # cpu percentage

        cpu_load = round(psutil.getloadavg()[2] / psutil.cpu_count(), 2)
        cpu_percent = psutil.cpu_percent(interval=0.01, percpu=False)
        json_response += ",'cpu_percent':" + str(cpu_percent) + ""
        json_response += ",'cpu_load':" + str(cpu_load) + ""

    except Exception as cpuex:
        json_response += ",'cpu_percent':0"
        errmsg += "cpu=" + str(cpuex)

    try:  # memory
        mem_percent = psutil.virtual_memory().percent
        mem_total = round(psutil.virtual_memory().total / (1024.0 ** 3), 1)
        mem_used = round(psutil.virtual_memory().used / (1024.0 ** 3), 1)
        mem_availabel = round(psutil.virtual_memory().available / (1024.0 ** 3), 1)

        json_response += ",'mem_percent':" + str(mem_percent) + ""
        json_response += ",'mem_total':" + str(mem_total) + ""
        json_response += ",'mem_used':" + str(mem_used) + ""
        json_response += ",'mem_availabel':" + str(mem_availabel) + ""

    except Exception as memoryex:
        json_response += ",'mem_percent':0"
        errmsg += "Mem=" + str(memoryex)

    try:  # disk
        #json_response += ",'Disk':[";
        diskRz =1
        for disk in diskpath:

            try:
                #json_response += "{";
                drive_size = disk.split(";")
                partition = disk
                partitionsize = minimumdisksize
                if (len(drive_size) == 2):
                    partition = drive_size[0]
                    partitionsize = drive_size[1]

                disk_percent = psutil.disk_usage(partition).percent
                disk_total = round(psutil.disk_usage(partition).total / (1024.0 ** 3), 2)
                disk_free = round(psutil.disk_usage(partition).free / (1024.0 ** 3), 2)
                disk_used = round(psutil.disk_usage(partition).used / (1024.0 ** 3), 2)

                if(diskRz==1):
                    if (disk_free < int(partitionsize)):
                        diskRz=0
                       

                json_response += ",'disk_percent_" + partition + "=':" + str(disk_percent) + ""
                json_response += ",'disk_total_" + partition + "=':" + str(disk_total) + ""
                json_response += ",'disk_free_" + partition + "=':" + str(disk_free) + ""
                json_response += ",'disk_used_" + partition + "=':" + str(disk_used) + ""
                #json_response += "},";
            except Exception as diskIex:
                diskRz=0
                errmsg += "Disk=" + str(diskIex)

        if(diskRz==1):
            json_response += ",'disk':1"
        else:
            json_response += ",'disk':0"
            

        
        #json_response += "]";
        
    except Exception as diskex:
        json_response += ",'disk':0"
        errmsg += "Disk=" + str(diskex)

    try:  # Web Service
        #json_response += ",'WebService':[";
        webServiceRz=1
        for wsv in webservice:
            ServiceName = wsv[wsv.rfind("/")+1:]
            try:
                my_headers = {'Authorization' : 'Bearer '+token+''}
                if(len(token)>5 and len(WsvUser)<1):
                    response = requests.get(wsv, headers=my_headers)
                if(len(WsvUser)>2 and len(token)<1):
                    response = requests.get(wsv, auth=HTTPBasicAuth(WsvUser, WsvPass))    
                if(len(WsvUser)>2 and len(token)>5):
                    response = requests.get(wsv, headers=my_headers,auth=HTTPBasicAuth(WsvUser, WsvPass))

                response_json = response.json()
                
                if(webServiceRz==1):
                    if(int(response_json['rz'])==1):
                        webServiceRz=1
                    else:
                        webServiceRz=0

                
                wsrv_status="0"
                wsrv_response = "-1"
                wsrv_msg="-1"
       
                try:
                    wsrv_status = str(response.status_code).replace("'","").replace("\"","")
                except Exception as wsvexInt:
                    wsrv_status="0"
                try:
                    wsrv_response = str(response_json['rz']).replace("'","").replace("\"","")
                except Exception as wsvexInt:
                    wsrv_response = "-1"
                try:
                    wsrv_msg = str(response_json['msg']).replace("'","").replace("\"","").replace("[","").replace("]","")
                except Exception as wsvexInt:
                    wsrv_msg="-1"

                
                
                json_response += ",'webserviceStatusCode_" + ServiceName + "=':'"+wsrv_status+"'"
                json_response += ",'webservice_" + ServiceName + "=':'"+wsrv_response+"'"
                json_response += ",'webserviceDetail_" + ServiceName + "=':'"+wsrv_msg+"'"

               
                
                              
                #json_response += "},";
            except Exception as wsvexInt:
                webServiceRz=0
                writeErrorToFile(" Web Service_Int_" + ServiceName + "=':"+str(wsvexInt))
                json_response += ",'webserviceDetail_" + ServiceName + "=':'"+str(wsvexInt)+"'"
                errmsg += "webservice=" + str(wsvexInt)
        
        if (len(webservice)==0):
            json_response += ",'webservice':'2'"
        
        if(webServiceRz==1):
            json_response += ",'webservice':'1'"
        else:
            json_response += ",'webservice':'0'"
        #json_response += "]";
        
    except Exception as wsvex:
        json_response += ",'webservice':'0'"
        errmsg += "webservice=" + str(wsvex)
        writeErrorToFile(" Web Service:"+str(wsvex))

    
    try:  # connected users
        users = psutil.users()
        json_response += ",'users':'" + str(users).replace("'", "").replace(":", "-").replace("[", "").replace("]","") + "'"
    except Exception as userex:
        errmsg += "User=" + str(userex)

    try:  # Backup file
        if (dbbackuppath == "false"):
            json_response += ",'backup':2"
        else:
            now = datetime.datetime.today()  # Get current date
            list_of_files = glob.glob(dbbackuppath)
            latest_file = max(list_of_files, key=os.path.getctime)  # get latest file created in folder
            backupdate = datetime.datetime.fromtimestamp(os.path.getctime(latest_file))
            dateDif = (now - backupdate).days
            if (dateDif > 1):
                json_response += ",'backup':0"
            else:
                json_response += ",'backup':1"
            json_response += ",'latest_file':'" + latest_file + "'"

    except Exception as backupex:
        json_response += ",'backup':0"
        errmsg += "backup=" + str(backupex)

    try: # DMIDecode 
        if (ostype == "Linux"):
            dmi = dmidecode.DMIDecode()
            json_response += ",'Manufacturer':'" + str(dmi.manufacturer()) + "'"
            json_response += ",'Model':'" + str(dmi.model()) + "'"
            json_response += ",'Firmware':'" + str(dmi.firmware()) + "'"
            serial1_temp = dmi.serial_number()

            if (serial1_temp != "Not Specified"):
                serial1 = serial1_temp
            serial2 = dmi.cpu_num()
            json_response += ",'CoresCount':'" + str(dmi.total_enabled_cores()) + "'"
            json_response += ",'ProcessorType':'" + str(dmi.cpu_type()) + "'"
            json_response += ",'CpuNum':'" + str(serial2) + "'"

        if (ostype == "Windows"):
            json_response += ",'Manufacturer':'" + str(
                subprocess.check_output("wmic computersystem get manufacturer").decode()).lower().replace(
                "manufacturer", "").replace("\n", "").replace("\r", "").replace(" ", "") + "'"
            json_response += ",'Model':'" + str(
                subprocess.check_output("wmic computersystem get model").decode()).lower().replace("model", "").replace(
                "\n", "").replace("\r", "").replace(" ", "") + "'"
            json_response += ",'CoresCount':'" + str(
                subprocess.check_output("wmic computersystem get NumberOfProcessors").decode()).lower().replace(
                "numberofprocessors", "").replace("\n", "").replace("\r", "").replace(" ", "") + "'"
            json_response += ",'CpuNum':'" + str(
                subprocess.check_output("wmic computersystem get NumberOfLogicalProcessors").decode()).lower().replace(
                "numberoflogicalprocessors", "").replace("\n", "").replace("\r", "").replace(" ", "") + "'"
            serial2 = str(subprocess.check_output("wmic csproduct get uuid").decode()).lower().replace("uuid",
                                                                                                       "").replace("\n",
                                                                                                                   "").replace(
                "\r", "").replace(" ", "")
            serial1 = str(subprocess.check_output("WMIC BIOS GET SERIALNUMBER").decode()).lower().replace(
                "serialnumber", "").replace("\n", "").replace("\r", "").replace(" ", "")
            json_response += ",'Serial2':'" + str(serial2) + "'"

    except Exception as sysex:
        errmsg += "sys=" + str(sysex)

    json_response += ",'Serial1':'" + str(serial1) + "'"
    json_response += ",'Date':'" + str(datetime.datetime.now()) + "'"
    json_response += ",'Time':'" + str(datetime.datetime.now().time())[0:5] + "'"
    json_response += ",'errmsg':'" + errmsg.replace("'", "").replace("\"", "").replace(":", "-").replace("[",
                                                                                                         "").replace(
        "]", "").replace("#", "").replace("\n", "").replace("\r", "").replace("\t", "") + "'}"
    json_response = json_response.replace("'", "\"")
    # print(json_response)
    siteContent = asymetricAbbas(json_response)

    #saveData(siteContent)
    return siteContent



# monitorSite()

#connn = pymssql.connect(server='.', user='sa', password='123', database='Emdad_Mosharekat',port=1433)


if (len(sys.argv) > 1):
    if (str(sys.argv[1]) == "enc"):
        print(sys.argv[2])
        x = asymetricAbbas2(sys.argv[2])
        print(x)
        y = de_asymetricAbbas2(x)
        print(y)
    if (str(sys.argv[1]) == "ping"):
        doPing(sys.argv[2])
else:
    try:
        workingDirectory = os.path.dirname(os.path.abspath(__file__)) +"\\"
        if(platform.system()=="Windows"):
            workingDirectory = os.path.dirname(os.path.abspath(__file__)) +"\\"
        else:
            workingDirectory = os.path.dirname(os.path.abspath(__file__)) +"/"

        json_file = open(workingDirectory+'project.config')
        data = json.load(json_file)
        sitepath = data['SitePath']
        token    = data['WsvToken']
        WsvUser  = data['WsvUser']
        WsvPass  = data['WsvPass']
             
        
        #sitelist=[]
        sitelist = ""
        for project in data['project_Config']:
            rz = monitorSite(project)
            if(rz!="" and len(rz)>10):
                if(rz.endswith("###")):
                    sitelist = sitelist + rz
                else:
                    sitelist = sitelist + rz +"###"
                
        #sitelist = sitelist + "]";
        saveData(sitelist)

            
    except Exception as jsonex:
        #print("::: "+str(jsonex))
        writeErrorToFile("Json File Exception:" + str(jsonex))



  