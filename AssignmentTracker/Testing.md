Who: Cameron Thompson, Jiahao Cao, DVreaux Fontaine, Ben Droste, Gengyu Liu

Title: Online Homework Tracker

Vison Statement: To provide a centralized location for college student to keep track of upcomming online assignments.

Automated Tests:
Python Database calls

how to run
./sqlite_call_test.py

what it tests
Inserting into table
Selecting from Table
Deleting from table

Test Results
...
----------------------------------------------------------------------
Ran 3 tests in 0.142s

OK


------------------
(program exited with code: 0)
Press return to continue


_____
UAT

Use Case ID = UC-01

Use Case Name = Python Database calls

Description = Python call that can insert, select, delete items from sqlite database

Users = Developers

Preconditions = 

Postconditions = 

Frequency of Use = Every time we need to access the database

Test Pass = Pass /Fail

Notes = 


_________
Use Case ID = UC-02

Use Case Name = No duplicate users

Description = When signing up it should prevent duplications of usernames and redirect to signup_error.html

User = Developers

Preconditions =

Postconditions =

Frequency of Use = Every time a new user joins

Test Pass = Pass /Fail

Notes =

Use Case ID = UC-03
Use Case Name = Plan based on algorithm.
Description = After loading all classes into the database, the user should be able to plan their homework scheduele based on the information provided back
User = User
Preconditions = Classes must be loaded into the database along with the information needed to run the algorithm. 
Postconditions = An output that gives a scheduele based on the information passe din. 
Frequency of Use = Everytime a new assignment is added 
Flow of Events: 
User clicks on a button that allows them to add an assignment 
Once all the information is added, it is added to a database
The information is then pulled and used with the other assignment data to maximize the algorithms. 
The final scheduele is displayed on the screen, where the user can decide what to do with it. 
Test Pass = Displays assignments with priorities 
Notes = 


