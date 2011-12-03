#!/usr/bin/env python
"""
Script to reconcile an s3 bucket of files against a directory of local files.
Local files not found in s3 will be uploaded. 

USAGE:

    python s3_update.py /full/path/to/local/dir


"""
import os
import sys

from utils.aws.s3 import S3


def main():
    # SET TARGET LOCAL DIRECTORY TO SYNC WITH S3
    try:
        # If path from command line is not a valid absolute path, or 
        # cannot be resolved to a valid abspath, then exit program
        path_from_cli = os.path.abspath(sys.argv[1])
        if os.path.isdir(path_from_cli):
            local_directory = path_from_cli
        else:
            raise IndexError
    except IndexError:
        sys.exit("You must supply a valid local directory for syncing to S3.")


    # SET UP AWS CONNECTION
    try:
        from aws_credentials import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY
    except ImportError:
        sys.exit(
            "\n\tImportError: Unable to import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY from aws_credentials.py" 
            "\n\tYou must create this module with these variables and place it in the same directory"
            "\n\tas the s3_upload.py script.\n"
        )
    
    # PROMPT USER TO CHOOSE A TARGET S3 BUCKET
    buckets = conn.get_all_buckets()
    buckets_lkup = dict(zip(xrange(1, len(buckets) + 1), buckets))
    bucket_choice_prompt = "\nPlease select the number of the target bucket:\n\n"
    bucket_names = "\n".join(["\t(%s) %s" % (key, bckt.name) 

    while True:
        try:
            bucket_id = raw_input(bucket_choice_prompt + bucket_names + '\n')
            bucket_name = buckets_lkup[int(bucket_id)]
            break
        except (KeyError, ValueError):
            print "Sorry, that was an invalid selection.\n"
            continue
        except (KeyboardInterrupt, SystemExit):
            sys.exit("\nExiting...")
 
    # SYNC LOCAL DIR TO S3
    conn = S3(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
    conn.sync_local_dir_to_bucket(local_directory, bucket_name)

if __name__ == '__main__':
    main()
