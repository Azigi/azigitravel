import smtplib

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'azigitravel@gmail.com'
EMAIL_HOST_PASSWORD = 'ibrqztvpgdwnpyue'  # App-specific password

try:
    server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
    server.starttls()
    server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
    server.sendmail(
        from_addr=EMAIL_HOST_USER,
        to_addrs=['azigitravel@gmail.com'],
        msg="Subject: Test Email\n\nThis is a test email from Python."
    )
    print("Email sent successfully!")
    server.quit()
except Exception as e:
    print(f"Error: {e}")
