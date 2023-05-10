resource "google_service_account" "demo-sa" {
project = var.project_id
account_id = var.serviceAccount
}

resource "google_project_iam_member" "demo-sa-roles" {
  for_each = toset(var.roles_demo_sa)

  project = var.project_id
  role = each.value
  member = "serviceAccount:${google_service_account.demo-sa.email}"
}