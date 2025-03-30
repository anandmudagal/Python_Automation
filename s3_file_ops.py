# s3_file_ops.py
import boto3

def list_s3_files(bucket_name, prefix=''):
    s3 = boto3.client('s3')
    response = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix)
    if 'Contents' in response:
        return [obj['Key'] for obj in response['Contents']]
    return []

def download_file(bucket_name, key, dest_path):
    s3 = boto3.client('s3')
    s3.download_file(bucket_name, key, dest_path)
    return f"Downloaded {key} to {dest_path}"
