import sys
import sqlite3


def db_select(table, where):

	#connect to DB
	conn = sqlite3.connect('../db.sqlite3')
	c = conn.cursor()
	
	query = "select * from " + table + where 
	
	#call stored Procedure
	c.execute(query)
	r = c.fetchall()
	#Do what is needed to get results to UI
	#TODO Figure out what UI needs to make use of results
	#for no print for testing
	
	#close connection
	conn.close()
	return (r)
	
def db_insert(table, values):
	#connect to DB
	conn = sqlite3.connect('../db.sqlite3')
	c = conn.cursor()
	query = "insert into " + table + " values" + values
	#call stored Procedure
	c.execute(query)
	conn.commit()
	#Do what is needed to get results to UI
	#TODO Figure out what UI needs to make use of results
	#for no print for testing
	
	#close connection
	conn.close()
	return
	
def db_delete(table, where):
	#connect to DB
	conn = sqlite3.connect('../db.sqlite3')
	c = conn.cursor()
	query = "delete from " + table + " where " + where
	#call stored Procedure
	c.execute("delete from tables_user where username = 'root1'")
	conn.commit()
	#Do what is needed to get results to UI
	#TODO Figure out what UI needs to make use of results
	#for no print for testing
	
	#close connection
	conn.close()
	return

#TODO#
#Create Log File
#update This code to send results to UI
#create stored proc
#findout connection to DB
