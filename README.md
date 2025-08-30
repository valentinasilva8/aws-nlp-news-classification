# AWS NLP: News Headline Classification (SageMaker + Lambda + API Gateway)

## Highlights
- DistilBERT fine-tuned to classify news headlines into Business, Science, Entertainment, Health.
- End-to-end on AWS: SageMaker training -> real-time endpoint -> Lambda -> API Gateway.
- CloudWatch validation: ~96% accuracy, ~0.118 loss.
- Public REST API: single POST /dev/invoke-model.

## Architecture
![System Architecture](assets/architecture.png)

*Complete system flow from client through API Gateway, Lambda, and SageMaker endpoint*

## Tech Stack
- AWS: SageMaker, Lambda, API Gateway, CloudWatch, S3
- ML: PyTorch, Transformers (DistilBERT)
- Python: boto3, sagemaker SDK

## Repo Structure
```
.
├─ notebooks/
│  ├─ 01_train_eval.ipynb
│  ├─ 02_deploy_endpoint.ipynb
├─ src/
│  ├─ train.py
│  ├─ inference.py
├─ lambda/
│  └─ lambda_function.py
├─ api/
│  └─ api_spec.md
├─ assets/  (screenshots)
├─ experiments/
│  └─ load-test.py
├─ requirements.txt
├─ runtime-requirements.txt
├─ README.md
└─ .gitignore
```

## Setup
1. pip install -r requirements.txt
2. Upload training data to S3 and run notebooks/01_train_eval.ipynb or SageMaker job using src/train.py.
3. Deploy with notebooks/02_deploy_endpoint.ipynb to create a real-time endpoint.
4. Create Lambda using code in lambda/lambda_function.py and set env var ENDPOINT_NAME or edit inline.
5. Wire API Gateway to Lambda (proxy integration).

## Example Inference (API)
POST `/dev/invoke-model`

Body:
```json
{ "query": "Life in Mars might be a real possibility" }
```

Response:
```json
{ "predicted_label": "Science", "probabilities": [0.02, 0.94, 0.02, 0.02] }
```


## Lambda Snippet
```python
response = sagemaker_runtime.invoke_endpoint(
    EndpointName=os.environ.get('ENDPOINT_NAME'),
    ContentType='application/json',
    Body=json.dumps({"inputs": headline})
)
```

## Training Notes
- Epoch summary (CloudWatch): validation accuracy ~96.09%, validation loss ~0.118.
- Instance: ml.g4dn.xlarge; optimizer Adam, lr=1e-5, batch sizes 4/2.

## Screenshots
- **API Gateway & Postman Test**: `assets/api-gateway-postman-test.png` - Shows successful POST request to `/dev/invoke-model` with query and response showing predicted label "Science"
- **Training Validation Metrics**: `assets/training-validation-metrics-log-events.png` - CloudWatch logs showing validation accuracy (~96%) and loss (~0.118) per epoch
- **Lambda Invoke Logs**: `assets/lambda-invoke-logs.png` - CloudWatch logs for Lambda function execution and performance metrics
- **S3 Model Artifact**: `assets/s3-model-artifact-bucket.png` - S3 bucket containing the `model.tar.gz` file (235.7 MB) from training
- **System Architecture**: `assets/architecture.png` - Complete system flow diagram



## Requirements
- See requirements.txt and runtime-requirements.txt.

## Roadmap
- Automate with SageMaker Pipelines; async inference; add monitoring dashboards; batch transform for scale.
