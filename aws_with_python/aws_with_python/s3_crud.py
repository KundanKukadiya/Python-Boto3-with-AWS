# import boto3 pacakage
import boto3

# Initialize boto3 resources in s3
s3 = boto3.resource('s3')
bucket_name = 'simple-aws-with-python'

# check if s3 bucket is present or not
# Create if doesn't exists....
all_my_bucket = [bucket.name for bucket in s3.buckets.all()]
if bucket_name not in all_my_bucket:
    print(f"'{bucket_name}' bucket doesn't exists , Creating now...")
    s3.create_bucket(Bucket = bucket_name)
    print(f"'{bucket_name}' bucket has been created..")
    
else:
   print(f"'{bucket_name}' bucket already exists , No need to create") 
   
# create 2 files
file_1 = 'file_1.txt'
file_2 = 'file_2.txt'

# upload files in s3 bucket
s3.Bucket(bucket_name).upload_file(Filename=file_1, Key=file_1)
print(f"File_1 has been uploaded....")
s3.Bucket(bucket_name).upload_file(Filename=file_2, Key=file_2)
print(f"File_2 has been uploaded....")  

# Read file which is uploaded in s3
obj = s3.Object(bucket_name, file_1)
body = obj.get()['Body'].read()
print(body)

# Update file1 with data of file2
s3.Object(bucket_name, file_1).put(Body=open(file_2, 'rb'))
obj = s3.Object(bucket_name, file_1)
body = obj.get()['Body'].read()
print(body)

# Delete file from bucket
s3.Object(bucket_name, file_1).delete()
s3.Object(bucket_name, file_2).delete()

print(f"Both files have been deleted....")

# Delete bucket from s3

bucket = s3.Bucket(bucket_name)
bucket.delete()
print(f"Bucket has been deleted...")