






# import mysql.connector, smtplib, os, csv
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from email.mime.image import MIMEImage
# from dotenv import load_dotenv
# from datetime import datetime

# # Load environment variables
# load_dotenv()

# # SMTP Configuration
# SMTP_USER = os.getenv("EMAIL_USER")
# SMTP_PASS = os.getenv("EMAIL_PASS")
# SMTP_HOST = os.getenv("SMTP_SERVER")
# SMTP_PORT = int(os.getenv("SMTP_PORT"))
# # UNSUBSCRIBE_URL = os.getenv("UNSUBSCRIBE_URL")

# # Database Configuration
# db_config = {
#     "host": os.getenv("DB_HOST"),
#     "user": os.getenv("DB_USER"),
#     "password": os.getenv("DB_PASS"),
#     "database": os.getenv("DB_NAME"),
# }

# # Log file for sent emails
# LOG_FILE = "logs/sent_emails.csv"
# os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

# def log_sent(email, name):
#     with open(LOG_FILE, "a", newline="") as f:
#         writer = csv.writer(f)
#         if f.tell() == 0:
#             writer.writerow(["Email", "Name", "Timestamp"])
#         writer.writerow([email, name, datetime.now().strftime("%Y-%m-%d %H:%M:%S")])

# def send_email(to_email, to_name):
#     subject = f"{to_name or 'Hi'}, explore careers in AI/ML"

#     html_body = f"""
#     <html>
#     <body style="font-family: Arial, sans-serif; font-size: 15px; color: #333; line-height: 1.6; margin: 0; padding: 0; background-color: #f6f8fa;">
#         <div style="max-width: 600px; margin: auto; padding: 20px; background-color: #ffffff; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
            
#             <!-- Header with logo and brand name -->
#             <div style="text-align: center; margin-bottom: 20px;">
#                 <img src="https://www.whitebox-learning.com/_next/static/media/wbl-dark.364b4e0a.png"
#                      alt="Whitebox Learning Logo"
#                      style="height: 50px; display: block; margin: auto;">
#                 <h2 style="margin: 10px 0 0 0; color: #1b1f23;">Whitebox Learning</h2>
#             </div>

#             <p>Hi {to_name or 'there'},</p>

#             <p>We hope you're doing well.</p>

#             <p>At <strong>Whitebox Learning</strong>, we've supported many professionals like you through QA and UI training programs. Now, we’re excited to help professionals transition into <strong>AI/ML careers</strong>.</p>

#             <p>In just the last 1 months, our AI/ML program has helped <strong>3 candidates</strong> become AI Engineers/ML Engineers.</p>

#             <!-- Insert GIF with smaller size -->
#             <div style="text-align: center; margin: 20px 0;">
#                 <img src="cid:promo_gif" alt="AI/ML Journey" style="width: 100%; max-width: 360px; border-radius: 6px;">
#             </div>

#             <!-- New business model -->
#             <p><strong>We have a new business model where we help you secure full-time roles directly with clients instead of contracting through us.</strong></p>

#             <p><strong>Our training covers:</strong></p>
#             <ul>
#                 <li>Classic Machine Learning</li>
#                 <li>MLOps</li>
#                 <li>Generative AI</li>
#             </ul>

#             <p>If you or someone you know is exploring this path, we’d love to help. You can join the program, refer a friend, or reach out with questions.</p>

#             <!-- Bootstrap-style action buttons -->
#             <div style="text-align: center; margin: 25px 0;">
#                 <a href="https://www.whitebox-learning.com/signup" target="_blank" style="background-color:#0d6efd; color:#fff; padding:10px 20px; text-decoration:none; border-radius:5px; display:inline-block; margin:5px;">🔗 Learn More</a>
#                 <a href="tel:+19255571053" style="background-color:#198754; color:#fff; padding:10px 20px; text-decoration:none; border-radius:5px; display:inline-block; margin:5px;">📞 Call Us</a>
#                 <a href="mailto:recruiting@whitebox-learning.com" style="background-color:#6f42c1; color:#fff; padding:10px 20px; text-decoration:none; border-radius:5px; display:inline-block; margin:5px;">📧 Email Our Team</a>
#             </div>

#             <p>Thanks for being part of our journey.<br>We’re here to support your next career step.</p>

#             <p style="margin-bottom: 0;">
#                 Warm regards,<br>
#                 <strong>Whitebox Learning Team</strong><br>
#                 <a href="https://www.whitebox-learning.com">whitebox-learning.com</a>
#             </p>

#             <!-- Social Media Buttons -->
#             <div style="text-align: center; margin-top: 30px;">
#                 <a href="https://www.facebook.com/WBLAIML" target="_blank" style="background-color:#3b5998; color:#fff; padding:8px 16px; text-decoration:none; border-radius:5px; display:inline-block; margin:5px;">
#                     <img src="https://cdn-icons-png.flaticon.com/24/145/145802.png" alt="Facebook" style="height: 18px; vertical-align: middle; margin-right: 6px;"> Facebook
#                 </a>
#                 <a href="https://www.linkedin.com/company/107532599/admin/dashboard/" target="_blank" style="background-color:#0077b5; color:#fff; padding:8px 16px; text-decoration:none; border-radius:5px; display:inline-block; margin:5px;">
#                     <img src="https://cdn-icons-png.flaticon.com/24/145/145807.png" alt="LinkedIn" style="height: 18px; vertical-align: middle; margin-right: 6px;"> LinkedIn
#                 </a>
#             </div>

#             <hr style="margin-top: 30px; border: none; border-top: 1px solid #ddd;">
#             <p style="font-size: 12px; color: #888; text-align: center;">
#                 Don’t want to hear from us again? 
#                 <a href="https://whitebox-learning.com/leads_unsubscribe?email={to_email}" style="color:#888;">Unsubscribe</a>
#             </p>
#         </div>
#     </body>
#     </html>
#     """

#     msg = MIMEMultipart("related")
#     msg["Subject"] = subject
#     msg["From"] = f"Whitebox Learning <{SMTP_USER}>"
#     msg["To"] = to_email

#     msg_alternative = MIMEMultipart("alternative")
#     msg.attach(msg_alternative)
#     msg_alternative.attach(MIMEText(html_body, "html"))

#     # Attach the GIF inline
#     with open("vid-min.gif", "rb") as f:
#         gif = MIMEImage(f.read(), _subtype="gif")
#         gif.add_header("Content-ID", "<promo_gif>")
#         gif.add_header("Content-Disposition", "inline", filename="vid-min.gif")
#         msg.attach(gif)

#     with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
#         server.starttls()
#         server.login(SMTP_USER, SMTP_PASS)
#         server.send_message(msg)

# def run():
#     conn = mysql.connector.connect(**db_config)
#     cursor = conn.cursor(dictionary=True)
#     cursor.execute("""
#         SELECT leadid, name, email FROM leads
#         WHERE massemail_unsubscribe != 'yes' AND massemail_email_sent != 'yes'
#         LIMIT 100
#     """)
#     leads = cursor.fetchall()
#     if not leads:
#         print("✅ No emails to send.")
#         return

#     for lead in leads:
#         try:
#             send_email(lead["email"], lead["name"])
#             cursor.execute("UPDATE leads SET massemail_email_sent = 'yes' WHERE leadid = %s", (lead["leadid"],))
#             log_sent(lead["email"], lead["name"])
#             print(f"✅ Sent to {lead['email']}")
#         except Exception as e:
#             print(f"❌ Failed to send to {lead['email']}: {e}")

#     conn.commit()
#     cursor.close()
#     conn.close()

# if __name__ == "__main__":
#     run()



















import mysql.connector, smtplib, os, csv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables
load_dotenv()

# SMTP Configuration
SMTP_USER = os.getenv("EMAIL_USER")
SMTP_PASS = os.getenv("EMAIL_PASS")
SMTP_HOST = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT"))
REPLY_TO_EMAIL = os.getenv("REPLY_TO_EMAIL")

# Database Configuration
db_config = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASS"),
    "database": os.getenv("DB_NAME"),
}

# Log file for sent emails
LOG_FILE = "logs/sent_emails.csv"
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

def log_sent(email, name):
    with open(LOG_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        if f.tell() == 0:
            writer.writerow(["Email", "Name", "Timestamp"])
        writer.writerow([email, name, datetime.now().strftime("%Y-%m-%d %H:%M:%S")])

def send_email(to_email, to_name):
    subject = f"{to_name or 'Hi'}, explore careers in AI/ML"

    html_body = f"""
    <html>
    <body style="font-family: Arial, sans-serif; font-size: 15px; color: #333; line-height: 1.6; margin: 0; padding: 0; background-color: #f6f8fa;">
        <div style="max-width: 600px; margin: auto; padding: 20px; background-color: #ffffff; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
            <div style="text-align: center; margin-bottom: 20px;">
                <img src="https://www.whitebox-learning.com/_next/static/media/wbl-dark.364b4e0a.png"
                     alt="Whitebox Learning Logo"
                     style="height: 50px; display: block; margin: auto;">
                <h2 style="margin: 10px 0 0 0; color: #1b1f23;">Whitebox Learning</h2>
            </div>

            <p>Hi {to_name or 'there'},</p>

            <p>We hope you're doing well.</p>

            <p>At <strong>Whitebox Learning</strong>, we've supported many professionals like you through QA and UI training programs. Now, we’re excited to help professionals transition into <strong>AI/ML careers</strong>.</p>

            <p>In just the last 1 months, our AI/ML program has helped <strong>3 candidates</strong> become AI Engineers / ML Engineers.</p>

            <div style="text-align: center; margin: 20px 0;">
                <img src="cid:promo_gif" alt="AI/ML Journey" style="width: 100%; max-width: 360px; border-radius: 6px;">
            </div>

            <p><strong>We have a new business model where we help you secure full-time roles directly with clients instead of contracting through us.</strong></p>

            <p><strong>Our training covers:</strong></p>
            <ul>
                <li>Classic Machine Learning</li>
                <li>MLOps</li>
                <li>Generative AI</li>
            </ul>

            <p>If you or someone you know is exploring this path, we’d love to help. You can join the program, refer a friend, or reach out with questions.</p>

            <div style="text-align: center; margin: 25px 0;">
                <a href="https://www.whitebox-learning.com/signup" target="_blank" style="background-color:#0d6efd; color:#fff; padding:10px 20px; text-decoration:none; border-radius:5px; display:inline-block; margin:5px;">🔗 Learn More</a>
                <a href="tel:+19255571053" style="background-color:#198754; color:#fff; padding:10px 20px; text-decoration:none; border-radius:5px; display:inline-block; margin:5px;">📞 Call Us</a>
                <a href="mailto:recruiting@whitebox-learning.com" style="background-color:#6f42c1; color:#fff; padding:10px 20px; text-decoration:none; border-radius:5px; display:inline-block; margin:5px;">📧 Email Our Team</a>
            </div>

            <p>Thanks for being part of our journey.<br>We’re here to support your next career step.</p>

            <p style="margin-bottom: 0;">
                Warm regards,<br>
                <strong>Whitebox Learning Team</strong><br>
                <a href="https://www.whitebox-learning.com">whitebox-learning.com</a>
            </p>

            <div style="text-align: center; margin-top: 30px;">
                <a href="https://www.facebook.com/WBLAIML" target="_blank" style="background-color:#3b5998; color:#fff; padding:8px 16px; text-decoration:none; border-radius:5px; display:inline-block; margin:5px;">
                    <img src="https://cdn-icons-png.flaticon.com/24/145/145802.png" alt="Facebook" style="height: 18px; vertical-align: middle; margin-right: 6px;"> Facebook
                </a>
                <a href="https://www.linkedin.com/company/107532599/admin/dashboard/" target="_blank" style="background-color:#0077b5; color:#fff; padding:8px 16px; text-decoration:none; border-radius:5px; display:inline-block; margin:5px;">
                    <img src="https://cdn-icons-png.flaticon.com/24/145/145807.png" alt="LinkedIn" style="height: 18px; vertical-align: middle; margin-right: 6px;"> LinkedIn
                </a>
            </div>

            <hr style="margin-top: 30px; border: none; border-top: 1px solid #ddd;">
            <p style="font-size: 12px; color: #888; text-align: center;">
                Don’t want to hear from us again? 
                <a href="https://www.whitebox-learning.com/leads_unsubscribe?email={to_email}" style="color:#888;">Unsubscribe</a>
            </p>
        </div>
    </body>
    </html>
    """

    msg = MIMEMultipart("related")
    msg["Subject"] = subject
    msg["From"] = f"Whitebox Learning <{SMTP_USER}>"
    msg["To"] = to_email
    msg["Reply-To"] = REPLY_TO_EMAIL  # Ensures replies go to the recruiting team

    msg_alternative = MIMEMultipart("alternative")
    msg.attach(msg_alternative)
    msg_alternative.attach(MIMEText(html_body, "html"))

    # Attach the GIF inline
    with open("vid-min.gif", "rb") as f:
        gif = MIMEImage(f.read(), _subtype="gif")
        gif.add_header("Content-ID", "<promo_gif>")
        gif.add_header("Content-Disposition", "inline", filename="vid-min.gif")
        msg.attach(gif)

    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USER, SMTP_PASS)
        server.send_message(msg)

def run():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT leadid, name, email FROM leads
        WHERE massemail_unsubscribe != 'yes' AND massemail_email_sent != 'yes'
        LIMIT 100
    """)
    leads = cursor.fetchall()
    if not leads:
        print("✅ No emails to send.")
        return

    for lead in leads:
        try:
            send_email(lead["email"], lead["name"])
            cursor.execute("UPDATE leads SET massemail_email_sent = 'yes' WHERE leadid = %s", (lead["leadid"],))
            log_sent(lead["email"], lead["name"])
            print(f"✅ Sent to {lead['email']}")
        except Exception as e:
            print(f"❌ Failed to send to {lead['email']}: {e}")

    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    run()
