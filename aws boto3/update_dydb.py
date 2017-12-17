# This script will update the dynamodb table in simple way and change the values according to conditions

from boto3 import resource
from boto3.dynamodb.conditions import Key
import boto3
# The boto3 dynamoDB resource
dynamodb_resource = resource('dynamodb')
table_name = 'name'
table = dynamodb_resource.Table(table_name)
imageId = ['ami-xxx..','ami-xx...']
for ami_id in imageId:
    filter_key = 'ImageId'
    filter_value = ami_id
    if filter_key and filter_value:
            filtering_exp = Key(filter_key).eq(filter_value)
            response = table.scan(FilterExpression=filtering_exp)
    else:
     	      response = table.scan()

    items = response['Items']
#print response

    while True:
	       print len(response['Items'])
           if response.get('LastEvaluatedKey'):
               response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
               items += response['Items']
           else:
               break

    print items[0]['is_active']

    print len(items)

    if items[0]['is_active'] == 'Yes':
        client = boto3.client('dynamodb')
        client.put_item(TableName=table_name, Item={'ImageId':{'S':items[0]['ImageId']},'CreationDate':{'S':items[0]['CreationDate']},'AccountRegionOS':{'S':items[0]['AccountRegionOS']},'MessageId':{'S':items[0]['MessageId']},'is_active':{'S':'No'}})
