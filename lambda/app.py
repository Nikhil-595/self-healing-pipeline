import json
import boto3

bedrock = boto3.client('bedrock-runtime', region_name='us-east-1')

def lambda_handler(event, context):
    log_text = event.get('log', '')
    prompt = f"""You are a Jenkins pipeline assistant. Analyze the following Jenkins job log and answer:
1. What is the failure reason?
2. What healing action can be taken?
Log:
{log_text}"""

    response = bedrock.invoke_model(
        modelId="anthropic.claude-3-sonnet-20240229-v1:0",
        contentType="application/json",
        accept="application/json",
        body=json.dumps({
            "prompt": prompt,
            "max_tokens_to_sample": 300,
            "temperature": 0.5
        })
    )

    result = json.loads(response['body'].read())
    return {
        'statusCode': 200,
        'analysis': result['completion']
    }
