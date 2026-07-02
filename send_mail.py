import smtplib
import ssl
import os
from email.message import EmailMessage


print("NAVER_ID:", os.environ.get("NAVER_ID"))
print("RECEIVER_EMAIL:", os.environ.get("RECEIVER_EMAIL"))

sender = os.environ["NAVER_ID"]
password = os.environ["NAVER_PASSWORD"]
receiver = os.environ["RECEIVER_EMAIL"]

file_path = "data/BD_Maintenance_Log.xlsx"

msg = EmailMessage()

msg["Subject"] = "[BM Maintenance] Weekly Log"
msg["From"] = sender
msg["To"] = receiver

msg.set_content("""
안녕하세요.

BM Maintenance Log 자동 발송 메일입니다.

첨부파일을 확인해 주세요.
""")

with open(file_path, "rb") as f:
    msg.add_attachment(
        f.read(),
        maintype="application",
        subtype="vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        filename="BM_Maintenance_Log.xlsx"
    )

context = ssl.create_default_context()

with smtplib.SMTP("smtp.naver.com", 587) as server:
    server.starttls(context=context)
    server.login(sender, password)
    server.send_message(msg)

print("메일 발송 완료")
