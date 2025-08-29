## API Specification

- Method: POST
- Path: /dev/invoke-model
- Auth: API Gateway default (configure as needed)
- Content-Type: application/json

### Request Body
`json
{ "query": "Life in Mars might be a real possibility" }
`

### Response
`json
{\n  "predicted_label": "Science",\n  "probabilities": [0.02, 0.94, 0.02, 0.02]\n}
`

### Notes
- Backed by AWS Lambda that forwards to a SageMaker endpoint using boto3 sagemaker-runtime.invoke_endpoint.
- Average p95 latency observed in Postman: ~1.5s (cold starts may be higher).
