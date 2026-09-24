# riddles.py - Banco de adivinanzas del proyecto

ADIVINANZAS = [
    {
        "pregunta": "Tengo hojas pero no soy árbol, tengo lomo pero no soy animal. ¿Qué soy?",
        "respuesta": "El libro"
    },
    {
        "pregunta": "Blanco por dentro, verde por fuera. Si quieres que te lo diga, espera.",
        "respuesta": "La pera"
    }
]

def obtener_adivinanza_aleatoria():
    import random
    return random.choice(ADIVINANZAS)
