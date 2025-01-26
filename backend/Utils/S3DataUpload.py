import boto3
from botocore.exceptions import NoCredentialsError
from dotenv import load_dotenv
import os

load_dotenv()


def uploadToS3(file_path, bucket_name, object_name=None, region="ap-southeast-1"):
    # Initialize S3 client
    s3_client = boto3.client(
        "s3",
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY"),
        aws_secret_access_key=os.getenv("AWS_SECRET_KEY"),
        region_name=os.getenv("REGION_NAME"),
    )

    if object_name is None:
        object_name = file_path.split("/")[-1]

    try:
        # Upload the file to S3
        s3_client.upload_file(file_path, bucket_name, object_name)

        # Get the URL of the uploaded file
        file_url = f"https://{bucket_name}.s3.{region}.amazonaws.com/{object_name}"

        return file_url

    except FileNotFoundError:
        print("The file was not found.")
        return None
    except NoCredentialsError:
        print("Credentials not available.")
        return None
