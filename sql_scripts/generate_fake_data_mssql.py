import pyodbc
import faker

# Create a connection string
conn_str = (
    "Driver={SQL Server Native Client 11.0};"
    "Server=localhost;"
    "Database=sampledb1;"
    "Trusted_Connection=yes;"
)

# Create a connection object
conn = pyodbc.connect(conn_str)

# Create a cursor object
cur = conn.cursor()

# Create a database
cur.execute("CREATE DATABASE sampledb1")

# Create a table
cur.execute(
    """
    CREATE TABLE users (
        id INT IDENTITY(1,1) PRIMARY KEY,
        name VARCHAR(255),
        email VARCHAR(255),
        lastupdate TIMESTAMP
    )
    """
)

# Generate 1GB of fake data
fake = faker.Faker()
for i in range(1000000):
    cur.execute(
        """
        INSERT INTO users (name, email, lastupdate)
        VALUES (?, ?, GETDATE())
        """,
        (fake.name(), fake.email(),),
    )

# Commit the changes
conn.commit()

# Close the connection
conn.close()
