# # from fastapi import FastAPI, Query, HTTPException
# # import mysql.connector
# # from mysql.connector import Error
# # import smtplib
# # from email.mime.text import MIMEText
# # from dotenv import load_dotenv
# # import os

# # # Load environment variables
# # load_dotenv()

# # # ENV Variables
# # SMTP_HOST = os.getenv("SMTP_SERVER")
# # SMTP_PORT = int(os.getenv("SMTP_PORT"))
# # SMTP_USER = os.getenv("EMAIL_USER")
# # SMTP_PASS = os.getenv("EMAIL_PASS")
# # BASE_URL = os.getenv("BASE_URL")

# # # DB config
# # db_config = {
# #     "host": os.getenv("DB_HOST"),
# #     "user": os.getenv("DB_USER"),
# #     "password": os.getenv("DB_PASS"),
# #     "database": os.getenv("DB_NAME"),
# # }

# # app = FastAPI()

# # # ---------- SEND EMAIL FUNCTION ----------

# # def send_email(to_email: str, to_name: str = ""):
# #     unsubscribe_url = f"{BASE_URL}/api/unsubscribe?email={to_email}"
# #     subject = "New Opportunities in AI/ML - Join Innovapath"

# #     html_body = f"""
# #     <html>
# #     <body>
# #         <p>Hello {to_name or 'there'},</p>

# #         <p>You were previously associated with <strong>Innovapath</strong>.</p>

# #         <p>We are excited to offer new opportunities in:</p>
# #         <ul>
# #             <li>AI Engineering</li>
# #             <li>Machine Learning</li>
# #             <li>Full-time & W2 Contract roles</li>
# #         </ul>

# #         <p>
# #             <strong>Check it out:</strong> 
# #             <a href="https://www.whitebox-learning.com/" target="_blank">www.whitebox-learning.com</a>
# #         </p>

# #         <p>
# #             If you're interested, feel free to reply or call us directly.
# #         </p>

# #         <hr>
# #         <p style="font-size: 12px; color: #888888;">
# #             If you do not wish to receive these updates, you may 
# #             <a href="{unsubscribe_url}" style="color:#888;">Unsubscribe</a>.
# #         </p>
# #     </body>
# #     </html>
# #     """

# #     msg = MIMEText(html_body, "html")
# #     msg["Subject"] = subject
# #     msg["From"] = f"Innovapath <{SMTP_USER}>"
# #     msg["To"] = to_email

# #     with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
# #         server.starttls()
# #         server.login(SMTP_USER, SMTP_PASS)
# #         server.send_message(msg)

# # # ---------- SEND EMAIL BATCH ----------

# # @app.post("/send-emails")
# # def send_batch_emails():
# #     try:
# #         conn = mysql.connector.connect(**db_config)
# #         cursor = conn.cursor(dictionary=True)

# #         cursor.execute("""
# #             SELECT leadid, name, email FROM leads
# #             WHERE unsubscribe != 'yes' AND email_sent != 'yes'
# #             LIMIT 100
# #         """)
# #         leads = cursor.fetchall()

# #         if not leads:
# #             return {"message": "No new leads to send emails to."}

# #         for lead in leads:
# #             try:
# #                 send_email(lead["email"], lead["name"])
# #                 cursor.execute("""
# #                     UPDATE leads 
# #                     SET email_sent = 'yes' 
# #                     WHERE leadid = %s
# #                 """, (lead["leadid"],))
# #                 print(f"✅ Email sent to {lead['email']}")
# #             except Exception as e:
# #                 print(f"❌ Failed to send to {lead['email']}: {e}")

# #         conn.commit()
# #         return {"message": f"✅ Emails sent to {len(leads)} leads."}

# #     except Error:
# #         raise HTTPException(status_code=500, detail="Database error")
# #     finally:
# #         if cursor: cursor.close()
# #         if conn: conn.close()

# # # ---------- UNSUBSCRIBE API ----------
# # from fastapi.responses import HTMLResponse

# # @app.get("/api/unsubscribe", response_class=HTMLResponse)
# # def unsubscribe(email: str = Query(...)):
# #     try:
# #         conn = mysql.connector.connect(**db_config)
# #         cursor = conn.cursor()
# #         cursor.execute("SELECT unsubscribe FROM leads WHERE email = %s", (email,))
# #         result = cursor.fetchone()

# #         if not result:
# #             return HTMLResponse(content=f"<h3>Email {email} not found.</h3>", status_code=404)

# #         if result[0] == 'yes':
# #             return HTMLResponse(content=f"<h3>Email {email} is already unsubscribed ✅</h3>", status_code=200)

# #         cursor.execute("UPDATE leads SET unsubscribe = 'yes' WHERE email = %s", (email,))
# #         conn.commit()
# #         return HTMLResponse(content=f"<h3>Email {email} has been successfully unsubscribed ❌</h3>", status_code=200)

# #     except Error:
# #         return HTMLResponse(content="<h3>Error occurred while unsubscribing.</h3>", status_code=500)

# #     finally:
# #         if cursor: cursor.close()
# #         if conn: conn.close()
# # import csv
# # from datetime import datetime

# # LOG_FILE = "logs/sent_emails.csv"

# # def log_sent_email(email, name):
# #     timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# #     log_row = [email, name, timestamp]

# #     # Create folder if missing
# #     os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

# #     # Write header only if file doesn't exist
# #     write_header = not os.path.exists(LOG_FILE)

# #     with open(LOG_FILE, "a", newline="") as csvfile:
# #         writer = csv.writer(csvfile)
# #         if write_header:
# #             writer.writerow(["Email", "Name", "Timestamp"])
# #         writer.writerow(log_row)





# from fastapi import FastAPI, Query, HTTPException
# import mysql.connector
# from mysql.connector import Error
# import smtplib
# from email.mime.text import MIMEText
# from dotenv import load_dotenv
# import os

# # Load environment variables
# load_dotenv()

# # ENV Variables
# SMTP_HOST = os.getenv("SMTP_SERVER")
# SMTP_PORT = int(os.getenv("SMTP_PORT"))
# SMTP_USER = os.getenv("EMAIL_USER")
# SMTP_PASS = os.getenv("EMAIL_PASS")
# BASE_URL = os.getenv("BASE_URL")

# # DB config
# db_config = {
#     "host": os.getenv("DB_HOST"),
#     "user": os.getenv("DB_USER"),
#     "password": os.getenv("DB_PASS"),
#     "database": os.getenv("DB_NAME"),
# }

# app = FastAPI()

# # ---------- SEND EMAIL FUNCTION ----------
# def send_email(to_email: str, to_name: str = ""):
#     unsubscribe_url = f"{BASE_URL}/api/unsubscribe?email={to_email}"
#     subject = "New Opportunities in AI/ML - Join Innovapath"
#     html_body = f"""
#     <html>
#     <body>
#         <p>Hello {to_name or 'there'},</p>
#         <p>You were previously associated with <strong>Innovapath</strong>.</p>
#         <p>We are excited to offer new opportunities in:</p>
#         <ul>
#             <li>AI Engineering</li>
#             <li>Machine Learning</li>
#             <li>Full-time & W2 Contract roles</li>
#         </ul>
#         <p>
#             <strong>Check it out:</strong>
#             <a href="https://www.whitebox-learning.com/" target="_blank">www.whitebox-learning.com</a>
#         </p>
#         <p>
#             If you're interested, feel free to reply or call us directly.
#         </p>
#         <hr>
#         <p style="font-size: 12px; color: #888888;">
#             If you do not wish to receive these updates, you may
#             <a href="{unsubscribe_url}" style="color:#888;">Unsubscribe</a>.
#         </p>
#     </body>
#     </html>
#     """
#     msg = MIMEText(html_body, "html")
#     msg["Subject"] = subject
#     msg["From"] = f"Innovapath <{SMTP_USER}>"
#     msg["To"] = to_email

#     with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
#         server.starttls()
#         server.login(SMTP_USER, SMTP_PASS)
#         server.send_message(msg)

# # ---------- SEND EMAIL BATCH ----------
# @app.post("/send-emails")
# def send_batch_emails():
#     try:
#         conn = mysql.connector.connect(**db_config)
#         cursor = conn.cursor(dictionary=True)
#         cursor.execute("""
#             SELECT leadid, name, email FROM leads
#             WHERE unsubscribe != 'yes' AND email_sent != 'yes'
#             LIMIT 100
#         """)
#         leads = cursor.fetchall()
#         if not leads:
#             return {"message": "No new leads to send emails to."}

#         for lead in leads:
#             try:
#                 send_email(lead["email"], lead["name"])
#                 cursor.execute("""
#                     UPDATE leads
#                     SET email_sent = 'yes'
#                     WHERE leadid = %s
#                 """, (lead["leadid"],))
#                 print(f"✅ Email sent to {lead['email']}")
#             except Exception as e:
#                 print(f"❌ Failed to send to {lead['email']}: {e}")

#         conn.commit()
#         return {"message": f"✅ Emails sent to {len(leads)} leads."}
#     except Error:
#         raise HTTPException(status_code=500, detail="Database error")
#     finally:
#         if cursor: cursor.close()
#         if conn: conn.close()

# # ---------- UNSUBSCRIBE API ----------
# from fastapi.responses import HTMLResponse

# @app.get("/api/unsubscribe", response_class=HTMLResponse)
# def unsubscribe(email: str = Query(...)):
#     try:
#         conn = mysql.connector.connect(**db_config)
#         cursor = conn.cursor()
#         cursor.execute("SELECT unsubscribe FROM leads WHERE email = %s", (email,))
#         result = cursor.fetchone()

#         if not result:
#             return HTMLResponse(content=f"<h3>Email {email} not found.</h3>", status_code=404)

#         if result[0] == 'yes':
#             return HTMLResponse(content=f"<h3>Email {email} is already unsubscribed ✅</h3>", status_code=200)

#         cursor.execute("UPDATE leads SET unsubscribe = 'yes' WHERE email = %s", (email,))
#         conn.commit()
#         return HTMLResponse(content=f"<h3>Email {email} has been successfully unsubscribed ❌</h3>", status_code=200)
#     except Error:
#         return HTMLResponse(content="<h3>Error occurred while unsubscribing.</h3>", status_code=500)
#     finally:
#         if cursor: cursor.close()
#         if conn: conn.close()

# # Logging function
# import csv
# from datetime import datetime

# LOG_FILE = "logs/sent_emails.csv"

# def log_sent_email(email, name):
#     timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     log_row = [email, name, timestamp]

#     # Create folder if missing
#     os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

#     # Write header only if file doesn't exist
#     write_header = not os.path.exists(LOG_FILE)
#     with open(LOG_FILE, "a", newline="") as csvfile:
#         writer = csv.writer(csvfile)
#         if write_header:
#             writer.writerow(["Email", "Name", "Timestamp"])
#         writer.writerow(log_row)




from fastapi import FastAPI, Query, HTTPException
from fastapi.responses import HTMLResponse
import mysql.connector
from mysql.connector import Error
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os
import csv
from datetime import datetime

# Load environment variables
load_dotenv()

# SMTP config
SMTP_USER = os.getenv("EMAIL_USER")
SMTP_PASS = os.getenv("EMAIL_PASS")
SMTP_HOST = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT"))
BASE_URL  = os.getenv("BASE_URL")

# DB config
db_config = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASS"),
    "database": os.getenv("DB_NAME"),
}

# Log file path
LOG_FILE = "logs/sent_emails.csv"

app = FastAPI()

# ---------- Log Sent Emails ----------
def log_sent_email(email, name):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    write_header = not os.path.exists(LOG_FILE)
    with open(LOG_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        if write_header:
            writer.writerow(["Email", "Name", "Timestamp"])
        writer.writerow([email, name, timestamp])

# ---------- Send Email ----------
def send_email(to_email: str, to_name: str = ""):
    unsubscribe_url = f"{BASE_URL}/api/unsubscribe?email={to_email}"
    subject = "New Opportunities in AI/ML - Join Innovapath"

    unsubscribe_button = f"""
    <p style="text-align:center; margin-top: 20px;">
        <a href="{unsubscribe_url}"
           style="
                background-color: #d9534f;
                color: white;
                padding: 10px 20px;
                text-decoration: none;
                border-radius: 5px;
                font-weight: bold;
                font-size: 14px;">
            Unsubscribe
        </a>
    </p>
    """

    html_body = f"""
    <html>
    <body>
        <p>Hello {to_name or 'there'},</p>

        <p>You were previously associated with <strong>Innovapath</strong>.</p>

        <p>We are excited to offer new opportunities in:</p>
        <ul>
            <li>AI Engineering</li>
            <li>Machine Learning</li>
            <li>Full-time & W2 Contract roles</li>
        </ul>

        <p>
            <strong>Check it out:</strong>
            <a href="https://www.whitebox-learning.com/" target="_blank">
                www.whitebox-learning.com
            </a>
        </p>

        <p>If you're interested, feel free to reply or call us directly.</p>

        <hr>
        <p style="font-size: 13px; color: #888;">
            Don't want to hear from us again?
        </p>
        {unsubscribe_button}
    </body>
    </html>
    """

    msg = MIMEText(html_body, "html")
    msg["Subject"] = subject
    msg["From"] = f"Innovapath <{SMTP_USER}>"
    msg["To"] = to_email
    msg["List-Unsubscribe"] = f"<{unsubscribe_url}>"

    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USER, SMTP_PASS)
        server.send_message(msg)

# ---------- Route: Send 100 Emails ----------
@app.post("/send-emails")
def send_batch_emails():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)

        cursor.execute("""
            SELECT leadid, name, email FROM leads
            WHERE unsubscribe != 'yes' AND email_sent != 'yes'
            LIMIT 100
        """)
        leads = cursor.fetchall()

        if not leads:
            return {"message": "✅ No leads to send emails to."}

        for lead in leads:
            try:
                send_email(lead["email"], lead["name"])
                cursor.execute("UPDATE leads SET email_sent = 'yes' WHERE leadid = %s", (lead["leadid"],))
                log_sent_email(lead["email"], lead["name"])
                print(f"✅ Email sent to {lead['email']}")
            except Exception as e:
                print(f"❌ Failed to send to {lead['email']}: {e}")

        conn.commit()
        return {"message": f"✅ Emails sent to {len(leads)} leads."}

    except Error as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

    finally:
        if cursor: cursor.close()
        if conn: conn.close()

# ---------- Route: Unsubscribe ----------
@app.get("/api/unsubscribe", response_class=HTMLResponse)
def unsubscribe(email: str = Query(...)):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("SELECT unsubscribe FROM leads WHERE email = %s", (email,))
        result = cursor.fetchone()

        if not result:
            return HTMLResponse(f"<h3>Email {email} not found in our system.</h3>", status_code=404)

        if result[0] == 'yes':
            return HTMLResponse(f"<h3>Email {email} is already unsubscribed ✅</h3>", status_code=200)

        cursor.execute("UPDATE leads SET unsubscribe = 'yes' WHERE email = %s", (email,))
        conn.commit()
        return HTMLResponse(f"<h3>Email {email} has been successfully unsubscribed ❌</h3>", status_code=200)

    except Error:
        return HTMLResponse("<h3>❌ An error occurred while unsubscribing.</h3>", status_code=500)

    finally:
        if cursor: cursor.close()
        if conn: conn.close()
