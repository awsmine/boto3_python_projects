#!/usr/bin/env python3.7


# 1_create_table.py 
# Get the method create_table() to create table "movies", and print data from table



# 1_create_table.py 
# Get the method create_table() to create table "movies", and print data from table


# To use Boto3, you must first import AWS Python SDK
import boto3


# A low-level client representing DynamoDB
dynamodb_client=boto3.client('dynamodb')


# use the DynamoDB.ServiceResource.create_table() method:
# then indicate which service or services you're going to use:
# Get the service resource.
dynamodb = boto3.resource('dynamodb')


# Create the DynamoDB table.
table = dynamodb.create_table(
    TableName='movies',
    KeySchema=[
        {
            'AttributeName': 'title',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'director',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'title',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'director',
            'AttributeType': 'S'
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

# Wait until the table exists.
table.wait_until_exists()

# Print out data about the table.
print(table.table_status)

