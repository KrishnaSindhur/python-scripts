import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.create_table(
    TableName = 'soccer_world',
    KeySchema =[
        {
     'AttributeName' : 'username',
     'KeyType' : 'HASH'
        },
        {
     'AttributeName' : 'last_name',
     'KeyType' : "RANGE"
        }
    ],
    AttributeDefinitions =[
        {
     'AttributeName' : 'username',
     'AttributeType' : 'S'
        },
        {
     'AttributeName' : 'last_name',
     'AttributeType' : 'S'
        },

    ],
    ProvisionedThroughput={

        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)
table.meta.client.get_waiter('table_exists').wait(TableName='soccer_world')

print "table is created with %d items" %(table.item_count)
# if output zero then table is created
# lets add some items
table = dynamodb.Table('soccer_world')
print "time when table is created at %s" %(table.creation_date_time)

with table.batch_writer() as batch:
    batch.put_item(
        Item={
            'account_type': 'ballondor',
            'username': 'cr7',
            'first_name': 'cristiano',
            'last_name': 'ronaldo',
            'age': 32,
        }
    )
    batch.put_item(
        Item={
            'account_type': 'ballondor',
            'username': 'mesi10',
            'first_name': 'lenol',
            'last_name': 'messi',
            'age': 30,
        }
    )
    batch.put_item(
        Item={
            'account_type': 'ballondor',
            'username': 'nymr',
            'first_name': 'neymar',
            'last_name': 'santos.junior',
            'age': 25,
        }
    )
print "added static items to table"
print "Table status"
print "press 0 to delete the table"
print "press 1 to keep table"
n = int(raw_input())
if n == 0:
    table.delete()
    print "table is deleted"
elif n == 1:
    print"table is safe"
