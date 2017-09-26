"""
Timed storage ARP form
"""

import os
import time
import pyodbc
import datetime
import sys


while True:
        conn=pyodbc.connect('DRIVER={FreeTDS};SERVER=******;port=1433;DATABASE=******;UID=sa;PWD=******;TDS_Version=8.0;')
        print 'connect ok......'
        os.system('arp -a > ArpD.txt')
        f=open("ArpD.txt","r")
        cursor=conn.cursor()
        print "Saving new ARP cache data-----"
		i=datetime.datetime.now()
        for line in f:
                line_d=line.split(" ");
                a=line_d[1]
                b=line_d[3]
                c=line_d[5]
                sql = "INSERT INTO ArpSave(ip,mac,dtype,ctime) VALUES('%s','%s','%s','%s')"%(a,b,c,i)
                cursor.execute(sql)
                conn.commit()
		print "Saving OK"
		os.system('ip neigh flush  dev eth0')
        os.system('ip neigh flush  dev wlan0')
        print "ARP cache table data has been deleted"
        f.close()
        cursor.close()
        conn.close()
        print "deleted OK"
        time.sleep(60)
