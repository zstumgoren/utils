#!/usr/bin/env python
"""
Script to reconcile an s3 bucket of files against a directory of local files.
Local files not found in s3 will be uploaded. 

USAGE:

    python s3_update.py /full/path/to/local/dir

"""
import os
import sys

from boto.s3.connection import S3Connection
from boto.s3.key import Key


# SET TARGET LOCAL DIRECTORY TO SYNC WITH S3
try:
    # if path from command line is not an valid absolute path, or 
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

conn = S3Connection(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)


def main():

    buckets = conn.get_all_buckets()
    buckets_lkup = dict(zip(xrange(1, len(buckets) + 1), buckets))

    bucket_choice_prompt = "\nPlease select the number of the target bucket:\n\n"

    bucket_names = "\n".join(["\t(%s) %s" % (key, bckt.name) 
                              for key, bckt in sorted(buckets_lkup.items())])

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

    bucket = conn.get_bucket(bucket_name)
 
    keys = get_s3_filenames(bucket)
    base_path, local_files = get_local_filenames(local_directory)

    # Get all files on local but not on s3
    missing_on_s3 = local_files - keys

    if not missing_on_s3:
        sys.exit("Files in %s are synchronized with S3. Nothing uploaded." % base_path)
    
    print "Files found locally that are not on S3."
    for fname in missing_on_s3:
        key = Key(bucket)
        key.key = fname
        target_file = os.path.join(base_path, fname) 
        print "Uploading %s to S3 bucket %s" % (target_file, bucket_name)
        key.set_contents_from_filename(target_file, cb=percent_cb, num_cb=10) 

def percent_cb(complete, total):
    """
    A simple file download status function.
    """
    sys.stdout.write('.')
    sys.stdout.flush()

def get_s3_filenames(bucket):
    return set([key.name for key in bucket.list()])

def get_local_filenames(directory):
    """
    Returns a tuple containing the base filepath before
    a toplevel directory containing files that should be uploaded
    to s3.

    Example:

        ('/home/serdar/Desktop', 
         set([
             'AP_FTP_DATA/AK/dbready/AK_Candidate.txt',
             'AP_FTP_DATA/AK/dbready/AK_Race.txt',
         ...])
        )
         
    """
    files = set([])
    
    base_path, slash, toplevel_path = directory.rpartition('/')

    for dirpath, dirnames, filenames in os.walk(directory):
        # Use the base_path, which is relative depending on system,
        # to isolate the toplevel path and its children. Then
        # combine that truncated path to the filename
        path = dirpath.split(base_path + '/')[-1]
        for filename in filenames:
            files.add(os.path.join(path, filename))

    return base_path, files
    

if __name__ == '__main__':
    main()
