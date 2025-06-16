# Self-Healing Jenkins Pipeline using AWS Bedrock

## Overview
This repo demonstrates how to create a Jenkins pipeline that uses AWS Bedrock (via Lambda + API Gateway) to:
- Analyze failed Jenkins job logs using LLM
- Identify the root cause
- Suggest healing actions
- Retry job automatically if recoverable

## Setup Steps

### 1. Deploy Lambda
- Use `lambda/app.py`
- Add permissions to access Bedrock

### 2. Create API Gateway
- Import `api_gateway/openapi.yaml`
- Connect to Lambda

### 3. Configure Jenkins Pipeline
- Use `jenkins/Jenkinsfile`
- Update API URL

### 4. Add `retry_decision.groovy`

## Notes
- Bedrock models (e.g. Claude, Mistral) provide flexible log analysis
- You can extend retry logic using more sophisticated conditions
