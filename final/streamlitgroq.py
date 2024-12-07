import streamlit as st
from pprint import pprint

# Título de la aplicación
st.title("Asistente de Preguntas Basado en LangChain")

# Área para el chat
st.header("Chat Asistente")

# Estado de la conversación
if "conversation" not in st.session_state:
    st.session_state.conversation = []

# Función para manejar el flujo
def process_question(question, app):
    """
    Procesa la pregunta a través del flujo y devuelve la respuesta final.
    Args:
        question (str): Pregunta del usuario.
        app: Aplicación del flujo de trabajo.
    Returns:
        str: Respuesta generada por el grafo.
    """
    inputs = {"question": question}
    try:
        for output in app.stream(inputs):
            for key, value in output.items():
                # Puedes imprimir los nodos procesados si es necesario
                pass
        # Devuelve la respuesta final
        return value["final_response"]
    except Exception as e:
        return f"Error al procesar la pregunta: {e}"

# Entrada de usuario
user_input = st.text_input("Escribe tu pregunta:", key="user_input")

# Si el usuario envía una pregunta
if st.button("Enviar"):
    if user_input:
        # Procesar la pregunta a través del grafo
        response = process_question(user_input, app)
        
        # Almacenar el intercambio en la conversación
        st.session_state.conversation.append({"user": user_input, "assistant": response})
        
        # Limpiar el input del usuario
        st.session_state.user_input = ""

# Mostrar la conversación
for exchange in st.session_state.conversation:
    st.markdown(f"**Usuario:** {exchange['user']}")
    st.markdown(f"**Asistente:** {exchange['assistant']}")
    st.markdown("---")

# Instrucciones adicionales
st.info("Escribe tu pregunta en el campo de texto y presiona 'Enviar'. Escribe 'salir' para reiniciar la conversación.")
