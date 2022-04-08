from os import getenv

import boto3
import botocore.exceptions
from botocore.config import Config

AWS_REGION = getenv("AWS_REGION", "us-east-1")
CUSTOM_CONFIG = Config(region_name=AWS_REGION)
#
s3_client = boto3.client("s3", region_name=AWS_REGION)

def already_policy(name_of_bucket):
    try:
        response = s3.get_bucket_policy(Bucket=name_of_bucket)
        pprint(response.get('Policy'))
    except ClientError as e:
        return apply_policy(name_of_bucket)


def generate_public_read_policy(name_of_bucket):
    return json.dumps({
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "PublicReadGetObject",
                "Effect": "Allow",
                "Principal": "*",
                "Action": "s3:GetObject",
                'Resource': [
                    f'arn:aws:s3:::{name_of_bucket}/dev/*',
                    f'arn:aws:s3:::{name_of_bucket}/test/*',
                ],
            }
        ]
    })


def apply_policy(name_of_bucket):
    if s3.put_bucket_policy(Bucket=name_of_bucket,
                            Policy=generate_public_read_policy(name_of_bucket)):
        print(f'policy has been applied to {name_of_bucket}')


if __name__ == '__main__':
    already_policy('test-lab-4343423')