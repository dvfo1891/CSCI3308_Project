import sqlite_algorithm
import sqlite_call
import sqlite3
def main():
	conn = sqlite3.connect('../db.sqlite3')
	c = conn.cursor()
	print (sqlite_algorithm.algorithm(1))

main()
