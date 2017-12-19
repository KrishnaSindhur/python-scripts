''' This script will give the snapshot id for all the deregisterd images in aws''' 


import boto3

client = boto3.client('ec2')
resource = client.describe_images(Owners=['self'])
#print len(resource['Images'])
#print resource['Images'][0]['ImageId']
ami_ids = []
for i in range(len(resource['Images'])):
        ami_id =  resource['Images'][i]['ImageId']

      	ami_ids.append(str(ami_id))
#print ami_ids
resource = client.describe_snapshots(OwnerIds=['self'])
#print resource
#print resource['Snapshots'][0]['SnapshotId']

snap_amids = []
snap_ids = []
for i in range(len(resource['Snapshots'])):
        idu = resource['Snapshots'][i]['Description']
        ids = resource['Snapshots'][i]['SnapshotId']
        idu = idu[48:60]
        snap_amids.append(idu)
        snap_ids.append(ids)
#print snap_amids
#print snap_ids
print "These are snapshots without image with SnapshotId and its imageId"
for i in range(len(snap_amids)):
     if snap_amids[i] not in ami_ids:
        print "%s and  %s" %(snap_ids[i],snap_amids[i])
