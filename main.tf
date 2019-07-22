provider "aws" {
  profile = "${terraform.workspace}"
  region  = "${var.region}"
  version = "~> 2.8"
}

locals {
  env = "${terraform.workspace}"
}

resource "aws_iam_role" "role-for-lambda" {
  name = "role-for-lambda-${local.env}"
  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF
}

resource "aws_iam_role_policy" "policy-for-lambda" {
  name = "policy-for-lambda-${local.env}"
  role = "${aws_iam_role.role-for-lambda.id}"
  policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "lambda:InvokeFunction"
      ],
      "Resource": [
        "${aws_lambda_function.lambda-function-for-get-games.arn}"
      ]
    }
  ]
}
EOF
}

resource "aws_lambda_function" "lambda-function-for-get-games" {
  function_name = "lambda-function-for-get-games-${local.env}"
  handler = "${var.lambda_handler}"
  runtime = "${var.lambda_runtime}"
  timeout = "${var.lambda_timeout}"
  filename = "sources/lambda-functions/get-games-for-platform/dist/lambda.zip"
  source_code_hash = "${filebase64sha256("sources/lambda-functions/get-games-for-platform/dist/lambda.zip")}"
  role = "${aws_iam_role.role-for-lambda.arn}"
  layers = [
    "${aws_lambda_layer_version.lambda-layer-for-classes.arn}",
  ]
}

resource "aws_lambda_function" "lambda-function-for-get-programming-joke" {
  function_name = "lambda-function-for-get-programming-joke-${local.env}"
  handler = "${var.lambda_handler}"
  runtime = "${var.lambda_runtime}"
  timeout = "${var.lambda_timeout}"
  filename = "sources/lambda-functions/get-programming-joke/dist/lambda.zip"
  source_code_hash = "${filebase64sha256("sources/lambda-functions/get-programming-joke/dist/lambda.zip")}"
  role = "${aws_iam_role.role-for-lambda.arn}"
  layers = [
    "${aws_lambda_layer_version.lambda-layer-for-classes.arn}",
  ]
}

resource "aws_lambda_layer_version" "lambda-layer-for-classes" {
  filename = "sources/lambda-layers/abstract-layer/dist/lambda.zip"
  layer_name = "lambda-layer-for-classes-${local.env}"
  compatible_runtimes = ["${var.lambda_runtime}"]
  source_code_hash = "${filebase64sha256("sources/lambda-layers/abstract-layer/dist/lambda.zip")}"
}