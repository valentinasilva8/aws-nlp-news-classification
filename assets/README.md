# Screenshots Documentation

This folder contains visual evidence of the AWS NLP project implementation.

## Screenshots

### 1. api-gateway-postman-test.png
**Content**: Postman API testing interface showing successful POST request to `/dev/invoke-model` endpoint with query "Life in Mars might be a real possibility" and response showing predicted label "Science" with probabilities

### 2. training-validation-metrics-log-events.png  
**Content**: CloudWatch log events showing validation loss and validation accuracy per epoch (~96% accuracy, ~0.118 loss) from the SageMaker training job

### 3. lambda-invoke-logs.png
**Content**: CloudWatch logs for Lambda endpoint invoke function showing execution details, cold start, and performance metrics

### 4. s3-model-artifact-bucket.png
**Content**: S3 bucket containing the `model.tar.gz` file (235.7 MB) - the packaged model artifact from the training job

### 5. architecture.png
**Content**: System architecture diagram showing the flow from client through API Gateway, Lambda, and SageMaker endpoint.

## Usage
These screenshots are referenced in the main README.md to provide visual proof of the project implementation, including AWS services configuration, training results, and API testing.
