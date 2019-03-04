import boto3
import click

session = boto3.Session(profile_name='pythonAutomation')
s3 = session.resource('s3')

@click.group()
def cli():
    "webotron will deploy website to AWS"
    pass

@cli.command('list-buckets')
def list_buckets():
    "List all s3 buckets"
    for bucket in s3.buckets.all():
        print (bucket)

@cli.command('list-buckets-objects')
@click.argument('bucketname')
def list_buckets_objects(bucketname):
    "This will list all objects in a bucket"
    for obj in s3.Bucket(bucketname).objects.all():
        print (obj)


if __name__ == '__main__':
    cli()
