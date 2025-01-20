from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request

# Configuración de Twilio
account_sid = 'TU_ACCOUNT_SID'  # Reemplaza con tu Account SID
auth_token = 'TU_AUTH_TOKEN'    # Reemplaza con tu Auth Token
client = Client(account_sid, auth_token)

# Crear una aplicación Flask
app = Flask(__name__)

@app.route("/whatsapp", methods=['POST'])
def whatsapp_reply():
    incoming_msg = request.values.get('Body', '').lower()

    # Crear respuesta
    response = MessagingResponse()
    msg = response.message()

    # Responder al saludo inicial
    if incoming_msg == 'hola':
        msg.body("Hola, ¿cómo estás? En qué puedo ayudarte?\nEste es nuestro menú:\n1. ¿Cuál es la capital de Chile?\n2. ¿Cuál es la capital de Colombia?")
    elif incoming_msg == '1':
        msg.body("La capital de Chile es Santiago.")
    elif incoming_msg == '2':
        msg.body("La capital de Colombia es Bogotá.")
    else:
        msg.body("Lo siento, no entiendo esa opción. Por favor selecciona 1 o 2.")

    return str(response)

if __name__ == "__main__":
    app.run(debug=True)