# -----------------------
# Outputs
# -----------------------

output "eb_environment_url" {
  description = "Public URL of the Elastic Beanstalk environment"
  value       = "http://${aws_elastic_beanstalk_environment.env.cname}"
}

output "eb_environment_name" {
  description = "Name of the Elastic Beanstalk environment"
  value       = aws_elastic_beanstalk_environment.env.name
}

output "eb_environment_id" {
  description = "ID of the Elastic Beanstalk environment"
  value       = aws_elastic_beanstalk_environment.env.id
}

output "eb_application_name" {
  description = "Name of the Elastic Beanstalk application"
  value       = aws_elastic_beanstalk_application.app.name
}


output "ecr_repository_url" {
  description = "ECR repository URL (use this to build & push Docker images)"
  value       = aws_ecr_repository.calculator.repository_url
}

output "ecr_repository_arn" {
  description = "ARN of the ECR repository"
  value       = aws_ecr_repository.calculator.arn
}

output "eb_instance_profile_name" {
  description = "IAM instance profile attached to EB EC2 instances"
  value       = aws_iam_instance_profile.eb_instance_profile.name
}

output "eb_service_role_arn" {
  description = "IAM service role ARN used by Elastic Beanstalk"
  value       = aws_iam_role.eb_service_role.arn
}
