from faker import Faker
import pyodbc

#server = 'tcp:myserver.database.windows.net' 
server='localhost'
database = 'unicodb'
username = 'sa'
password = '1@Welcome1'

# Connect to the database.
conn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';Encrypt=yes;TrustServerCertificate=yes;UID='+username+';PWD='+ password)

# Create the table.
cursor = conn.cursor()
cursor.execute('''
IF EXISTS (SELECT * FROM sys.views WHERE object_id = OBJECT_ID(N'[dbo].[franquia_venda_produto]'))
EXEC sp_executesql N'DROP TABLE franquia_venda_produto'
CREATE OR ALTER TABLE franquia_venda_produto (
    codigo_filial CHAR(50) NOT NULL,
    ticket VARCHAR(50) NOT NULL,
    data DATE NOT NULL,
    produto VARCHAR(13) NOT NULL,
    qtde INT NULL,
    valor_bruto_itens MONEY NULL,
    desconto_prod MONEY NULL,
    valor_liquido_itens MONEY NULL,
    qtde_troca INT NULL,
    valor_bruto_itens_troca MONEY NULL,
    desconto_troca MONEY NULL,
    valor_liquido_itens_troca MONEY NULL
)
''')

# Generate 1GB of fake data.
faker = Faker()
for i in range(100):
    cursor.execute('INSERT INTO franquia_venda_produto (codigo_filial,ticket,data,produto,qtde,valor_bruto_itens,desconto_prod,valor_liquido_itens,qtde_troca,valor_bruto_itens_troca,desconto_troca,valor_liquido_itens_troca) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)',
    (faker.word(), faker.word(),faker.date(), faker.word(), faker.pyint(), faker.pricetag(), faker.pricetag(), faker.pricetag(), faker.pyint(), faker.pricetag(), faker.pricetag(), faker.pricetag()))


# Commit the changes.
conn.commit()

# Close the connection.
conn.close()