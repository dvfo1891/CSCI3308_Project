import sys
import MySQLdb

try:
	#connect to DB
	mysql = MySQLdb.connect(user = User, passwd=Passwd,db="DB")
	mysql_cursor = myslq.cursor()

	#call stored Procedure
	mysql_cursor.execute( "call stored Proc;", "variables for stored proc")
	results = mysql_cursor.fetchall()
	
	#Do what is needed to get results to UI
	#TODO Figure out what UI needs to make use of results
	#for no print for testing
	print results

	#close connection
	mysql_cursor.close()
	mysql.close

#if Error with connection, ext. print error
except MySQLdb.Error, e:
	print "mySQL Error %d: %s" % (e.args[0], e.args[1])
	sys.exit(1)

	#TODO#
	#Create Log File
	#update This code to send results to UI
	#create stored proc
	#findout connection to DB
