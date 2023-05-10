resource "google_compute_instance" "default" {
  name = "postgresql-linux"
  machine_type = "e2-small"
  zone = var.zone
  deletion_protection = false
  labels = {
    env = "demosql1"
  }
  
  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
      }
    }

  network_interface {
    network = var.network_name
    subnetwork = var.subnetwork
  }

  tags = ["allow-ssh"]

  shielded_instance_config {
    enable_secure_boot = true
    enable_vtpm = true
    enable_integrity_monitoring = true
  }
  metadata = {
    "dbpassword" = var.dbpassword
  }
  metadata_startup_script = file("${path.module}/files/install_postgresql.sh")

  depends_on = [
    google_compute_subnetwork.subnet-demo
  ]
}