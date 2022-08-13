# --- boto3_python_projects/trigger_api_lambda_sqs/create_sqs_queue.py ---

# Create a Standard SQS Queue using Python


# AWS Python SDK
import boto3


# A low-level client representing Amazon Elastic Compute Cloud (SQS)
sqs_client=boto3.client("sqs")


# use Amazon service sqs
sqs_resource = boto3.resource('sqs')


# Queue will be created 
sqs_queue = sqs_resource.create_queue(QueueName='time_queue')



# prints the output - Standard Queue url
print('Standard Queue created. Queue URL: ' + sqs_queue.url)
