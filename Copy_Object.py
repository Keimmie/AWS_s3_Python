"""
Summary: This code will copy a file from one bucket to another.
"""

import logging
import boto3
from botocore.exceptions import ClientError

# Create an S3 client
s3 = boto3.resource('s3')

#define copy object
def copy_object(src_bucket_name, src_object_name,
                dest_bucket_name, dest_object_name=None):

    # Construct source bucket/object parameter
    copy_source = {'Bucket': src_bucket_name, 'Key': src_object_name}
    if dest_object_name is None:
        dest_object_name = src_object_name

    # Copy the object
    s3 = boto3.client('s3')
    try:
        s3.copy_object(CopySource=copy_source, Bucket=dest_bucket_name,
                       Key=dest_object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

#define the main function
def main():

    # Assign these values before running the program
    #The original bucket and file name
    src_bucket_name = 'SourceBuket'
    src_object_name = 'logo.png'
    
    #The new Bucket I want to place the file in
    dest_bucket_name = 'DestinationBucket'
    
    #The name of the new file
    dest_object_name = 'NewLogo.png'

    # Set up logging
    logging.basicConfig(level=logging.DEBUG,
                        format='%(levelname)s: %(asctime)s: %(message)s')

    # Copy the object
    success = copy_object(src_bucket_name, src_object_name,
                         dest_bucket_name, dest_object_name)
                         
    #If the program is executed correctly print the name of the source file and bucket and the info of the new source file and bucket.                      
    if success:
        logging.info(f'Copied {src_bucket_name}/{src_object_name} to '
                     f'{dest_bucket_name}/{dest_object_name}')

if __name__ == '__main__':
    main()
