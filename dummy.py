# from itsdangerous import URLSafeTimedSerializer, BadSignature, SignatureExpired
# import time

# SECRET_KEY = "my_secret_key"
# SALT = "email-confirmation"

# serializer = URLSafeTimedSerializer(SECRET_KEY)

# # Generate a token
# token = serializer.dumps({"user_id": 1}, salt=SALT)
# print(f"Generated Token: {token}")

# # Simulate token expiry (wait for 35 seconds)
# time.sleep(35)  # Token expire hone ka wait karte hain

# # Try decoding the token
# try:
#     data = serializer.loads(token, salt=SALT, max_age=30)  # Token expiry: 30 sec
#     print(f"Decoded Data: {data}")  # Agar token valid hai toh yeh chalega
# except SignatureExpired:
#     print("❌ Error: Token has expired!")  # Expired token ka handling
# except BadSignature:
#     print("❌ Error: Invalid token!")  # Agar token modify kiya gaya hai



import os
from dotenv import load_dotenv

# Load .env file
# load_dotenv()
# email=os.getenv('EMAIL_USER')
# passw=os.getenv('EMAIl_PASS')
# print(email,passw)
# import smtplib

# try:
#     server = smtplib.SMTP("smtp.gmail.com", 587)
#     server.starttls()  # Upgrade to secure connection
#     server.login(email,passw)
#     print("✅ SMTP Connection Successful!")
#     server.quit()
# except Exception as e:
#     print(f"❌ Error: {e}")
