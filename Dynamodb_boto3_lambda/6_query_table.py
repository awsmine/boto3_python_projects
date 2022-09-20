#!/usr/bin/env python3.7


# 6_query_table.py
# you can query the items in the table using the DynamoDB.Table.query() method.


# for formatting
import json


# To use Boto3, you must first import AWS Python SDK
import boto3


# For querying, Import the boto3.dynamodb.conditions.Key and boto3.dynamodb.conditions.Attr classes.
# Import the boto3.dynamodb.conditions.Key when the condition is related to the key of the item.
# Import the boto3.dynamodb.conditions.Attr when the condition is related to an attribute of the item:
from boto3.dynamodb.conditions import Key, Attr


# Get the service resource
dynamodb = boto3.resource('dynamodb')


# Instantiate a table resource object without actually
# creating a DynamoDB table.
table = dynamodb.Table('movies')


# Insert your partition or sort key here along with the attribute
# return the title Silsila
response = table.query(      
    KeyConditionExpression=Key('title').eq('Silsila') 
)

items = response['Items']
print(items)

