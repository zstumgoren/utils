#!/usr/bin/env python
"""
Shell script to upload local files to s3. Only uploads local files not found in s3.
"""
import sys

from utils.aws.credentials.zstumgoren import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY
from utils.aws.s3 import S3


#TODO: Replace argv with argparse
# Local directory of files and bucket name which will be compared
try:
    local_directory = sys.argv[1] 
    bucket_name = sys.argv[2]    
except IndexError:
    sys.exit("You must supply a target directory and an S3 bucket name.")

def main():
    conn = S3(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
    conn.sync_local_dir_to_bucket(local_directory, bucket_name)

if __name__ == '__main__':
    main()
