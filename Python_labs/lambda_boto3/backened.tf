terraform {
  backend "s3" {
    bucket         = "talent-academy-monika-lab-tfstates"
    key            = "talent-academy/lambda_boto3/terraform.tfstates"
    dynamodb_table = "terraform-lock"
    region = "eu-west-1"
  }
}