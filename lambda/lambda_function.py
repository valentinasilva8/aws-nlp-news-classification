import json
import boto3

def lambda_handler(event, context):

    sagemaker_runtime = boto3.client('sagemaker_runtime')

    body = json.loads(event.get('body', '{}'))
    # Accept either {"query": "text"} or {"query": {"headline": "text"}}
    query = body.get('query')
    if isinstance(query, dict):
        headline = query.get('headline')
    else:
        headline = query
    if not headline:
        return {"statusCode": 400, "body": json.dumps({"error": "Missing 'query' in body"})}

    #headline = "How I met your Mother voted as best sitcom in Europe"

    endpoint_name = os.environ.get('ENDPOINT_NAME', 'your-endpoint-name')

    payload = json.dumps({"inputs": headline})

    response = sagemaker_runtime.invoke_endpoint(
        EndpointName = endpoint_name, 
        ContentType = "application/json",
        Body = payload
        )
    result = json.loads(response['Body'].read().decode())

    return {

        'statusCode':200,
        'body': json.dumps(result)
    }