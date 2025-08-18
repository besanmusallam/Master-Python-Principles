import smtplib
from email.mime.text import MIMEText

sender_email = "besanzak8@gmail.com"
receiver_email = "oranthuraya@gmail.com"
password = "ruim sjyq oimk gglm"  # or use an app password
message = MIMEText("This is the body of the email.")
message['Subject'] = 'Subject of the email'
message['From'] = sender_email
message['To'] = receiver_email

try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server: # Use SMTP_SSL for Gmail
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
    print("Email sent successfully!")
except Exception as e:
    print(f"An error occurred: {e}")