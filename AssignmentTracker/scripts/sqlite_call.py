import sys
rt sys
import sqlite3


def db_select_user(where):

#connect to DB
conn = sqlite3.connect('../db.sqlite3')
c = conn.cursor()

query = "select * from tables_user where" + where 

#call stored Procedure
c.execute(query)
r = c.fetchall()
#Do what is needed to get results to UI
#TODO Figure out what UI needs to make use of results
#for no print for testing

#close connection
conn.close()
return (r)

def db_insert_user(values):
#connect to DB
conn = sqlite3.connect('../db.sqlite3')
c = conn.cursor()
query = "insert into tables_user values" + values
#call stored Procedure
c.execute(query)
conn.commit()
#Do what is needed to get results to UI
#TODO Figure out what UI needs to make use of results
#for no print for testing

#close connection
conn.close()
return

def db_delete_user(where):
#connect to DB
conn = sqlite3.connect('../db.sqlite3')
c = conn.cursor()
query = "delete from tables_user where " + where
#call stored Procedure
c.execute("delete from tables_user where username = 'root1'")
conn.commit()
#Do what is needed to get results to UI
#TODO Figure out what UI needs to make use of results
#for no print for testing

#close connection
conn.close()
return



def db_select_course(where):

#connect to DB
conn = sqlite3.connect('../db.sqlite3')
c = conn.cursor()

query = "select * from tables_course where" + where 

#call stored Procedure
c.execute(query)
r = c.fetchall()
#Do what is needed to get results to UI
#TODO Figure out what UI needs to make use of results
#for no print for testing

#close connection
conn.close()
return (r)

def db_insert_course(values):
#connect to DB
conn = sqlite3.connect('../db.sqlite3')
c = conn.cursor()
query = "insert into tables_course values" + values
#call stored Procedure
c.execute(query)
conn.commit()
#Do what is needed to get results to UI
#TODO Figure out what UI needs to make use of results
#for no print for testing

#close connection
conn.close()
return

def db_delete_course(where):
#connect to DB
conn = sqlite3.connect('../db.sqlite3')
c = conn.cursor()
query = "delete from tables_course where " + where
#call stored Procedure
c.execute(query)
conn.commit()
#Do what is needed to get results to UI
#TODO Figure out what UI needs to make use of results
#for no print for testing

#close connection
conn.close()
return


def db_select_assignments(where):

#connect to DB
conn = sqlite3.connect('../db.sqlite3')
c = conn.cursor()

query = "select * from tables_assignments where" + where 

#call stored Procedure
c.execute(query)
r = c.fetchall()
#Do what is needed to get results to UI
#TODO Figure out what UI needs to make use of results
#for no print for testing

#close connection
conn.close()
return (r)

def db_insert_assignments(values):
#connect to DB
conn = sqlite3.connect('../db.sqlite3')
c = conn.cursor()
query = "insert into tables_assignments values" + values
#call stored Procedure
c.execute(query)
conn.commit()
#Do what is needed to get results to UI
#TODO Figure out what UI needs to make use of results
#for no print for testing

#close connection
conn.close()
return

def db_delete_assignments(where):
#connect to DB
conn = sqlite3.connect('../db.sqlite3')
c = conn.cursor()
query = "delete from tables_assignments where " + where
#call stored Procedure
c.execute(query)
conn.commit()
#Do what is needed to get results to UI
#TODO Figure out what UI needs to make use of results
#for no print for testing

#close connection
conn.close()
return
import sqlite3


def db_select_user(where):

	#connect to DB
	conn = sqlite3.connect('../db.sqlite3')
	c = conn.cursor()
	
	query = "select * from tables_user where" + where 
	
	#call stored Procedure
	c.execute(query)
	r = c.fetchall()
	#Do what is needed to get results to UI
	#TODO Figure out what UI needs to make use of results
	#for no print for testing
	
	#close connection
	conn.close()
	return (r)
	
def db_insert_user(values):
	#connect to DB
	conn = sqlite3.connect('../db.sqlite3')
	c = conn.cursor()
	query = "insert into tables_user values" + values
	#call stored Procedure
	c.execute(query)
	conn.commit()
	#Do what is needed to get results to UI
	#TODO Figure out what UI needs to make use of results
	#for no print for testing
	
	#close connection
	conn.close()
	return
	
def db_delete_user(where):
	#connect to DB
	conn = sqlite3.connect('../db.sqlite3')
	c = conn.cursor()
	query = "delete from tables_user where " + where
	#call stored Procedure
	c.execute("delete from tables_user where username = 'root1'")
	conn.commit()
	#Do what is needed to get results to UI
	#TODO Figure out what UI needs to make use of results
	#for no print for testing
	
	#close connection
	conn.close()
	return
	
	
	
def db_select_course(where):

	#connect to DB
	conn = sqlite3.connect('../db.sqlite3')
	c = conn.cursor()
	
	query = "select * from tables_course where" + where 
	
	#call stored Procedure
	c.execute(query)
	r = c.fetchall()
	#Do what is needed to get results to UI
	#TODO Figure out what UI needs to make use of results
	#for no print for testing
	
	#close connection
	conn.close()
	return (r)
	
def db_insert_course(values):
	#connect to DB
	conn = sqlite3.connect('../db.sqlite3')
	c = conn.cursor()
	query = "insert into tables_course values" + values
	#call stored Procedure
	c.execute(query)
	conn.commit()
	#Do what is needed to get results to UI
	#TODO Figure out what UI needs to make use of results
	#for no print for testing
	
	#close connection
	conn.close()
	return
	
def db_delete_course(where):
	#connect to DB
	conn = sqlite3.connect('../db.sqlite3')
	c = conn.cursor()
	query = "delete from tables_course where " + where
	#call stored Procedure
	c.execute(query)
	conn.commit()
	#Do what is needed to get results to UI
	#TODO Figure out what UI needs to make use of results
	#for no print for testing
	
	#close connection
	conn.close()
	return
	
	
def db_select_assignments(where):

	#connect to DB
	conn = sqlite3.connect('../db.sqlite3')
	c = conn.cursor()
	
	query = "select * from tables_assignments where" + where 
	
	#call stored Procedure
	c.execute(query)
	r = c.fetchall()
	#Do what is needed to get results to UI
	#TODO Figure out what UI needs to make use of results
	#for no print for testing
	
	#close connection
	conn.close()
	return (r)
	
def db_insert_assignments(values):
	#connect to DB
	conn = sqlite3.connect('../db.sqlite3')
	c = conn.cursor()
	query = "insert into tables_assignments values" + values
	#call stored Procedure
	c.execute(query)
	conn.commit()
	#Do what is needed to get results to UI
	#TODO Figure out what UI needs to make use of results
	#for no print for testing
	
	#close connection
	conn.close()
	return
	
def db_delete_assignments(where):
	#connect to DB
	conn = sqlite3.connect('../db.sqlite3')
	c = conn.cursor()
	query = "delete from tables_assignments where " + where
	#call stored Procedure
	c.execute(query)
	conn.commit()
	#Do what is needed to get results to UI
	#TODO Figure out what UI needs to make use of results
	#for no print for testing
	
	#close connection
	conn.close()
	return
