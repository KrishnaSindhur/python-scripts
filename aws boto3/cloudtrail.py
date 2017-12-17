''' lambda function to filters certain events in cloud trailfrom current time to past 24 hours 
and sends email to notify if events has occured, here it return AMI_ID od deregistered image''' 


from __future__ import print_function

import json
import datetime
import collections
import boto3
print('Loading function')

imageId = []
def lambda_handler(event, context):
    cloudtrail = boto3.client('cloudtrail')
    eventName = 'DeregisterImage'
    endtime = datetime.datetime.now()
    interval = datetime.timedelta(hours=24)
    starttime = endtime - interval
    try:
    	response = cloudtrail.lookup_events(
            LookupAttributes=[
                {
                    'AttributeKey': 'EventName',
                    'AttributeValue': eventName
                },
            ],
            StartTime=starttime,
            EndTime=endtime,
            MaxResults=50
        )
    except Exception as e:
        print(e)
        print('Unable to retrieve CloudTrail for event "{}"'.format(eventName))
        raise(e)
    events = response
    resource_name_counter = collections.Counter()
    for event in events['Events']:
        resources = event.get("Resources")
        if resources is not None:
            resource_name_counter.update([resource.get("ResourceName") for resource in resources])

    for i,v in enumerate(resource_name_counter):
        imageId.append(v)
    if len(imageId) > 0:

        client = boto3.client("sns")
        topic_arn = 'arn:aws:sns:us-east-1:109600190682:notifications'
        client.publish(Message="there was %d image which is dderegistered"%(len(imageId)), TopicArn=topic_arn)
    return imageId
