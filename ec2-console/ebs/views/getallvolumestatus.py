#!/usr/bin/python

import boto3
import csv
from pprint import pprint


aws_mgmt_console = boto3.session.Session(profile_name="default")
ec2_mgmt_console = aws_mgmt_console.client(service_name="ec2", region_name="us-east-1")

volume_response=ec2_mgmt_console.describe_volumes()['Volumes']

attachments=[]
volume_instance_infos=[]
for each_item in volume_response:
    attachments.append(each_item['Attachments'])

for each_attachment in attachments:
    for each_item in each_attachment:
        volume_instance_infos.append(each_item['InstanceId'])
        volume_instance_infos.append(each_item['VolumeId'])
        volume_instance_infos.append(each_item['State'])
        volume_instance_infos.append(each_item['Device'])
        





# Get list of all volumes
#for each_volume in volume_response:
#    print(each_volume['VolumeId'],each_volume['Size'],each_volume['State'],each_volume['VolumeType'],each_volume['AvailabilityZone'])


