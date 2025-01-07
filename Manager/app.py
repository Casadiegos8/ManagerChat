from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulación de almacenamiento de mensajes y operadores
messages = [
    {"id": 1, "content": "¿Tienen paracetamol disponible?", "operator": None},
    {"id": 2, "content": "¿Cuánto cuesta la vitamina C?", "operator": None},
    {"id": 3, "content": "Necesito un jarabe para la tos, ¿pueden ayudarme?", "operator": None}
]

operators = [
    {"id": 1, "name": "Operador 1", "assigned_messages": []},
    {"id": 2, "name": "Operador 2", "assigned_messages": []}
]

# Ruta para obtener los mensajes pendientes
@app.route('/messages', methods=['GET'])
def get_messages():
    return jsonify(messages)

# Ruta para asignar un mensaje a un operador
@app.route('/assign_message', methods=['POST'])
def assign_message():
    data = request.get_json()
    message_id = data.get('message_id')
    operator_id = data.get('operator_id')

    # Buscar mensaje y operador
    message = next((msg for msg in messages if msg['id'] == message_id), None)
    operator = next((op for op in operators if op['id'] == operator_id), None)

    if not message or not operator:
        return jsonify({"error": "Mensaje u operador no encontrado"}), 404

    # Asignar mensaje al operador
    operator['assigned_messages'].append(message)
    message['operator'] = operator['id']

    return jsonify({"message": "Mensaje asignado correctamente", "operator": operator})

# Ruta para responder a un mensaje
@app.route('/respond_message', methods=['POST'])
def respond_message():
    data = request.get_json()
    message_id = data.get('message_id')
    response_content = data.get('response')

    # Buscar mensaje
    message = next((msg for msg in messages if msg['id'] == message_id), None)

    if not message:
        return jsonify({"error": "Mensaje no encontrado"}), 404

    # Simulación de guardar respuesta (en un entorno real se guardaría en una base de datos)
    messages.remove(message)
    return jsonify({"message": "Respuesta enviada", "response": response_content})

if __name__ == '__main__':
    app.run(debug=True)
