"""
Summary: This code will download a file from the s3 bucket.
"""

import logging
import boto3
from botocore.exceptions import ClientError

# Create an S3 client
s3 = boto3.resource('s3')

#Set the variable for bucket and the file you are downloading.
BUCKET_NAME = 'InsertTheBucketName' # replace with your bucket name
KEY = 'InsertTheFileWithTheExtenstion' # replace with your object key

#Locate the bucket and the file & download it & change the name
try:
    s3.Bucket(BUCKET_NAME).download_file(KEY, 'TheNameYouWantToChangeTheFileToo.TheSameExtenstion')
    print("File sucessfilly downloaded!")
#If the program fails with an error code of 404 print a message.    
except s3.exceptions.ClientError as e:
    if e.response['Error']['Code'] == "404":
        print("The object does not exist.")
    else:
        raise
