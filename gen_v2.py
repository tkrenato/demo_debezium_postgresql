import faker
import pyodbc

# Connect to the database
connection = pyodbc.connect('Driver={SQL Server};Server=localhost;Database=unicodb;Trusted_Connection=yes;')
cursor = connection.cursor()

# Generate fake data for the table
column_names = ['id_branch', 'ticket', 'date', 'product', 'quantity', 'gross_amount', 'discount', 'net_amount', 'quantity_exchange', 'valor_bruto_itens_troca', 'desconto_troca', 'valor_liquido_itens_troca']
data = [tuple(faker.generate(*column_names)) for i in range(100)]

# Insert the data into the table
insert_statement = 'INSERT INTO franchise_sales_product ({}) VALUES ({});'.format(', '.join(column_names), ', '.join('?' * len(column_names)))
cursor.executemany(insert_statement, data)

# Commit the changes
connection.commit()

# Close the connection
cursor.close()
connection.close()