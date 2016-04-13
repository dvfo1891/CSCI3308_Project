import sys
import sqlite3
import time
import sqlite_call.py
import json
import dateutil.parser as dparser
import date

def algorithm(user):
	user_courses = db_select(course, 'where  username = user')
	assignment_list = db_select('user_courses, assignments', 'where user_courses.course =assignment.course')
	conn = sqlite3.connect('../db.sqlite3')
	c = conn.cursor()

	query = "select assignment, difficulty, end from assignment_list order by end, difficulty"

	#call stored Procedure
	c.execute(query)
	r = c.fetchall()
	conn.close()
	finished_plan = scheduler(r)
	return(JSONEncoder().encoder(finished_plan))
def scheduler(courses):
	order = 0
	place = 0
	for rows in courses:
		# sets order to the first item in the table
		if order == 0:
			order = row
			place = place +1 
		# Projects take priority over all other assignments, followed by papers
		# Will overwrite end date base don assignment up to a point.  
		else:
			if('project' in rows[0]):
				temp =0
				added = False
				for objects in order:
					if(added):
						temp = temp + objects
					else:
						if 'project' in objects[0]:
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
			elif('paper' in rows[0]):
				temp =0
				added = False
				for objects in order:
					if(added):
						temp = temp + objects
					else:
						if 'project' in objects[0]:
							temp = temp + objects
						elif 'paper' in objects[0]:
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
				
			
def date_func(date1, date2):
	# checks dates to see if they are an acceptable amount together to override end date.
	date_a = dparser.parse(date1, fuzzy = true) 				
	date_b = dparser.parse(date2, fuzzy = true)
	if(date_b.month - date_a.month > 2):
		return True
	if(date_b.day - date_a.month > 5):
		return True
	return False	
	
									
		
	
