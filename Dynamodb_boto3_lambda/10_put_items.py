#!/usr/bin/env python3.7


# 10_put_items.py
# Create and run the Python script to validate that you cannot write an item to the DynamoDB table.



# To use Boto3, you must first import AWS Python SDK
import boto3


# Get the service resource
dynamodb = boto3.resource('dynamodb')


# Instantiate a table resource object without actually
# creating a DynamoDB table.
table = dynamodb.Table('movies')



# add new items to the table
# adding an item
table.put_item(
   Item={
        'title': 'Khoobsurat',
        'director': 'Mukherjee'
    }
)


