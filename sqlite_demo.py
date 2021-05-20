# sqlite3 is a standard library withing python, so no need to pip.
import sqlite3

conn = sqlite3.connect('employee.db')

c = conn.cursor()

# c.execute("""
# CREATE TABLE employees (
#     first text,
#     last text,
#     pay integer
# )
#  """)
 # datatypes can bee found here: https://www.sqlite.org/datatype3.html

# c.execute("INSERT INTO employees VALUES ('Thomas', 'Scheer', 50000)")
# c.execute("INSERT INTO employees VALUES ('Diana', 'Scheer', 70000)")
# conn.commit()

c.execute("SELECT * FROM employees WHERE last='Scheer'")

print(c.fetchall())

conn.commit()

conn.close()