# below variables should be changed if there's a conflict with your existing environment
region = "us-central1"
zone = "us-central1-c"
network_name = "vpc-demo-debezium"
subnetwork = "us-central1"
ip_cidr_range = "192.168.72.0/24"
serviceAccount = "sa-debezium-demo"
router = "routerdemo-1"
nat = "natdemo-1"
bq_dataset = "dataset_demo_debezium"
bq_table = "from_postgresql"

roles_demo_sa = [
    "roles/bigquery.dataEditor",
    "roles/bigquery.metadataViewer",
    "roles/pubsub.admin"
    ]


services_list = [
    "compute.googleapis.com",
    "pubsub.googleapis.com",
    "bigquery.googleapis.com",
    "iam.googleapis.com",
    "cloudresourcemanager.googleapis.com"
  ]