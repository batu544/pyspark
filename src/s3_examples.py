import boto3

def get_client():
    return boto3.client('s3')


# list buckets present in your account

def list_all_buckets(s3_cli):

    resp = s3_cli.list_buckets()
    for bucket in resp['Buckets']:
        print(bucket['Name'])


def list_all_objects(s3_cli, bucket=''):
    resp = s3_cli.list_objects_v2(Bucket=bucket)

    for keys in resp['Contents']:
        print(keys['Key'])


# built complete path of s3 object for matching input object name

def build_complete_path():
    resp = s3_client.list_object_v2(Bucket=bucket, )

if __name__ == '__main__':
    clint = get_client()
    list_all_buckets(clint)
    list_all_objects(clint, 'my-awsphotos')
