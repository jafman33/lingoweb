from app import app
# import yaml
# from flask_mysqldb import MySQL
# from faunadb.client import FaunaClient
# import boto3
# import os
# from dotenv import load_dotenv


# reads key-value pairs from a .env file and can set them as environment variables
# load_dotenv()

# client = FaunaClient(
#     secret=os.getenv("FAUNA_KEY"),
#     domain="db.us.fauna.com",
#     port=443,
#     scheme="https"
#     )

# Configure the required config variables for boto3.
# app.config['S3_BUCKET'] = os.getenv('S3_BUCKET')
# app.config['S3_KEY'] = os.getenv('S3_KEY')
# app.config['S3_SECRET'] = os.getenv('S3_SECRET')

# s3 = boto3.client(
#     's3',
#     aws_access_key_id=app.config['S3_KEY'],
#     aws_secret_access_key=app.config['S3_SECRET']
# )

# Configure mySQL database
# db = yaml.full_load(open('yaml/db.yaml'))
# app.config['MYSQL_HOST'] = db['mysql_host']
# app.config['MYSQL_USER'] = db['mysql_user']
# app.config['MYSQL_PASSWORD'] = db['mysql_password']
# app.config['MYSQL_DB'] = db['mysql_db']
# mysql = MySQL(app)
