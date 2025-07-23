from flask import Flask, request, jsonify
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

@app.route('/api/send_email', methods=['POST'])
def send_email():
    data = request.json
    recipient = data.get("soiamrai88@gmail.com")

    if not recipient:
        return jsonify({"error": "Missing 'to' field"}), 400

    sender = "soyamrai18@gmail.com"
    password = "stsm ssyb dush fxxw"

    msg = EmailMessage()
    msg['Subject'] = "Test from Vercel API"
    msg['From'] = sender
    msg['To'] = recipient
    msg.set_content("Hi Soyam sent this email from a Vercel Python API!")

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(sender, password)
            smtp.send_message(msg)

        return jsonify({"success": True, "message": "Email sent!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
