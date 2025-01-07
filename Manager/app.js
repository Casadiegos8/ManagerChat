// app.js

// Referencias a elementos del DOM
const messagesContainer = document.getElementById('messages');
const selectedMessageField = document.getElementById('selectedMessage');
const responseField = document.getElementById('response');
const responseForm = document.getElementById('responseForm');

// Simulación de mensajes y operadores (esto será sustituido por el backend)
let messages = [
    { id: 1, content: "¿Tienen paracetamol disponible?", operator: null },
    { id: 2, content: "¿Cuánto cuesta la vitamina C?", operator: null },
    { id: 3, content: "Necesito un jarabe para la tos, ¿pueden ayudarme?", operator: null }
];

let selectedMessage = null;

// Renderizar mensajes en el contenedor
function renderMessages() {
    messagesContainer.innerHTML = '';
    messages.forEach(message => {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message');
        messageDiv.textContent = message.content;
        messageDiv.onclick = () => selectMessage(message);
        messagesContainer.appendChild(messageDiv);
    });
}

// Seleccionar un mensaje para responder
function selectMessage(message) {
    selectedMessage = message;
    selectedMessageField.value = message.content;
    responseField.value = '';
}

// Manejar el envío de la respuesta
responseForm.addEventListener('submit', (e) => {
    e.preventDefault();
    if (!selectedMessage) {
        alert('Selecciona un mensaje primero.');
        return;
    }

    const response = responseField.value.trim();
    if (response === '') {
        alert('Escribe una respuesta.');
        return;
    }

    // Aquí enviaríamos la respuesta al backend
    console.log(`Respuesta enviada al mensaje ID ${selectedMessage.id}: ${response}`);

    // Marcar mensaje como respondido (en la simulación lo eliminamos de la lista)
    messages = messages.filter(msg => msg.id !== selectedMessage.id);
    selectedMessage = null;
    selectedMessageField.value = '';
    renderMessages();
});

// Inicializar la aplicación
renderMessages();
