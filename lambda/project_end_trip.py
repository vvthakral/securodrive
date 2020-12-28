import json
import boto3
import paramiko
import os
import time

def lambda_handler(event, context):
    process_id = int(event['process_id'])
    print(process_id)
    ec_client = boto3.client('ec2')
    s3_client = boto3.client('s3')
    s3_client.download_file('project-ecpem','linux_ami1.pem', '/tmp/file.pem')
    host = 'ec2-54-160-156-213.compute-1.amazonaws.com'
    user = 'ec2-user'
    key = paramiko.RSAKey.from_private_key_file("/tmp/file.pem")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=host,username=user, pkey = key)
    
    #command = 'echo $$; exec ' + 'python3 test.py'
    command = 'echo $$; exec ' + 'kill ' + str(process_id)
    stdin, stdout, stderr = ssh.exec_command(command)
    print(stdout.readline())
    time.sleep(2)
    ssh.close()
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }