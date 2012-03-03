Pathon and Mysql sample
=================================

The aim of this sample is to demostrate a interactive command line interface written with Python to talk with Mysql DB.

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
2. python 
3. gzip -cd custom-karaf-1.0-SNAPSHOT-bin.tar.gz | tar -xvf -
4. cd custom-karaf-1.0-SNAPSHOT
5. bin/karaf
6. in console: features:install icarus-springmvc-webapp
7. the URL http://localhost:8181/spring-mvc-client should display the home page

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