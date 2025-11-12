from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import os

app = Flask(__name__)

MENU = "*Bienvenido*\n1 Productos\n2 Horarios\n3 Pedir\n4 Contacto"
PRODUCTOS = "Pizza $10\nHamburguesa $8"
HORARIOS = "Lun-Vie: 12h-22h"
CONTACTO = "+54 9 11 1234-5678"

@app.route('/whatsapp', methods=['POST'])
def whatsapp():
    resp = MessagingResponse()
    msg = resp.message()
    texto = request.values.get('Body', '').strip().lower()

    if texto in ['1', 'productos']: msg.body(PRODUCTOS)
    elif texto in ['2', 'horarios']: msg.body(HORARIOS)
    elif texto in ['3', 'pedir']: msg.body("¿Qué deseas?")
    elif texto in ['4', 'contacto']: msg.body(CONTACTO)
    else: msg.body(MENU)

    return str(resp)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
