#!/usr/bin/python

import boto3
import csv
from pprint import pprint


aws_mgmt_console = boto3.session.Session(profile_name="default")
ec2_mgmt_console = aws_mgmt_console.client(service_name="ec2", region_name="us-east-1")

volume_response=ec2_mgmt_console.describe_volumes()['Volumes']

attachments=[]
volume_infos=[]
volume_infos1=[]
for each_item in volume_response:
    attachments.append(each_item['Attachments'])

# for each_attachment in attachments:
#     for each_item in each_attachment:
#         volume_infos.append(each_item['InstanceId'])

with open('./listvolumes.csv', 'w') as csvfile:
    # Write Header for csv file 
    fields = [ 'VolumeId', 
               'Size',
               'State',
               'VolumeType',
               'AvailabilityZone',
             ]
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
                
    for each_volume in volume_response:
      # volume_infos1.append(each_volume['VolumeId'])
      # volume_infos1.append(each_volume['Size'])
      # volume_infos1.append(each_volume['State'])
      # volume_infos1.append(each_volume['VolumeType'])
      # volume_infos1.append(each_volume['AvailabilityZone'])
        volume_details = [ 
                            each_volume['VolumeId'],
                            each_volume['Size'],
                            each_volume['State'],
                            each_volume['VolumeType'],
                            each_volume['AvailabilityZone'],
                        ]
        csvwriter.writerow(volume_details)


