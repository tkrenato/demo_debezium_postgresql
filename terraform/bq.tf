resource "google_bigquery_dataset" "dataset1" {
  dataset_id = var.bq_dataset
  description = "Dataset used for debezium demo"
  location = var.region
  delete_contents_on_destroy = true
  depends_on = [
    google_compute_subnetwork.subnet-demo
  ]
}

resource "google_bigquery_table" "table1" {
  dataset_id = google_bigquery_dataset.dataset1.dataset_id
  table_id = var.bq_table
  deletion_protection = false
  depends_on = [
    google_compute_subnetwork.subnet-demo
  ]

  schema = <<EOF
    [
      {
        "name": "id",
        "type": "INT64"
      },
      {
        "name": "name",
        "type": "STRING"
      },
      {
        "name": "email",
        "type": "STRING"
      },
      {
        "name": "lastupdate",
        "type": "TIMESTAMP"
      }
    ]
  EOF
}
