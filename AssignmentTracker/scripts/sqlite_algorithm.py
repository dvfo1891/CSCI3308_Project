import sys
import sqlite3
import time
from sqlite_call import *
from json import *
import datetime
import parser
# start of the algorithm. Takes tables and returns final JSON readable courselist 
def algorithm(user_id):
	# waiting on sqlite_call to work. Can't test otherwise
	conn = sqlite3.connect('../db.sqlite3')
	c = conn.cursor()
	# does what the code below does but doesn't break everything
	c.execute( 'select assignment, difficulty, end from tables_assignments where course_id in ( select course_id from tables_course_users where user_id=%d ) order by end, difficulty' % (user_id))
	# old code: here to explain what happens above
	#c.execute('SELECT * FROM tables_course WHERE username_id=?', user_id)
	#user_courses = c.fetchall()
	#conn.close()
	#conn = sqlite3.connect('../db.sqlite3')
	#c = conn.cursor()
	#query = "select * from tables_course, tables_assignments where tables_course.id =tables_assignments.course_id"
	#c.execute(query)
	#assignment_list = c.fetchall()
	#conn.close()
	#conn = sqlite3.connect('../db.sqlite3')
	#c = conn.cursor()

	#query = "select assignment, difficulty, end from assignment_list order by end, difficulty"

	##call stored Procedure
	#c.execute(query)
	r = c.fetchall()
	conn.close()
	# run the scheduler
	finished_plan = scheduler(r)
	# return json readable file 
	return(JSONEncoder().encode(finished_plan))
def scheduler(courses):
	order = 0
	place = 0
	for rows in courses:
		# sets order to the first item in the table
		if order == 0:
			order = rows
			place = place +1 
		# Projects take priority over all other assignments, followed by papers
		# Will overwrite end date base don assignment up to a point.  
		else:
			if('project' in rows[0].lower()):
				temp =0
				added = False
				for objects in order:
					if(added):
						temp = temp + objects
					else:
						if 'project' in objects[0].lower():
							temp = temp + objects
						else:
							if(objects[1] > rows[1]):
								continue;
							else:
								if(date_func(objects[2], rows[2])):
									temp = temp + rows
									added = True
				order = temp
				place = place +1
			elif('paper' in rows[0].lower()):
				temp =0
				added = False
				for objects in order:
					if(added):
						temp = temp + objects
					else:
						if 'project' in objects[0].lower():
							temp = temp + objects
						elif 'paper' in objects[0].lower():
							temp = temp + objects
						else:
							if(objects[1] > rows[1]):
								continue;
							else:
								if(date_func(objects[2], rows[2])):
									temp = temp + rows
									added = True
				if(added):
					order = temp
				else:
					order = temp + rows
				place = place + 1
			else: 
				order = order + rows
	return order
				
			
def date_func(date1, date2):
	# checks dates to see if they are an acceptable amount together to override end date.
	date_a = parse(date1, fuzzy) 				
	date_b = parse(date2, fuzzy)
	if(date_b.month - date_a.month > 2):
		return True
	if(date_b.day - date_a.month > 5):
		return True
	return False	
	
									
		
	
