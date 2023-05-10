resource "google_compute_network" "vpc_demo" {
  name = var.network_name
  auto_create_subnetworks = false
}

resource "google_compute_subnetwork" "subnet-demo" {
  name          = var.subnetwork
  ip_cidr_range = var.ip_cidr_range
  region        = var.region
  network       = google_compute_network.vpc_demo.id
  private_ip_google_access = true
}

resource "google_compute_router" "router1" {
  name    = var.router
  region  = google_compute_subnetwork.subnet-demo.region
  network = google_compute_network.vpc_demo.name

  bgp {
    asn = 64514
  }
}

resource "google_compute_router_nat" "nat" {
  name                               = var.nat
  router                             = google_compute_router.router1.name
  region                             = google_compute_router.router1.region
  nat_ip_allocate_option             = "AUTO_ONLY"
  source_subnetwork_ip_ranges_to_nat = "ALL_SUBNETWORKS_ALL_IP_RANGES"

  log_config {
    enable = true
    filter = "ERRORS_ONLY"
  }
}