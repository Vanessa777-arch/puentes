import streamlit as st

# Título de la aplicación
st.title("Asistente Virtual de Puentes")

# Mensaje de bienvenida
st.write("¡Hola! ¿Qué necesitas saber?")

# Entrada de texto del usuario
pregunta = st.text_input("Escribe tu problema o pregunta:", "")

# Respuesta basada en palabras clave
if pregunta:
    if "bloqueado" in pregunta.lower():
        st.write("Debes ingresar a la pantalla y seleccionar el botón verde.")
    elif "sin energía" in pregunta.lower() or "sin energia" in pregunta.lower():
        st.write("Debes encender el interruptor.")
    elif "sin conexión" in pregunta.lower() or "desconectado" in pregunta.lower():
        st.write("Verifica el cable de conexión o contacta al soporte técnico.")
    else:
        st.write("Comunícate al número +56966233827 para más información.")
