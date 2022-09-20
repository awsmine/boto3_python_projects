#!/usr/bin/env python3.7


# 8_scan_table_json.py
# scan the formatted table


# To use Boto3, you must first import AWS Python SDK
import boto3


#import json so scan returns in jason format 
import json  


# A low-level client representing DynamoDB
dynamodb = boto3.client('dynamodb')


# scan the table movies
response = dynamodb.scan(
    TableName='movies'  
    )

# print scan report in json format
for i in response['Items']:  
    print(json.dumps(i))