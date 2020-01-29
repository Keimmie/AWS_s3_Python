Summary: This code will delete the s3 Bucket
"""

import logging
import boto3
from botocore.exceptions import ClientError

# Create an S3 client
s3 = boto3.client('s3')

#Set the variables
bucket_name = 'BUcketName'

# Delete the bucket
s3.delete_bucket(Bucket=bucket_name)
