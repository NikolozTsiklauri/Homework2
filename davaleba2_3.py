from os import getenv

import boto3
from botocore.config import Config

AWS_REGION = getenv("AWS_REGION", "us-east-1")
CUSTOM_CONFIG = Config(region_name=AWS_REGION)

s3_client = boto3.client("s3", region_name=AWS_REGION)

def already_bucket(name):
    try:
        response = s3.head_bucket(Bucket=name)
    except ClientError as ex:
        print(ex)
        print(f"Bucket {name} doesn't exist")
        return False
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        return delete_bucket(name)


def delete_bucket(name):
    s3.delete_bucket(Bucket=name)
    print(f'Bucket named {name} has been successfully deleted')


if __name__ == '__main__':
    already_bucket('btu-test-lab4')
