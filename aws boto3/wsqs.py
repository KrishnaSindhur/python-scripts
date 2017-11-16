''' This script will collect instance id which are stopped instances and creates queue
and sends to the queue '''



#!/usr/bin/env python
import boto3
import sys
import time


''' credentials can be given in aws configure if your running in local machine
or its better to assign roles in IAM to ec2 instance if your running the script in ec2 instance
for security purpose'''

a = []
ec2 = boto3.resource('ec2')
for instance in ec2.instances.all():
    if instance.state['Name'] == 'stopped':
        #print type(instance.id)
        a.append(instance.id)
#print a
#print
sqs = boto3.resource('sqs')
queue = sqs.create_queue(QueueName='test', Attributes={'DelaySeconds': '5'})
print(queue.url)
get_queue = sqs.get_queue_by_name(QueueName='test')
for msg in a:
    response = get_queue.send_message(MessageBody= msg)
print response
# sorry for bad naming of variables due to time constarint
