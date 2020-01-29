"""
Summary: This code will create a new s3 Bucket
"""

import boto3

#Create an S3 client
s3 = boto3.client('s3')

#Create a new bucket
s3.create_bucket(Bucket = 'InsertTheBucketNameBetweenTheQuotes')
