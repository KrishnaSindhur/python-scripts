''' This script will transfer any files from amazon linux ec2 instance
of one particular file structure to similar file structure in aws s3 bucket'''


import boto3
import os
BUCKET_NAME = 'bucket_name'

''' credentials can be given in aws configure if your running in local machine
or its better to assign roles to ec2 instance in IAM if your running the script in ec2 instance'''

s3 = boto3.resource('s3')
for i in range(1,3):
        path = 'main_directory/sub_directory%d/'%i
        listing = os.listdir(path)
        for infile in listing:
                #print "current file is: " + infile
        	data = open('main_directory/sub_directory%d/%s'%(i,infile), 'rb')
        	s3.Bucket(BUCKET_NAME).put_object(Key='main_directory/sub_directory%d/%s'%(i,infile), Body=data)
print ("Transfer successfully done")
