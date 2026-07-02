import smtplib
import ssl
import os
from email.message import EmailMessage

sender = os.environ["NAVER_ID"]
password = os.environ["NAVER_PASSWORD"]
receiver = os.environ["RECEIVER_EMAIL"]

msg = EmailMessage()

msg["Subject"] = "[KPI] 자동 발송"
msg["From"] = sender
msg["To"] = receiver

msg.set_content("""
안녕하세요.

GitHub에 있는 KPI 파일을 자동 발송합니다.
""")

with open("KPI_Data.xlsx", "rb") as f:
    msg.add_attachment(
        f.read(),
        maintype="application",
        subtype="vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        filename="KPI_Data.xlsx"
    )

context = ssl.create_default_context()

with smtplib.SMTP("smtp.naver.com", 587) as server:
    server.starttls(context=context)
    server.login(sender, password)
    server.send_message(msg)

print("메일 발송 완료")
