from flask import Flask, request
import os
import requests

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
TELEGRAM_API = f"https://api.telegram.org/bot{BOT_TOKEN}"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    chat_id = data['message']['chat']['id']
    user_msg = data['message']['text'].lower()

    if 'precio' in user_msg or 'coste' in user_msg:
        response = "En AUTENEX AUTOMATIONS IA no vendemos herramientas, creamos soluciones inteligentes que ahorran tiempo y dinero."
    elif 'servicio' in user_msg or 'haces' in user_msg:
        response = "Creamos agentes de voz, Asistentes Virtuales, Automatizaciones con n8n y Make y muchos mas comandos para empresas que quieren ahorrar tiempo y dinero."
    elif 'cita' in user_msg or 'llamar' in user_msg:
        response = "¿Quieres agendar una videollamada para explicarte todo en detalle? Escríbeme: contacto@autenexai.com o dime qué hora y que día te viene bien."
    else:
        response = "Soy Paloma, la asistente de AUTENEX. ¿Te cuento cómo podemos ayudarte a automatizar tu empresa?"

    requests.post(f"{TELEGRAM_API}/sendMessage", json={
        "chat_id": chat_id,
        "text": response
    })
    return "OK"
    if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
