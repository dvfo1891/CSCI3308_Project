import sqlite_algorithm
import sqlite_call
import sqlite3
#this is a testing file for sqlite_algorithm.py - the formal scheduler
def main():
	conn = sqlite3.connect('../db.sqlite3')
	c = conn.cursor()
	print (sqlite_algorithm.algorithm(1))

main()
