import boto3
import logging
from datetime import datetime
import json

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    
    ec2 = boto3.client('ec2')
    current_time = datetime.now().strftime("%Y-%m-%d")
    
    try:
        response = ec2.create_snapshot(
            VolumeId = 'vol-079cd2c6adafc00de',
            Description = 'My EC2 Snapshot',
            TagSpecifications = [
                {
                    'ResourceType' : 'snapshot',
                    'Tags' : [
                        {
                        'Key' : 'Name',
                        'Value' : f"My EC2 snapshot {current_time}"
                        }
                    ] 
                }
                
                ]
            
            
            )
        
        logger.info(f"Successfully created Snapshot : {json.dumps(response , default=str)}")   
    
    except Exception as e :
        logger.error(f"Facing issue with snapshot: {str(e)}")
    
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
