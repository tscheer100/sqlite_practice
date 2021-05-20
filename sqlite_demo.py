# sqlite3 is a standard library withing python, so no need to pip.
import sqlite3
from employee import Employee

conn = sqlite3.connect('employees.db')

c = conn.cursor()

# c.execute("""
# CREATE TABLE employees (
#     first text,
#     last text,
#     pay integer
# )
#  """)
 # datatypes can bee found here: https://www.sqlite.org/datatype3.html

emp_1 = Employee('John', 'Doe', 80000)
emp_2 = Employee('Jane', 'Doe', 90000)

# print(emp_1.first)
# print(emp_1.last)
# print(emp_1.pay)

# c.execute("INSERT INTO eemployees VALUES ('{}', '{}', {})".format(emp_1.first, emp_1.last, emp_1.pay)) # string formatting is bad practice in DBs | vulnerable to SQL injecctions
# c.execute("INSERT INTO employees VALUES (?, ?, ?)", (emp_1.first, emp_1.last, emp_1.pay) ) # do this instead
# conn.commit()

# # # but you can 1up the previous format using a dictionary
# c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': emp_2.first, 'last': emp_2.last, 'pay': emp_2.pay})

# c.execute("INSERT INTO employees VALUES ('Thomas', 'Scheer', 50000)")
# c.execute("INSERT INTO employees VALUES ('Diana', 'Scheer', 70000)")
# conn.commit()

c.execute("SELECT * FROM employees WHERE last='Scheer'") # bad practice

print(c.fetchall())

c.execute("SELECT * FROM employees WHERE last=:last", {'last': 'Doe'}) 

print(c.fetchall())

conn.commit()

conn.close()