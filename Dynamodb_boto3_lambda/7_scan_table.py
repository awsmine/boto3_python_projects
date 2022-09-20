#!/usr/bin/env python3.7


# 7_scan_table.py
# scan the table using DynamoDB.Table.scan() method



# To use Boto3, you must first import AWS Python SDK
import boto3


# Get the service resource
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')


# Instantiate a table resource object without actually
# creating a DynamoDB table.
table = dynamodb.Table('movies')


# scan the table
response = table.scan()
items = response['Items']


# print the items in the table
print(items)


