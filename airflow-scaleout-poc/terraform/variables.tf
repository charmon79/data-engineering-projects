### locals
locals {
  azs = {
    a = "${var.aws_region}a"
    b = "${var.aws_region}b"
    c = "${var.aws_region}c"
  }
}

### variables
variable "aws_auth" {
  type = object(
    {
      access_key = string
      secret_key = string
    }
  )
}

variable "aws_region" {
  type = string
}

variable "default_tags" {
  type = object(
    {
      Environment = string
      Repo        = string
      ConfigBy    = string
      Purpose     = string
    }
  )
  default = {
    ConfigBy    = "TF"
    Repo        = "https://github.com/charmon79/data-engineering-projects"
    Environment = "sandbox"
    Purpose     = "Demonstrating a scale-out deployment of Apache Airflow"
  }
}

variable "allowed_internet_cidrs" {
  type = list(string)
}
