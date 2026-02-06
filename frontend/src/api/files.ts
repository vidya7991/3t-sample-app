import { request } from "./client";

export async function listFiles() {
  return request<Array<{ id: number; original_name: string; s3_key: string; size_bytes: number; created_at: string }>>("/files");
}

export async function uploadFile(file: File) {
  const form = new FormData();
  form.append("file", file);
  return request<{ id: number }>("/files", {
    method: "POST",
    body: form
  });
}
