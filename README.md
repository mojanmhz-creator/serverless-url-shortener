# Serverless URL Shortener

A project to learn AWS fundamentals, built toward a Terraform and CI/CD deployment.

## Week 1: what I built (by hand in the console)
- **Lambda function** (Python): looks up a short code and returns the URL
- **DynamoDB table** (`links-test`): stores code and URL pairs
- **IAM role** (`hello-test-role`): least privilege, allows only `GetItem` on one table

## What I learned
- Each Lambda should get its own role with only the permissions it needs
- I tested least privilege by trying a `Scan`, which AWS denied
- My account only allows us-east-2, because an organization policy denies other regions
- The AWS CLI works the same in any shell, but the shell syntax around it differs

## Next
- Rebuild everything in Terraform
- Add API Gateway, a frontend, and a CI/CD pipeline