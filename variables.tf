variable "lambda_handler" {
  default = "lambda.lambda_handler"
}

variable "lambda_runtime" {
  default = "python3.7"
}

variable "lambda_timeout" {
  default = "900"
}

variable "region" {
  default = "us-west-1"
}