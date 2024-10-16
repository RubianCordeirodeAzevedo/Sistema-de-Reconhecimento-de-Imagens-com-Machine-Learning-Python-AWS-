import boto3
import os

# Initialize S3 client
s3 = boto3.client('s3')

def upload_to_s3(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket"""
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    response = s3.upload_file(file_name, bucket, object_name)
    return response
