import sqlite3
old = ["f0000e","28","11","2025","PM","12:15"]
conn = sqlite3.connect('Mincrete.db')
cursor = conn.cursor()
cursor = conn.execute(
    "SELECT * FROM order_details WHERE custID =? and day =? and month =? and year =? and AMPM =? and time =?",
    (old[0], old[1], old[2], old[3], old[5], old[4]))
results = cursor.fetchone()
print(results)



cursor = conn.cursor()
cursor = conn.execute("SELECT * FROM order_details")
p = cursor.fetchall()
print(p)