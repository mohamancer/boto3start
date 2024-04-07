import boto3

# Create an EC2 client
ec2_client = boto3.client('ec2')

def list_instance_ids():
    # Use the describe_instances() method to fetch information about the instances
    response = ec2_client.describe_instances()

    # Loop through the response to extract instance IDs
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            print(instance['InstanceId'])

if __name__ == "__main__":
    list_instance_ids()
