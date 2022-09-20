#!/usr/bin/env python3.7


# 5_print_table_data.py
# print data from table


# To use Boto3, you must first import AWS Python SDK
import boto3


# Get the service resource
dynamodb = boto3.resource('dynamodb')


# Instantiate a table resource object without actually
# creating a DynamoDB table.
table = dynamodb.Table('movies')


# You will need the table_arn for updating the role for accessing dynamodb table
# Similarly you can print out table_id, table_name, and table_status


# This will cause a request to be made to DynamoDB and its attribute
# Print out those attributes about the table.
print('Table ARN: ' + table.table_arn)
print('Table ID: ' + table.table_id)
print('Table Name: ' + table.table_name)
print('Table Status: ' + table.table_status)


