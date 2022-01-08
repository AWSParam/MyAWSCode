# import boto3
# from botocore.exceptions import NoCredentialsError
#
#
#
# ACCESS_KEY = 'AKIAZZEVVOOIX5QWG7WB'
# SECRET_KEY = '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'
#
# print("Access Key  : ", ACCESS_KEY)
# print("Secret Key  : ", SECRET_KEY)
#
# local_file = 'input/Test.text'
# bucket = 'test-bucket-conti-001'
# s3_file = 'Test_File'
# s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
#
# r = s3.upload_file(local_file, bucket, s3_file)
# print(r)\


import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv("input/Demo.csv")
print(df)

host='testdb.cnqqfgiwd1gu.ap-south-1.rds.amazonaws.com'
user='admin'
password = "Test1234"
database="DemoDb"
url = user+":"+password+"@"+host+"/"+database
engine = create_engine('mysql+pymysql://'+url)
# df.to_sql("TestTable", con = engine)
df_1 = pd.read_sql_table('TestTable', engine)
print(df_1)
