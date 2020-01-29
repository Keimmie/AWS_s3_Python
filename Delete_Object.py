"""
Summary: This code will put an delete an obejct in my s3 Bucket
"""

import logging
import boto3
from botocore.exceptions import ClientError

# Create an S3 client
s3 = boto3.client('s3')

#Set the variables
bucket_name = 'TheBucketName'
object_name = 'TheobjectName'

#Delete the object
s3.delete_object(Bucket=bucket_name, Key=object_name)
