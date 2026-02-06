import { useEffect, useState } from "react";
import { listFiles, uploadFile } from "./api/files";

type FileItem = {
  id: number;
  original_name: string;
  s3_key: string;
  size_bytes: number;
  created_at: string;
};

export default function App() {
  const [files, setFiles] = useState<FileItem[]>([]);
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function refresh() {
    const data = await listFiles();
    setFiles(data);
  }

  useEffect(() => {
    refresh().catch((err) => setError(String(err)));
  }, []);

  async function onUpload(e: React.ChangeEvent<HTMLInputElement>) {
    const file = e.target.files?.[0];
    if (!file) return;

    setBusy(true);
    setError(null);
    try {
      await uploadFile(file);
      await refresh();
    } catch (err) {
      setError(String(err));
    } finally {
      setBusy(false);
      e.target.value = "";
    }
  }

  return (
    <div style={{ fontFamily: "sans-serif", padding: 24 }}>
      <h1>3T Sample App</h1>
      <p>Upload a file to S3 and store metadata in Postgres.</p>

      <input type="file" onChange={onUpload} disabled={busy} />
      {busy && <p>Uploading...</p>}
      {error && <p style={{ color: "crimson" }}>{error}</p>}

      <h2>Files</h2>
      <ul>
        {files.map((f) => (
          <li key={f.id}>
            {f.original_name} ({Math.round(f.size_bytes / 1024)} KB)
          </li>
        ))}
      </ul>
    </div>
  );
}
