from pprint import pprint

def chat_interface(app):
    """
    Interfaz de chat para interactuar con el workflow.
    
    Args:
        app: La aplicación compilada del workflow.
    """
    print("Bienvenido al asistente de preguntas. Escribe tu pregunta o 'salir' para terminar.")
    
    while True:
        # Solicitar entrada del usuario
        question = input("\nPregunta: ")
        
        # Salir del loop si el usuario escribe 'salir'
        if question.lower() in ["salir", "exit", "quit"]:
            print("Cerrando el asistente. ¡Hasta pronto!")
            break
        
        # Crear el estado inicial
        inputs = {"question": question}
        
        try:
            # Ejecutar el flujo de trabajo
            for output in app.stream(inputs):
                for key, value in output.items():
                    # Imprimir información del nodo actual
                    pprint(f"Procesando nodo '{key}'...")
            # Mostrar la respuesta final
            pprint("\nRespuesta final:")
            pprint(value["final_response"])
        except Exception as e:
            print(f"Error: {e}")
            continue

# Ejecutar la interfaz de chat
chat_interface(app)
