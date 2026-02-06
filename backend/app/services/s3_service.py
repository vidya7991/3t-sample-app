import uuid
import boto3

from app.core.config import (
    S3_ACCESS_KEY,
    S3_SECRET_KEY,
    S3_ENDPOINT_URL,
    S3_REGION,
    S3_BUCKET,
)


session = boto3.session.Session(
    aws_access_key_id=S3_ACCESS_KEY,
    aws_secret_access_key=S3_SECRET_KEY,
    region_name=S3_REGION,
)

s3 = session.client("s3", endpoint_url=S3_ENDPOINT_URL)


def ensure_bucket() -> None:
    existing = [b["Name"] for b in s3.list_buckets().get("Buckets", [])]
    if S3_BUCKET not in existing:
        s3.create_bucket(Bucket=S3_BUCKET)


def upload_fileobj(fileobj, content_type: str | None) -> str:
    key = str(uuid.uuid4())
    extra = {"ContentType": content_type} if content_type else {}
    s3.upload_fileobj(fileobj, S3_BUCKET, key, ExtraArgs=extra)
    return key
