#!/usr/bin/env python3.7


# 11_delete_table.py
# delete the table - movies


# To use Boto3, you must first import AWS Python SDK
import boto3


# A low-level client representing DynamoDB
dynamodb = boto3.client('dynamodb')


# delete the table movies
response = dynamodb.delete_table(
    TableName='movies'
)

