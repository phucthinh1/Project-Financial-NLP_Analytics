from minio import Minio
import json
import io

# 1. Kết nối với MinIO local
client = Minio(
    "localhost:9001",
    access_key="dataNLPmining-lab",
    secret_key="dataNLPmining-lab",
    secure=False # Dùng HTTP vì đang chạy local
)

# 2. Giả lập việc lấy dữ liệu (Trong thực tế, bạn dùng requests.get(url))
crawled_news = {
    "ticker": "FPT",
    "title": "FPT công bố báo cáo tài chính quý 1",
    "content": "Doanh thu tăng trưởng mạnh..."
}

# Chuyển đổi JSON thành dạng bytes để đẩy đi
raw_bytes = json.dumps(crawled_news, ensure_ascii=False).encode('utf-8')

# 3. Đẩy thẳng vào thư mục 'json-news' trong bucket
client.put_object(
    bucket_name="raw-financial-data",
    object_name="json-news/2026-05-30_fpt.json", # Đường dẫn lưu trữ
    data=io.BytesIO(raw_bytes),
    length=len(raw_bytes),
    content_type="application/json"
)

print("Đã lưu tin tức thành công vào MinIO!")