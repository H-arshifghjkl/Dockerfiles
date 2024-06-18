#problem-2...Write a script to automate the backup of a specified directory to a remote
#server or a cloud storage solution. The script should provide a report on the
#success or failure of the backup operation.


#used python script......

import os
import shutil
import subprocess
import datetime
import boto3
import paramiko

# Configuration
BACKUP_SOURCE_DIR = '/path/to/your/source/directory'  # Directory to be backed up
BACKUP_DEST_DIR = '/path/to/your/backup/directory'   # Local directory where backups will be stored temporarily
REMOTE_SSH_HOST = 'your_remote_host'  # Remote server hostname or IP
REMOTE_SSH_PORT = 22  # SSH port of the remote server
REMOTE_SSH_USER = 'your_ssh_user'  # SSH username for remote server
REMOTE_SSH_DEST_DIR = '/path/to/remote/backup/directory'  # Directory on the remote server to store backups
AWS_S3_BUCKET_NAME = 'your-s3-bucket-name'  # AWS S3 bucket name for cloud storage
AWS_REGION = 'your-aws-region'  # AWS region where the S3 bucket is located

def backup_to_local():
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    backup_dir = os.path.join(BACKUP_DEST_DIR, f'backup_{timestamp}')
    
    try:
        shutil.copytree(BACKUP_SOURCE_DIR, backup_dir)
        print(f"Backup to local directory '{backup_dir}' successful.")
        return True
    except Exception as e:
        print(f"Backup to local directory '{backup_dir}' failed: {str(e)}")
        return False

def backup_to_remote():
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        ssh_client.connect(REMOTE_SSH_HOST, port=REMOTE_SSH_PORT, username=REMOTE_SSH_USER)
        sftp_client = ssh_client.open_sftp()
        
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        remote_backup_dir = os.path.join(REMOTE_SSH_DEST_DIR, f'backup_{timestamp}')
        sftp_client.mkdir(remote_backup_dir)
        
        local_backup_dir = os.path.join(BACKUP_DEST_DIR, f'backup_{timestamp}')
        shutil.copytree(BACKUP_SOURCE_DIR, local_backup_dir)
        
        for root, dirs, files in os.walk(local_backup_dir):
            for file in files:
                local_file_path = os.path.join(root, file)
                remote_file_path = os.path.join(remote_backup_dir, file)
                sftp_client.put(local_file_path, remote_file_path)
        
        sftp_client.close()
        ssh_client.close()
        
        print(f"Backup to remote directory '{remote_backup_dir}' on {REMOTE_SSH_HOST} successful.")
        return True
    except Exception as e:
        print(f"Backup to remote directory '{remote_backup_dir}' on {REMOTE_SSH_HOST} failed: {str(e)}")
        return False

def backup_to_s3():
    s3_client = boto3.client('s3', region_name=AWS_REGION)
    
    try:
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        s3_backup_key = f'backup_{timestamp}/'
        
        local_backup_dir = os.path.join(BACKUP_DEST_DIR, f'backup_{timestamp}')
        shutil.copytree(BACKUP_SOUR
