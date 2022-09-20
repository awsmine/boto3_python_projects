#!/usr/bin/env python3.7


# 9_delete_items.py
# get the method delete_item() and create the file
# You can also delete the item using DynamoDB.Table.delete_item()


# To use Boto3, you must first import AWS Python SDK
import boto3


# Get the service resource
dynamodb = boto3.resource('dynamodb')


# Instantiate a table resource object without actually
# creating a DynamoDB table.
table = dynamodb.Table('movies')


# delete the item from the table
table.delete_item(
    Key={
        'title': 'Mili',
        'director': 'Mukherjee'
    }
)

