from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import os

app = Flask(__name__)

@app.route("/whatsapp", methods=['POST'])
def whatsapp():
    resp = MessagingResponse()
    msg = resp.message()
    msg.body("Pizza $10\nHamburguesa $8")
    return str(resp)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
