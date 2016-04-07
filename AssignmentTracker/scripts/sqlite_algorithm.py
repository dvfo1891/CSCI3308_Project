import sys
import sqlite3
import time
import sqlite_call.py

def algorithm(user):
        user_courses = db_select(course, where  username = user)
        assignment_list = db_select('user_courses, assignments', where user_courses.course =assignment.course
        conn = sqlite3.connect('../db.sqlite3')
        c = conn.cursor()

        query = "select difficulty, end from assignment_list order by end, difficulty"

        #call stored Procedure
        c.execute(query)
        r = c.fetchall()
        conn.close()
        return(r)
