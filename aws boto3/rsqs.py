''' This script will receive_messages from queue and starts the
stopped instances and deletes the executed message from the queue'''


#!/usr/bin/env python
import boto3
import time

''' credentials can be given in aws configure if your running in local machine
or its better to assign roles in IAM to ec2 instance if your running the script in ec2 instance
for security purpose'''

sqs = boto3.resource('sqs')
ec2 = boto3.client('ec2')
queue = sqs.get_queue_by_name(QueueName='test')
for message in queue.receive_messages():
    print message.body
    instance_id = message.body
    ec2.start_instances(InstanceIds=[instance_id])
    message.delete()

''' draw back if there are more than one message u have to run agin this script
if all messages should be executed then you have to create seperate threads '''
