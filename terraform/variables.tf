# -----------------------
# Variables
# -----------------------

variable "aws_region" {
  type        = string
  default     = "us-east-1"
}

variable "app_name" {
  type        = string
  default     = "calculator-app"
}

variable "env_name" {
  type        = string
  default     = "calculator-env"
}

variable "ecr_repo_name" {
  type        = string
  default     = "calculator"
}

variable "ecr_image" {
  type        = string
  description     = "Full ECR image URI with tag (set by Jenkins)"
  default     = "placeholder" 
}

variable "eb_platform_arn" {
  type    = string
  default = "64bit Amazon Linux 2023 v4.7.1 running Docker"
}
