# 3T Sample App (Frontend + Backend + Postgres + S3)

This is a learning scaffold for a 3-tier app:
- **Frontend**: React (Vite)
- **Backend**: FastAPI
- **Data**: PostgreSQL + S3 (LocalStack for local dev)

## Quick Start (Local)
1. Start infra:
   ```bash
   docker-compose up -d
   ```
2. Backend:
   ```bash
   cd backend
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   uvicorn app.main:app --reload
   ```
3. Frontend:
   ```bash
   cd frontend
   npm install
   npm run dev
   ```

## Notes
- S3 is emulated using **LocalStack**.
- Backend writes files to S3 and stores metadata in PostgreSQL.
# 3t-sample-app
