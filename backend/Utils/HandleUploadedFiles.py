import os
import tempfile
from fastapi import UploadFile
from Utils.S3DataUpload import uploadToS3

bucketName = os.getenv("BucketName")


# Function to handle FastAPI `UploadFile`
def handleUploadToS3(file: UploadFile, bucket_name: str, region="ap-southeast-1"):
    # Save file temporarily
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        file_path = tmp_file.name
        tmp_file.write(file.file.read())  # Write the file's content to temp file

    try:
        # Upload the file to S3
        object_name = file.filename  # Use the original filename
        file_url = uploadToS3(file_path, bucket_name, object_name, region)
        return file_url
    finally:
        # Remove the temporary file
        os.remove(file_path)
