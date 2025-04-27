#  Backup Database Python Project

##  Mô tả

Project này tự động **backup** các file database có đuôi `.sql` và `.sqlite3` từ thư mục `databases/` sang thư mục `backups/`, và **gửi email thông báo** backup **thành công** hoặc **thất bại** mỗi ngày vào lúc **00:00 AM** (nửa đêm).

---

## Hướng dẫn cài đặt

### 1. Clone project về máy

```bash
git clone https://github.com/Nnhan299/backup_database.git
cd backup_database
```

### 2. Tạo file `.env` trong thư mục gốc với nội dung:

```dotenv
SENDER_EMAIL=your_gmail@gmail.com
SENDER_PASSWORD=your_gmail_app_password
RECEIVER_EMAIL=receiver_email@example.com
```

> **Lưu ý:** Không được push file `.env` chứa thông tin nhạy cảm này lên GitHub.

### 3. Cài đặt thư viện cần thiết

```bash
pip install -r requirements.txt
```

---

##  Cách chạy project

Chạy file Python chính:

```bash
python backupdatabase/baitap.py
```

>  Chương trình sẽ tự động **đợi** đến **00:00 AM** rồi mới bắt đầu backup.

---

## 📂Cấu trúc thư mục

```
backup_database/
├── backups/               # Thư mục chứa file backup (.sql, .sqlite3)
├── databases/             # Thư mục chứa file database gốc
├── backupdatabase/
│──  baitap.py          # File Python thực hiện backup và gửi mail
├── .gitignore             # File cấu hình loại trừ khi push Git
├── requirements.txt       # Danh sách thư viện cần cài
└── README.md              # Tài liệu hướng dẫn (file này)
```

---

##  Các thư viện sử dụng

- `python-dotenv`: Đọc biến môi trường từ file `.env`
- `schedule`: Hẹn giờ chạy tự động theo lịch
- `smtplib` + `email.mime`: Gửi email báo cáo
- `os`, `shutil`, `datetime`: Xử lý file hệ thống

---

##  Một số lưu ý

- Tài khoản Gmail gửi mail cần bật **App Password** và bật cho phép **Less secure apps** (nếu cần).
- Thư mục `databases/` phải có ít nhất 1 file `.sql` hoặc `.sqlite3` để chương trình sao lưu.
- Đừng quên thêm file `.env`, `__pycache__/`, `.vscode/`,... vào file `.gitignore`.
- Nếu cần tạo mới file `requirements.txt`, dùng lệnh:

```bash
pip freeze > requirements.txt
```

---

##  Nội dung file `.gitignore` mẫu

```
# Bỏ file môi trường
.env

# Bỏ thư mục cache của Python
__pycache__/

# Bỏ thiết lập editor
.vscode/
*.code-workspace


##  Tác giả

**Ngô Đức Nhân** - DAU University

---

#  Kết thúc.

# backup_database
