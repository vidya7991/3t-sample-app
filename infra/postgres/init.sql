-- Initial SQL (optional)
CREATE TABLE IF NOT EXISTS files (
  id SERIAL PRIMARY KEY,
  original_name TEXT NOT NULL,
  s3_key TEXT NOT NULL,
  content_type TEXT,
  size_bytes BIGINT NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT NOW()
);
