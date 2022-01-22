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