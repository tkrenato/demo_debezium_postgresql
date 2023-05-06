import psycopg2
from faker import Faker

# Create a connection to the PostgreSQL database
conn = psycopg2.connect("host=localhost dbname=sampledb user=postgres password=mypassword")

# Create a cursor object
cur = conn.cursor()

# Create the `sampletable1` table
cur.execute("CREATE TABLE sampletable1 (id INT, name VARCHAR(255), email VARCHAR(255), lastupdate TIMESTAMP)")

# Generate 1GB of data inside the `sampletable1` table
fake = Faker()
for i in range(10000000):
    cur.execute("INSERT INTO sampletable1 (id, name, email, lastupdate) VALUES (%s, %s, %s, %s)", (i, fake.name(), fake.email(), fake.date_time()))

# Commit the changes to the database
conn.commit()

# Close the connection to the PostgreSQL database
conn.close()
