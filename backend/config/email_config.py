import os
from dotenv import load_dotenv
from typing import Dict
from email.message import EmailMessage
import smtplib

load_dotenv()

SMTP_SERVER="smtp.gmail.com" 
SMTP_PORT= 465
EMAIL= os.getenv("EMAIL_USER")
PASSWORD= os.getenv("EMAIL_PASS")

def send_anomaly_email(to_email: str, anomaly: Dict):
  subject= "LOG ANOMALY DETECTED!"

  body=f"""
  Anomaly detected in System Logs

 Time Window : {anomaly['timestamp']}
 Error Count : {anomaly['error_count']}
 Z-Score     : {round(anomaly['z_score'], 2)}

 Please investigate immediately.

 Regards,
 Log Monitoring System
 """
  msg = EmailMessage()
  msg["Subject"] = subject
  msg["From"] = EMAIL
  msg["To"] = to_email

  msg.set_content(body)

  with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
    server.login(EMAIL, PASSWORD)
    server.send_message(msg)