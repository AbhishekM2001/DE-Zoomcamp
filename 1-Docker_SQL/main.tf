

terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "6.18.1"

    }
  }
}

provider "google" {
  project = "indigo-tracker-449618-c7"
  region  = "asia-south1"
}


resource "google_storage_bucket" "terraform-demo-bucket" {
  name          = "indigo-tracker-449618-c7-terraform-demo-bucket"
  location      = "US"
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}
