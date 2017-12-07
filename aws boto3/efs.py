''' 
In aws this script will mount efs to current ec2 instance in which you are runnning this python script
before running this you will have to install boto3 and in aws configure give the region''' 

import boto3
import time
import os

ec2 = boto3.resource('ec2')
client = boto3.client('ec2')
sub_id = set()

for vpc in ec2.vpcs.all():
    for subnet in vpc.subnets.all():
        sub_id.add(subnet.id)
#print sub_id
sub_id = list(sub_id)
print "Subnets:"
print sub_id
client = boto3.client('efs')
response = client.create_file_system(
    CreationToken='tokenstring',
    PerformanceMode='generalPurpose',
)

#print response['FileSystemId']
fsid = response['FileSystemId']
print "FileSystemId:- %s" %(fsid)
#print fsid
#print type(fsid)
time.sleep(60)
for i in range(len(sub_id)):
    response = client.create_mount_target(
        FileSystemId=fsid,
        SubnetId=sub_id[i],
    )
    #print(response)

os_type = str(raw_input("Enter the flavours of linux you are using ubuntu or others:- "))
fsid = str(fsid)
time.sleep(60)
if os_type == 'ubuntu':
    os.system("sudo apt-get update")
    os.system("sudo apt-get install nfs-common")
    os.system("sudo mkdir efs")
    os.system("sudo mount -t nfs4 -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2 {}.efs.us-east-1.amazonaws.com:/ efs".format(fsid))
else:
    os.system("sudo yum update -y")
    os.system("sudo yum install -y nfs-utils")
    os.system("sudo mkdir efs")
    os.system("sudo mount -t nfs4 -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2 {}.efs.us-east-1.amazonaws.com:/ efs".format(fsid))
