import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from faker import Faker

# Connect to the PostgreSQL server as the default postgres user
conn = psycopg2.connect("host=localhost user=postgres password=welcome1")

# Set the isolation level to autocommit to allow database creation
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

# Create a cursor object
cur = conn.cursor()

# Check if the `sampledb` database exists
cur.execute("SELECT datname FROM pg_catalog.pg_database WHERE datname='sampledb'")
exists = cur.fetchone()

if not exists:
    # Create the `sampledb` database
    cur.execute("CREATE DATABASE sampledb")

# Close the cursor and connection to the PostgreSQL server
cur.close()
conn.close()

# Connect to the `sampledb` database
conn = psycopg2.connect(
    host="localhost",
    database="sampledb",
    user="postgres",
    password="welcome1"
    )

# Create a cursor object
cur = conn.cursor()

# Create the `sampletable1` table
create_table = """
    CREATE TABLE sampletable1 (
        id INT,
        name VARCHAR(255),
        email VARCHAR(255),
        lastupdate TIMESTAMP
    )
"""
cur.execute(create_table)

# Generate 1GB of data inside the `sampletable1` table
fake = Faker()
for i in range(1000):
    cur.execute("INSERT INTO sampletable1 (id, name, email, lastupdate) VALUES (%s, %s, %s, %s)", (i, fake.name(), fake.email(), fake.date_time()))

# Commit the changes to the database
conn.commit()

# Close the connection to the PostgreSQL database
conn.close()
