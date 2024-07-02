import boto3
import time


# Create VPC
ec2 = boto3.client('ec2')
vpc_name = 'sample-vpc'

response = ec2.describe_vpcs(
     Filters = [{ 'Name': 'tag:Name' , 'Values' : [vpc_name]}]
    )

vpcs = response.get('Vpcs',[])

if vpcs:
    vpc_id = vpcs[0]['VpcId']
    print(f"VPC '{vpc_name}' with ID '{vpc_id}' is already exits....")

else:
    vpc_response = ec2.create_vpc(CidrBlock = '10.0.1.0/28')
    vpc_id = vpc_response['Vpc']['VpcId']
    
    time.sleep(5)
    
    ec2.create_tags(Resources = [vpc_id], Tags = [{'Key':'Name', 'Value': vpc_name}])
    print(f"VPC '{vpc_name}' with ID '{vpc_id}' has been created....")
    
# Create Internet Gateway
ig_name = 'sample-ig'

response = ec2.describe_internet_gateways(
     Filters = [{ 'Name': 'tag:Name' , 'Values' : [ig_name]}]
    )

internet_gateways = response.get('InternetGateways',[])

if internet_gateways:
   ig_id = internet_gateways[0]['InternetGatewayId']
   print(f"Internet Gateway'{ig_name}' with ID '{ig_id}' is already exits....")

else:
    ig_response = ec2.create_internet_gateway()
    ig_id = ig_response['InternetGateway']['InternetGatewayId']
    
    ec2.create_tags(Resources = [ig_id], Tags = [{'Key':'Name', 'Value': ig_name}])
    ec2.attach_internet_gateway(VpcId = vpc_id , InternetGatewayId = ig_id)
    print(f"Internet Gateway'{ig_name}' with ID '{ig_id}' has been created....")
    

# Create route table
rt_response = ec2.create_route_table(VpcId = vpc_id)
rt_id = rt_response['RouteTable']['RouteTableId']
route = ec2.create_route (
    RouteTableId = rt_id,
    DestinationCidrBlock = '0.0.0.0/0',
    GatewayId = ig_id
    
    )
print(f"Route table with id {rt_id} has created...")    

# Create subnets
subnet_1 = ec2.create_subnet(VpcId = vpc_id , CidrBlock = '10.0.1.0/28', AvailabilityZone = 'us-east-1a')

print(f"subnet_1 ID = {subnet_1['Subnet']['SubnetId']}")