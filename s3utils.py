import boto3
from boto3.s3.transfer import S3Transfer

### AWS credentials ###
AWS_ACCESS_KEY_ID = <your access key>
AWS_SECRET_ACCESS_KEY = <your secret access key> 
AWS_HOST= <your host>
REGION_NAME= <your region>
API_VERSION='2006-03-01'
BUCKET = <your bucket>

CREDENTIALS = {
        'aws_access_key_id': AWS_ACCESS_KEY_ID,
        'aws_secret_access_key': AWS_SECRET_ACCESS_KEY
}

def s3_upload(filename,key,content_type):

    client = boto3.client('s3', REGION_NAME, **CREDENTIALS)
    transfer = S3Transfer(client)

    transfer.upload_file(filename, BUCKET, key,
                         extra_args={'ACL': 'public-read','ContentType':content_type})

    file_url = '%s/%s/%s' % (client.meta.endpoint_url, BUCKET, key)

    print("**** this is the upload url :: " + file_url)
  
def s3_download(key, filename):

    client = boto3.client('s3', REGION_NAME, **CREDENTIALS)
    transfer = S3Transfer(client)

    print(filename + "<--- filename & key ----->" + key)

    transfer.download_file(BUCKET, key, filename)

    download_path = 'https://' + AWS_HOST + '/' + BUCKET + '/' + key

    print("**** this is the download url :: ", download_path)
    
