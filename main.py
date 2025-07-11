import os
import requests
from flask import Flask, request

app = Flask(__name__)

# Obtén el token del entorno
BOT_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_API = f"https://api.telegram.org/bot{BOT_TOKEN}"
print("🔐 Token cargado:", BOT_TOKEN)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()

    # Extrae datos del mensaje
    chat_id = data.get('message', {}).get('chat', {}).get('id')
    user_msg = data.get('message', {}).get('text', "").lower()

    print("📞 chat_id recibido:", chat_id)
    print("📨 Mensaje del usuario:", user_msg)

    # Múltiples condiciones según palabras clave
    if 'precio' in user_msg or 'coste' in user_msg or 'presupuesto' in user_msg:
        response = (
            "Para darte un presupuesto ajustado necesitamos entender y estudiar bien tu caso.\n"
            "¿Te parece si agendamos una videollamada o una llamada para ver exactamente lo que necesitas?"
        )

    elif 'servicio' in user_msg or 'haces' in user_msg or 'ofreces' in user_msg:
        response = (
            "Creamos agentes de voz, asistentes virtuales y automatizaciones "
            "con n8n y Make para empresas que quieren optimizar sus procesos."
        )

    elif 'cita' in user_msg or 'llamar' in user_msg or 'reunión' in user_msg or 'agenda' in user_msg:
        response = (
            "¿Quieres agendar una videollamada para que te expliquemos en detalle?\n"
            "Escríbeme a autenexia@gmail.com o dime qué día y hora te viene bien."
        )

    elif 'automatizar' in user_msg or 'automatizaciones' in user_msg or 'automations' in user_msg:
        response = (
            "Podemos automatizar procesos en múltiples áreas:\n"
            "– Reservas\n"
            "– Atención al cliente\n"
            "– Integración de sistemas\n"
            "– Y más, utilizando n8n, Make y tecnologías personalizadas."
        )

    elif 'n8n' in user_msg:
        response = (
            "n8n es una plataforma potente para crear flujos automatizados y se adapta "
            "perfectamente a tus necesidades de ahorro y optimización."
        )

    elif 'make' in user_msg:
        response = (
            "Make es otra herramienta de automatización que usamos para integrar y optimizar "
            "procesos empresariales complejos de forma visual y sencilla."
        )

    elif 'chatbot' in user_msg or 'asistente virtual' in user_msg:
        response = (
            "Desarrollamos chatbots y asistentes virtuales que mejoran la comunicación y la "
            "atención al cliente, dándole a tu empresa un toque innovador."
        )

    elif 'voz' in user_msg or 'llamada' in user_msg:
        response = (
            "Nuestra tecnología de voz permite gestionar llamadas y respuestas automatizadas "
            "con un nivel profesional, ofreciendo una experiencia de usuario única."
        )

    elif 'asesoramiento' in user_msg:
        response = (
            "Ofrecemos asesoramiento personalizado en automatización y transformación digital.\n"
            "Estamos aquí para ayudarte a crecer y ser más eficiente."
        )

    elif any(frase in user_msg for frase in [
        'nada más', 'eso es todo', 'ya está', 'no necesito más',
        'todo claro', 'no, gracias', 'todo perfecto ya', 'todo entendido',
        'adiós', 'hasta luego', 'me voy', 'nos vemos'
    ]):
        response = "Perfecto. Ha sido un placer ayudarte. 👋"

    else:
        response = (
            "🤖 Hola, soy Paloma, la asistente virtual de AUTENEX AUTOMATIONS IA.\n"
            "Ayudo a empresas como la tuya a automatizar tareas repetitivas con inteligencia artificial.\n"
            "¿Te interesa saber más sobre nuestros Asistentes de Voz, Automatizaciones, CRM, Chatbots o Asesoramiento?"
        )

    # Envía la respuesta al usuario
    url = f"{TELEGRAM_API}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": response
    }

    res = requests.post(url, json=payload)
    print("📤 Respuesta de Telegram:", res.status_code, res.text)

    return "OK"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
