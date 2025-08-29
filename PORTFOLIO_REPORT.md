# News Headline Classification on AWS (Portfolio Summary)

## Goal
Build a production-ready NLP system that classifies news headlines into four topics (Business, Science, Entertainment, Health).

## Model
DistilBERT fine-tuned on a headlines dataset with PyTorch + Hugging Face Transformers.

## AWS Pipeline
- SageMaker Training Job: trains DistilBERT, saves model artifacts to S3.
- SageMaker Endpoint: real-time inference endpoint from model tarball and `src/inference.py`.
- AWS Lambda: lightweight HTTP handler that forwards to the SageMaker endpoint.
- API Gateway: exposes a single REST route `POST /dev/invoke-model`.

## Results
- Validation accuracy ≈96%; validation loss ≈0.118 (CloudWatch logs).
- Postman test returns 200 OK with ~1.5s latency for typical requests.

## Proof (Screenshots)
- CloudWatch training logs with metrics.
- SageMaker Studio job creation & endpoint deployment.
- Postman request/response for the API.

## Example Request
```json
{ "query": "Life in Mars might be a real possibility" }
```

## Example Response
```json
{ "predicted_label": "Science", "probabilities": [0.02, 0.94, 0.02, 0.02] }
```

## Future Improvements
- **Content Analysis Expansion**: Extend beyond headlines to analyze full news articles, enabling deeper content understanding and more accurate classification based on complete context rather than just titles.
- Orchestrate with SageMaker Pipelines (automated train-eval-deploy).
- Async inference for bursty traffic; provisioned concurrency for Lambda.
- Monitoring dashboards (CloudWatch/QuickSight) with latency, accuracy, drift.
