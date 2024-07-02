import boto3

ec2 = boto3.resource('ec2')
instance_name = 'simple-ec2'

instance_id = None

instances = ec2.instances.all()
instance_exits = False

for instance in instances:
    for tag in instance.tags:
        if tag['Key'] == 'Name' and tag['Value'] == instance_name:
            instance_exits = True
            instance_id = instance.id
            print(f"Instance {instance_name} with ID {instance_id} already exists...")
    if instance_exits:
        break

if not instance_exits:
        new_instance = ec2.create_instances(
            ImageId='ami-04b70fa74e45c3917',
            InstanceType= 't2.micro',
            KeyName='Key1',
            MaxCount=1,
            MinCount=1,
            
            TagSpecifications=[
                {
                    'ResourceType': 'instance',
                    'Tags': [
                        {
                            'Key': 'Name',
                            'Value': instance_name
                        },
                    ]
                },
                
            ]
            
        )
    
        instance_id = new_instance[0].id
        print(f"Instance {instance_name} with ID {instance_id} already exists...")
    
# Stop instance
ec2.Instance(instance_id).stop()
print(f"Instance {instance_name} with ID {instance_id} is stopped...")

# Start instance
ec2.Instance(instance_id).start()
print(f"Instance {instance_name} with ID {instance_id} is started...") 

# Terminated instace
ec2.Instance(instance_id).terminate()
print(f"Instance {instance_name} with ID {instance_id} is started...") 
    