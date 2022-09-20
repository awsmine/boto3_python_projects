#!/usr/bin/env python3.7


# 3_add_items.py
# get the method put_item to create for adding the items to the table


# To use Boto3, you must first import AWS Python SDK
import boto3


# Get the service resource
dynamodb = boto3.resource('dynamodb')


# Instantiate a table resource object without actually
# creating a DynamoDB table.
table = dynamodb.Table('movies')



# add new items to the table
# adding 1st item
table.put_item(
   Item={
        'title': 'Silsila',
        'director': 'Chopra',
    }
)


# adding 2nd item
table.put_item(
   Item={
        'title': 'Batman',
        'director': 'Martin',
    }
)


# adding 3rd item
table.put_item(
   Item={
        'title': 'Abhimaan',
        'director': 'Mukherjee',
    }
)


# adding 4th item
table.put_item(
   Item={
        'title': 'Mili',
        'director': 'Mukherjee',
    }
)

