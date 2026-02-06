from datetime import datetime
from pydantic import BaseModel


class FileOut(BaseModel):
    id: int
    original_name: str
    s3_key: str
    content_type: str | None
    size_bytes: int
    created_at: datetime

    class Config:
        from_attributes = True
