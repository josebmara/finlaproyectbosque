import streamlit as st
import os

try:
    from ai_engine import consultar_ia
except ImportError:
    def consultar_ia(prompt):
        return f"Respuesta simulada para: '{prompt}'"

st.set_page_config(
    page_title="Nuevo Proyecto - Inspirado en CalmaPlay",
    page_icon="🧘",
    layout="wide"
)

st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #f5f0ff 0%, #e6e6fa 100%);
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    .calma-header {
        text-align: center;
        background: linear-gradient(90deg, #6c5ce7, #a29bfe);
        color: white;
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 10px 25px rgba(108, 92, 231, 0.2);
        margin-bottom: 2rem;
    }

    .stChatMessage {
        background-color: #ffffff;
        border-radius: 15px;
        padding: 1rem;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
        margin-bottom: 0.8rem;
    }

    div.stButton > button {
        background-color: #ffffff;
        color: #6c5ce7;
        border: 2px solid #a29bfe;
        border-radius: 20px;
        font-weight: 600;
        transition: all 0.3s ease;
        width: 100%;
    }

    div.stButton > button:hover {
        background-color: #6c5ce7;
        color: white;
        border-color: #6c5ce7;
        transform: translateY(-2px);
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="calma-header">
        <h1>✨ Tu Nuevo Espacio Interactivo</h1>
        <p>Adivinanzas, juegos y asistente inteligente</p>
    </div>
""", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "¡Hola! 👋 Soy tu asistente interactivo. ¿En qué te puedo ayudar hoy o qué te gustaría jugar?"}
    ]

st.subheader("💡 Preguntas recomendadas:")
col1, col2, col3, col4 = st.columns(4)

preguntas_prehechas = [
    "Dame una adivinanza fácil",
    "¿Cómo puedo relajarme hoy?",
    "Cuéntame un dato curioso",
    "¿Qué juegos hay disponibles?"
]

pregunta_seleccionada = None
with col1:
    if st.button(preguntas_prehechas[0]):
        pregunta_seleccionada = preguntas_prehechas[0]
with col2:
    if st.button(preguntas_prehechas[1]):
        pregunta_seleccionada = preguntas_prehechas[1]
with col3:
    if st.button(preguntas_prehechas[2]):
        pregunta_seleccionada = preguntas_prehechas[2]
with col4:
    if st.button(preguntas_prehechas[3]):
        pregunta_seleccionada = preguntas_prehechas[3]

st.write("---")
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt_usuario = st.chat_input("Escribe tu consulta o juego aquí...")

prompt_final = pregunta_seleccionada if pregunta_seleccionada else prompt_usuario

if prompt_final:
    st.session_state.messages.append({"role": "user", "content": prompt_final})
    with st.chat_message("user"):
        st.markdown(prompt_final)

    with st.chat_message("assistant"):
        with st.spinner("Procesando respuesta..."):
            try:
                respuesta = consultar_ia(prompt_final)
            except Exception as e:
                respuesta = f"Error al conectar con la IA: {str(e)}"

            st.markdown(respuesta)
            st.session_state.messages.append({"role": "assistant", "content": respuesta})

            if pregunta_seleccionada:
                st.rerun()
