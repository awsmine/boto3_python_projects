# AWS Python SDK
import boto3


# A low-level client representing Amazon Elastic Compute Cloud (EC2)
ec2_client=boto3.client("ec2")


# use Amazon service ec2
ec2_resource=boto3.resource("ec2")


# create 4 ec2 instances
ec2_resource.create_instances(
    ImageId='ami-090fa75af13c156b4',
    InstanceType='t2.micro',
    MaxCount=5,
    MinCount=5)


# List of ec2 instance ids
ec2_instance_ids = []


# iterate and prints all ec2 instances 
# EXCEPT Cloud9 id - i-0e6238103c9b3f9a8
response=ec2_client.describe_instances()


# reservations = response['Reservations']
for reservation in response['Reservations']:
   
    for instance in reservation['Instances']:
        # instanceId = instance["InstanceId"]
        # not to print Cloud9 id - i-0e6238103c9b3f9a8
        if ("i-0e6238103c9b3f9a8" != instance["InstanceId"]):
                print(instance["InstanceId"])
                ec2_instance_ids.append(instance["InstanceId"])


# create tags for 3 ec2 instances
# with **Environment: Dev** tag
response=ec2_client.create_tags(
    Resources=[
        ec2_instance_ids[1], ec2_instance_ids[2], ec2_instance_ids[3],
    ],
    Tags=[
        {
            'Key': 'Environment',
            'Value': 'dev',
        },
    ],
)


# filters **running** instances that have the **Environment: Dev** tag.
instances = ec2_resource.instances.filter(
    Filters = [{'Name': 'instance-state-name', 'Values': ['running']},
        {'Name': 'tag:Environment', 'Values':['dev']}])


# only stops **running** instances that have the **Environment: Dev** tag.
for instance in instances:
    try:
        instance.stop()
        print(f'{instance} stopped')
    except:
        print(f'Error stopping {instance}')
     