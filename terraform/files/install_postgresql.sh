sudo apt update -y
sudo apt install -y postgresql
sudo apt install -y pip
sudo apt install -y wget

pip install faker
pip install psycopg2-binary

# retrieve the password for the database
DBPASSWORD=$(curl -H "Metadata-Flavor: Google" http://metadata.google.internal/computeMetadata/v1/instance/attributes/dbpassword)
sudo su - postgres -c "psql -c \"ALTER USER postgres PASSWORD '$DBPASSWORD';\""
sudo systemctl restart postgresql.service

wget https://raw.githubusercontent.com/tkrenato/demo_debezium_postgresql/main/postgresql_fake_data.py
python3 postgresql_fake_data.py