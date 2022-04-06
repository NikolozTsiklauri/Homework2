from os import getenv

import boto3
import botocore.exceptions
from botocore.config import Config

AWS_REGION = getenv("AWS_REGION", "us-east-1")
CUSTOM_CONFIG = Config(region_name=AWS_REGION)
#
s3_client = boto3.client("s3", region_name=AWS_REGION)


def Already_buckets(name):
    try:
        response = s3_client.head_bucket(Bucket=name)
    except botocore.exceptions.ClientError:
        return False
    status_code = response["ResponseMetadata"]["HTTPStatusCode"]
    if status_code == 200:
        return True
    return False


def create_bucket(Name_Of_Bucket):
    if not Already_buckets(Name_Of_Bucket):
        try:
            s3_client.create_bucket(Bucket=Name_Of_Bucket)
            print(f"Bucket '{Name_Of_Bucket}' created successfuly")
        except botocore.exceptions.ClientError as ex:
            print(ex)
    else:
        print(f"Bucket'{Name_Of_Bucket}' already exists")


def main():
    bucket_name = "btu-test-lab4"
    create_bucket(bucket_name)

if __name__ == '__main__':
    main()