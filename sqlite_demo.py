# sqlite3 is a standard library withing python, so no need to pip.
import sqlite3

conn = sqlite3.connect('employee.db')

c = conn.cursor()

c.execute("""
CREATE TABLE employyes (
    first text,
    last text,
    pay integer
)
 """)
 # datatypes can bee found here: https://www.sqlite.org/datatype3.html

conn.commit()

conn.close()