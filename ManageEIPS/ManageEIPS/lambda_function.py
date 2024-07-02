import boto3

def lambda_handler(event, context):
    
    ec2_resource = boto3.resource('ec2')
    
    for elastic_ip in ec2_resource.vpc_addresses.all():
        if elastic_ip.instance_id is None:
            print(f"\n No association with Instance of elastic ID {elastic_ip}. Hence Releasing...\n")
            elastic_ip.release()
    
    
    return {
        'statusCode': 200,
        'body': 'Processing EIP address.....'
    }
