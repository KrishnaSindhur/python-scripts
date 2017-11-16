''' This script will create golden image of a stopped instance in that particular region
using boto3 this code is static and asssumes has only 1 stopped instance in that region
it can be changed into dynamic also very easily'''

import boto3
import time

''' credentials can be given in aws configure if your running in local machine
or its better to assign roles in IAM to ec2 instance if your running the script in ec2 instance'''

ec2 = boto3.resource('ec2')
ec = boto3.client('ec2')
for instance in ec2.instances.all():
    if instance.state['Name'] == 'stopped':
        ids =instance.id
AMIid = ec.create_image(InstanceId=ids, Name = "MyImage",Description="Testing",NoReboot=True, DryRun=False)
image = ec2.Image(AMIid['ImageId'])
print image.state
while image.state == "pending":
    time.sleep(5)
    image.load()
if image.state == "available":
    print "Image is created"
    print "Created AMI %s " % (AMIid['ImageId'])
    print "copying and encrypting image"
    response = ec.copy_image(Name = 'newami',SourceImageId=AMIid['ImageId'],SourceRegion = 'us-east-1',Encrypted=True)
    print "Done, Cheres!!!"
