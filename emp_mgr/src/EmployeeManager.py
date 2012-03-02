#!/usr/bin/env python3

import Console
import MySQLdb as mdb
import sys
import warnings


def main():
    functions = dict(a=all_employee, r=list_report, m=list_manager,
                     q=quit_app)
    con = None    
    
    try:
        # connect to hostName, userName, password, databaseName
        con = mdb.connect('localhost', 'testuser', 'test623', 'testdb');
        cur = con.cursor()
        initDB(con, cur);

        print("\nManager and his/her reports:\n")
        all_employee(cur)

        action = ""
        while True:
            print()
            menu = " (A)llEmployee  List(R)eport  List(M)anager  (Q)uit"
            action = Console.get_menu_choice(menu, "armq",
                                        "q", True)
            functions[action](cur)
    except mdb.Error as e:
        print("Error %d: %s", e.args[0], e.args[1])
        sys.exit(1)            
    finally:
        if con is not None:
            con.close()

def initDB(con, cur):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore") 
        cur.execute("DROP TABLE IF EXISTS Employee")
    cur.execute("CREATE TABLE IF NOT EXISTS \
        Employee(Id INT PRIMARY KEY, Name VARCHAR(25), ManagerId INT)")
    cur.execute("INSERT INTO Employee(Id, Name, ManagerId) VALUES(1, 'Jack', 0)")
    cur.execute("INSERT INTO Employee(Id, Name, ManagerId) VALUES(2, 'Honore', 1)")
    cur.execute("INSERT INTO Employee(Id, Name, ManagerId) VALUES(3, 'Lion', 1)")
    cur.execute("INSERT INTO Employee(Id, Name, ManagerId) VALUES(4, 'Emile', 1)")
    cur.execute("INSERT INTO Employee(Id, Name, ManagerId) VALUES(5, 'Truman', 3)")
    cur.execute("INSERT INTO Employee(Id, Name, ManagerId) VALUES(6, 'Ted', 3)")
    con.commit()                

def all_employee(cur):
    print("\nAll employees:")
    cur.execute('select a.*, IF(b.name IS NULL,"",b.name) as ManagerName \
     from employee a left join employee b on a.ManagerId = b.id')
    print_query_result(cur)  

def list_report(cur):
    manager_name = Console.get_string("Please enter manager name", "Manager Name")
    if not manager_name:
        return
    print("\n" + manager_name + "'s reports:")

    # In oracle, a query could be written like this:
    #    SELECT  LPAD(' ', level * 4, ' ') || name, managerid, level
    #    FROM    employee
    #    START WITH
    #            lower(name) = lower("Insert Manager's Name Here")
    #    CONNECT BY
    #            managerid = PRIOR id
    # in Mysql, it could be done with complex query or following python code
    # traverse manager's direct report
    # print_direct_report(manager, level)
    print_direct_report(cur, manager_name, 1)  
    
def list_manager(cur):
    employee_name = Console.get_string("Please enter employee name", "Employee Name")
    if not employee_name:
        return
    print("\n" + employee_name + "'s managers:")
    # In oracle, a query could be written like this:
    #    SELECT  LPAD(' ', level * 4, ' ') || name, CONNECT_BY_ROOT last_name "Manager", LEVEL-1
    #    FROM    employee
    #    START WITH
    #            lower(name) = lower("Insert Manager's Name Here")
    #    CONNECT BY
    #            managerid = PRIOR id
    # in Mysql, it could be done with complex query or with following python code
    # traverse manager's direct report
    print_manager(cur, employee_name, 1)  

def quit_app(cur):
    print("quit application, bye!")
    sys.exit()

def print_query_result(cur, print_header=True, print_rows=True):
    if print_header:
        print("-----------------------------------")
        desc = cur.description
        header = ""
        for label in desc:
            header += label[0] + " "
        
        print(header)
        print("-----------------------------------")

    if print_rows:
        rows = cur.fetchall()
        for row in rows:
            print(row)


def print_direct_report(cur, manager_name, level):
    
    # query direct report
    sql = "select a.*, b.name as ManagerName , " + str(level) + " as Level \
     from employee a, employee b where a.ManagerId = b.id and Lower(b.name)\
      = Lower('" + manager_name + "')"
    cur.execute(sql)
    
    # no direct report, exit condition for recursion
    if cur.rowcount < 1:
        return 
    
    if level == 1 :
        print_query_result(cur, True, False)
    
    rows = cur.fetchall()
    for row in rows:
        print(row)
        print_direct_report(cur, row[1], level + 1)
    

def print_manager(cur, employee_name, level):
    
    # query direct manager
    sql = 'select a.*, IF(b.name IS NULL,"",b.name) as ManagerName, ' \
    + str(level) \
    + ' as Level from employee a left join employee b on a.ManagerId = b.id' \
    + " where a.id in (select managerid from employee where lower(name)=lower('" \
    + employee_name + "') )"
    cur.execute(sql)
    
    # no direct manager, exit condition for recursion
    if cur.rowcount < 1:
        return 
    
    if level == 1 :
        print_query_result(cur, True, False)
    
    rows = cur.fetchall()
    for row in rows:
        print(row)
        print_manager(cur, row[1], level + 1)

main()
