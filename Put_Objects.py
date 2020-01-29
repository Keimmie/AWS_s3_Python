"""
Summary: This code will put an object in my the specified s3 Bucket
"""
import logging
import boto3
from botocore.exceptions import ClientError

# Create an S3 client
s3 = boto3.client('s3')

#Set the variables
dest_bucket_name = 'TheNameOfTheBucket'
dest_object_name = 'TheNameOfTheObject'
object_data = 'This will be a text object put in my bucket.'

# Put the object
s3.put_object(Bucket=dest_bucket_name, Key=dest_object_name, Body=object_data)
