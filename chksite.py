import sys
import json
# sudo apt-get install python3-pymysql
import pymysql
import urllib3
import smtplib
import SiteList as site
import DateConvertor as dt
import requests
import datetime
#import zeep

"""
print(sys.argv[0])
print(sys.argv[1])
print(sys.argv[2])
"""
try:
    if(len(sys.argv)>1):
        global_oid=sys.argv[1]
    else:
        global_oid = 102
except Exception as argx:
    print("Error:"+str(argx))

MySQL_server = 'localhost'
MySQL_username = 'root'
MySQL_password = 'Dtec@dmin1690'
MySQL_database_name = 'wf_support'
MySQL_port = 3306

MySQLServer_args = {'host': MySQL_server, 'user': MySQL_username, 'password': MySQL_password,'database': MySQL_database_name, 'port': MySQL_port}
jsonWebSite = site.SiteCollection.jsonWebSite

jsonWebSites = jsonWebSite.replace(" ","").replace("\n","")
pWebSites    = json.loads(jsonWebSites)
lst_unsuccess_site = []


def writeErrorToFile(msg):
    #try:
    # file = open("/home/abbas/Desktop/"+str(datetime.datetime.now().date())+".txt", "a+")
    file = open("/home/rmax/sitemonitor/Error_" + str(datetime.datetime.now().date()) + ".txt", "a+")
    file.write(str(datetime.datetime.now()) + ":" + str(msg) + "\r\n")
    file.close()
    #except Exception as exx:
     #   print(exx)

def writeLogToFile(msg):
    #try:
    # file = open("/home/abbas/Desktop/"+str(datetime.datetime.now().date())+".txt", "a+")
    file = open("/home/rmax/sitemonitor/Log_" + str(datetime.datetime.now().date()) + ".txt", "a+")
    file.write(str(datetime.datetime.now()) + ":" + str(msg) + "\r\n")
    file.close()
    #except Exception as exx:
     #   print(exx)

def checkSiteAvailability():
    http = urllib3.PoolManager(maxsize=50)
    statuscode =0
    errmsg=""

    index = 0
    for project in pWebSites["project_list"]:
        try:
            r= http.request("GET", project["projecturl"])
            statuscode  = r.status
            #jsonResponse   = r.data
            jsonResponse   = ""
        except Exception as argx:
            pWebSites["project_list"][index]["errmsg"] = str(argx)
            statuscode = 0
            jsonResponse = ""

        if (statuscode!= 200 ):
            lst_unsuccess_site.append(index)
            pWebSites["project_list"][index]["statuscode"] = str(statuscode)

            ## set response data
            try:
                if (jsonResponse != ""):
                    pResponse = json.loads(jsonResponse)
                    #fill json ...
                    # pWebSites["project_list"][index]["hdd"]=pResponse["hdd"]
            except Exception as ag:
                jsonResponse = ""

        ######## Insert to mysql #########
        conn_MySQL   = pymysql.connect(**MySQLServer_args)
        MySQL_cursor = conn_MySQL.cursor()
        monitordate  = dt.DateConvert.gregorian_to_jalali(datetime.datetime.now().year,datetime.datetime.now().month,datetime.datetime.now().day)
        monitortime  = str(datetime.datetime.now().hour) + ":" + str(datetime.datetime.now().minute)
        projectname  = pWebSites["project_list"][index]["projectname"]

        insert_query = (" INSERT INTO wf_support.INDEP_SITEMONITOR "+
                         " (MONITORDATE,MONITORTIME, PROJECTNAME, STATUSCODE, DISK, CPU, MEM, DBCON, BACKUP, SERIAL1, SERIAL2, JSONDATA) "+
                         " VALUES("+str(monitordate)+",'"+monitortime+"' ,'"+projectname+"',"+str(statuscode)+", 1,1, 1, 1, 1, '', '', ''); ")
        try:
            MySQL_cursor.execute(insert_query)
            conn_MySQL.commit()
            conn_MySQL.close()
        except Exception as ax:
            writeErrorToFile(ax)

        index = index + 1

def sendSMS():
    # Gmail Sign In
    # Gmail Sign In
    url = 'http://webservice.iran.tc/URL/'
    for item in lst_unsuccess_site:
        projectname = pWebSites["project_list"][item]["projectname"]
        projecturl  = pWebSites["project_list"][item]["projecturl"]
        errmsg      = pWebSites["project_list"][item]["errmsg"]
        Receivers   = pWebSites["project_list"][item]["Receivers"]
        CellPhones  = pWebSites["project_list"][item]["CellPhones"]
        statuscode = pWebSites["project_list"][item]["statuscode"]

        TEXT = " project name:" + projectname + "\n" + " status code:"+str(statuscode) + "\n" + " error message:"+ errmsg
        for sms in CellPhones.split(','):
           try:
               formdata={'uid':'abbasali_g',
                            'pass':'135406001NwDIC',
                            'tel':sms,
                            'body':TEXT
                         }
               requests.post(url, data=formdata)
           except  Exception as smsx:
               writeErrorToFile(smsx)

def sendEmail():
    # Gmail Sign In
    # Gmail Sign In
    gmail_sender = "dadehtamin@gmail.com"
    gmail_passwd = "DDtec1690"

    emaile_server = smtplib.SMTP("smtp.gmail.com", 587)
    emaile_server.ehlo()
    emaile_server.starttls()
    emaile_server.ehlo()
    try:
        emaile_server.login(gmail_sender, gmail_passwd)
    except  Exception as emailx1:
        writeErrorToFile(emailx1)


    for item in lst_unsuccess_site:
        projectname = pWebSites["project_list"][item]["projectname"]
        projecturl  = pWebSites["project_list"][item]["projecturl"]
        errmsg      = pWebSites["project_list"][item]["errmsg"]
        Receivers   = pWebSites["project_list"][item]["Receivers"]
        CellPhones  = pWebSites["project_list"][item]["CellPhones"]
        statuscode = pWebSites["project_list"][item]["statuscode"]

        SUBJECT = projectname + ":monitor error"
        TEXT = " project name:" + projectname + "\n" + " status code:"+str(statuscode) + "\n" + " error message:"+ errmsg
        for email in Receivers.split(','):
            Receipient =email
            BODY = "\r\n".join(["To: %s" % Receipient,
                        "From: %s" % gmail_sender,
                        "Subject: %s" % SUBJECT,
                        "", TEXT])
            try:
                emaile_server.sendmail(gmail_sender, Receipient, BODY)
            except  Exception as emailx:
                writeErrorToFile(emailx)

    emaile_server.quit()

checkSiteAvailability()
sendSMS()
sendEmail()
