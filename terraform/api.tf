resource "google_project_service" "enable_apis" {
  project = var.project_id
  for_each = toset(var.services_list)
  service = each.key
  disable_on_destroy = false
}