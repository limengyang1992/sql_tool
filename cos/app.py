# pip install -U cos-python-sdk-v5

from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
import os

# 连接cos
secret_id = '**********'     
secret_key = '**********'   
config = CosConfig(Region='ap-beijing', SecretId=secret_id, SecretKey=secret_key, Token=None, Scheme='https')
client = CosS3Client(config)

def cos_upload_file(path_file,dirs="***"):
    file_name = os.path.basename(path_file)
    client.upload_file(Bucket='****',LocalFilePath=path_file,Key=os.path.join(dirs,file_name),PartSize=1,MAXThread=10,EnableMD5=False)