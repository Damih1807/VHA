import os

def upload_file(upload_dir, filename):
    os.makedirs(upload_dir, exist_ok=True)
    file_path = os.path.join(upload_dir, filename)

    if os.path.exists(file_path):
        print(f"File đã tồn tại: {file_path}")
        return file_path

    # Giả lập upload file nếu cần
    with open(file_path, "wb") as f:
        f.write(b"demo content")

    print(f"Đã upload: {file_path}")
    return file_path
