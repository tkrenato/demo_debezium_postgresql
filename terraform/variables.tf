variable "project_id"{
    description = "GCP Project ID"
}

variable "region" {
  type        = string
  description = "GCP region"
}

variable "zone" {
  type        = string
  description = "GCP Zone"
}

variable "services_list" {
    type = list(string)
    description = "list of services to be enabled for the project"
    default = []
}

variable "network_name" {
  type = string
  description = "VPC name"
}

variable "subnetwork" {
    type = string
    description = "subnet"
}

variable "ip_cidr_range" {
  type = string
  description = "CIDR to be used in the VPC / Subnet"
}

variable "serviceAccount" {
  type = string
  description = "Service account for Debezium demo"
}

variable "roles_demo_sa" {
    type = list(string)
    description = "Roles for the service account used on the Debezium Demo"
    default = []
}

# since argolis does not allows external ip, we need to create a NAT GW
variable "router" {
    type = string
    description = "Router for Cloud NAT"
}

variable "nat" {
    type = string
    description = "Cloud NAT"
}

variable "bq_dataset" {
    type = string
    description = "BigQuery Dataset name"
}

variable "bq_table" {
    type = string
    description = "BigQuery table name"
}

variable "dbpassword" {
  type = string
  description = "password for source database"
}