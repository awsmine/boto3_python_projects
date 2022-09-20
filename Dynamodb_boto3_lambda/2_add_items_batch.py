#!/usr/bin/env python3.7


# 2_add_items_batch.py
# get the method put_item for adding the items to the table
# using DynamoDB.Table.batch_writer() so you can both speed up the process
# is used for a large of items



# To use Boto3, you must first import AWS Python SDK
import boto3


# then indicate which service or services you're going to use:
# Get the service resource.
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')


#adding itmes to th etable.
items = [
    {'title': 'Anuradha', 'director': 'Mukherjee'},
    {'title': 'Anand', 'director': 'Mukherjee'},
]


# Instantiate a table resource object without actually
# creating a DynamoDB table.
table = dynamodb.Table('movies')  


# using DynamoDB.Table.batch_writer() so you can both speed up the process
# is used for a large of items
with table.batch_writer() as batch:
    for i in items:
        batch.put_item(    
        Item=i
        )
        
        
        