import requests

def consultar_ia(prompt):
    """
    Función para procesar las consultas del usuario hacia la IA.
    Puedes integrar tu API Key o proveedor de IA aquí.
    """
    prompt_lower = prompt.lower()

    if "adivinanza" in prompt_lower:
        return "🧩 **Aquí tienes una adivinanza:**\n\n*Oro parece, plata no es. El que no lo adivine, bien tonto es.* ¿Qué es?\n\n*(Respuesta: El plátano)*"
    elif "relajarme" in prompt_lower:
        return "🌿 **Consejo de relajación:**\n\nToma una respiración profunda sosteniendo el aire por 4 segundos, y exhala lentamente durante 6 segundos. Repítelo 3 veces."
    elif "juegos" in prompt_lower:
        return "🎮 **Juegos disponibles:**\n\n1. Adivinanzas interactivas.\n2. Retos de memoria.\n3. Preguntas de trivia."
    else:
        return f"¡Entendido! Has preguntado: **'{prompt}'**. Estoy aquí para ayudarte a jugar o responder tus dudas."
