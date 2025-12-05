import sqlite3

# Connect to the database
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Execute a query to fetch all rows from the students table
cursor.execute("SELECT * FROM students")

# Fetch and print the results
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close the connection
conn.close()
