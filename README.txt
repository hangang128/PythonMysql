Python and Mysql sample
=================================

The aim of this sample is to demonstrate a command line application written in Python to talk with Mysql DB.

The data model is an employee-manager table which has hierarchical relationship among employees. 

The command is to query all employees, get all employees reporting to a specific manager, or get all the managers of an employee.

The table creation and data population is done by the program. Before its run, a mysql server and a database need to be created.


System Requirements
-------------------
* Python 3.2
* MySQLdb for Python
* MySQL server 5.5
* Pydev plugin with Eclipse3.6 (optional)

Directory Structure
-------------------

* PythonMysql\emp_mgr\src
  
  	Folder to run the program

* PythonMysql\emp_mgr
  
  	Folder to have eclipse project files


Running
-------
1. cd PythonMysql\emp_mgr\src

2. Setup mysql connection:
   Modify file EmployeeManager.py, line 16(host, user, password and database):
        con = mdb.connect('localhost', 'testuser', 'test623', 'testdb');

3. run cmd:
   python EmployeeManager.py


Sample Output
--------------
S:\dev\python\emp_mgr\src>python EmployeeManager.py

Manager and his/her reports:


All employees:
-----------------------------------
Id Name ManagerId ManagerName
-----------------------------------
(1, 'Jack', 0, '')
(2, 'Honore', 1, 'Jack')
(3, 'Lion', 1, 'Jack')
(4, 'Emile', 1, 'Jack')
(5, 'Truman', 3, 'Lion')
(6, 'Ted', 3, 'Lion')

 (A)llEmployee  List(R)eport  List(M)anager  (Q)uit [q]: r
Please enter manager name: Jack

Jack's reports:
-----------------------------------
Id Name ManagerId ManagerName Level
-----------------------------------
(2, 'Honore', 1, 'Jack', 1)
(3, 'Lion', 1, 'Jack', 1)
(5, 'Truman', 3, 'Lion', 2)
(6, 'Ted', 3, 'Lion', 2)
(4, 'Emile', 1, 'Jack', 1)

 (A)llEmployee  List(R)eport  List(M)anager  (Q)uit [q]: m
Please enter employee name: Ted

Ted's managers:
-----------------------------------
Id Name ManagerId ManagerName Level
-----------------------------------
(3, 'Lion', 1, 'Jack', 1)
(1, 'Jack', 0, '', 2)

 (A)llEmployee  List(R)eport  List(M)anager  (Q)uit [q]: a

All employees:
-----------------------------------
Id Name ManagerId ManagerName
-----------------------------------
(1, 'Jack', 0, '')
(2, 'Honore', 1, 'Jack')
(3, 'Lion', 1, 'Jack')
(4, 'Emile', 1, 'Jack')
(5, 'Truman', 3, 'Lion')
(6, 'Ted', 3, 'Lion')

 (A)llEmployee  List(R)eport  List(M)anager  (Q)uit [q]: q
quit application, bye!

S:\dev\python\emp_mgr\src>