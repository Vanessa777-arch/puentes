import streamlit as st

st.title("Asistente Virtual")
import streamlit as st

# Título de la aplicación
st.title("Asistente Virtual")

# Mensaje de bienvenida
st.write("¡Bienvenido, humano! ¿Qué deseas hacer hoy?")

# Opciones para el usuario
opcion = st.radio("Elige una opción:", ["Contar una historia", "Contar un chiste"])

# Respuesta según la opción elegida
if opcion == "Contar una historia":
    st.subheader("Aquí va una historia:")
    st.write(
        """
        Había una vez un programador que siempre olvidaba cerrar los paréntesis.
        Un día, mientras trabajaba en un código importante, dejó un paréntesis sin cerrar y...
        su programa se cayó al infinito.
        Moraleja: ¡Siempre cierra tus paréntesis! 😄
        """
    )
elif opcion == "Contar un chiste":
    st.subheader("Aquí tienes un chiste:")
    st.write(
        """
        ¿Por qué los desarrolladores nunca se pierden?  
        Porque siempre tienen su "ruta" bien definida. 😂
        """
    )
