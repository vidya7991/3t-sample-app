from fastapi import APIRouter, UploadFile, File, HTTPException
from sqlalchemy import select

from app.db.session import SessionLocal
from app.db.models.file import FileRecord
from app.schemas.file import FileOut
from app.services.s3_service import ensure_bucket, upload_fileobj

router = APIRouter()


@router.get("/files", response_model=list[FileOut])
def list_files():
    with SessionLocal() as db:
        rows = db.scalars(select(FileRecord).order_by(FileRecord.created_at.desc())).all()
        return rows


@router.post("/files")
def upload_file(file: UploadFile = File(...)):
    if not file.filename:
        raise HTTPException(status_code=400, detail="Missing filename")

    ensure_bucket()
    key = upload_fileobj(file.file, file.content_type)

    with SessionLocal() as db:
        record = FileRecord(
            original_name=file.filename,
            s3_key=key,
            content_type=file.content_type,
            size_bytes=file.size or 0,
        )
        db.add(record)
        db.commit()
        db.refresh(record)
        return {"id": record.id}
