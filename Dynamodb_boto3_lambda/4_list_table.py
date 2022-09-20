#!/usr/bin/env python3.7


# 4_list_table.py
# List the table


# To use Boto3, you must first import AWS Python SDK
import boto3


# Get the service resource
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')


# list the table
tables = list(dynamodb.tables.all())
print(tables)