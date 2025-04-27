import os
import time
import shutil
import smtplib
from datetime import datetime
from email.mime.text import MIMEText
from dotenv import load_dotenv

# Nạp biến môi trường từ file .env
load_dotenv()

SENDER_EMAIL = os.getenv("SENDER_EMAIL")
RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")
APP_PASSWORD = os.getenv("APP_PASSWORD")

# Hàm gửi email thông báo
def send_email(subject, body):
    message = MIMEText(body)
    message["Subject"] = subject
    message["From"] = SENDER_EMAIL
    message["To"] = RECEIVER_EMAIL

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(SENDER_EMAIL, APP_PASSWORD)
            server.send_message(message)
        print(f" Email đã gửi đến {RECEIVER_EMAIL}")
    except Exception as e:
        print(f" Lỗi gửi email: {e}")

# Hàm backup database
def backup_database():
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d_%H%M%S")
    source_folder = r"E:\python\backupdatabase\databases"
    backup_folder = r"E:\python\backupdatabase\backups"
    os.makedirs(backup_folder, exist_ok=True)

    files = [f for f in os.listdir(source_folder) if f.endswith((".sql", ".sqlite3"))]

    if not files:
        subject = "Backup thất bại"
        body = "Không có file .sql hoặc .sqlite3 để backup."
        send_email(subject, body)
        return

    for file in files:
        src = os.path.join(source_folder, file)
        dst = os.path.join(backup_folder, f"{timestamp}_{file}")
        shutil.copy2(src, dst)

    subject = "Backup thành công"
    body = f"Đã backup {len(files)} file lúc {now.strftime('%d/%m/%Y %H:%M:%S')}."
    send_email(subject, body)

#Hàm backup lúc 0h00
def wait_until_midnight():
    while True:
        now = datetime.now()
        if now.hour == 0 and now.minute == 00:
            print(" Đến 00:00, bắt đầu backup!")
            return
        time.sleep(30)  


if __name__ == "__main__":
    while True:
        wait_until_midnight()
        backup_database()
        time.sleep(60) 
