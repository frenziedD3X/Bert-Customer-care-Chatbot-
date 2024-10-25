class Chatbox {
    constructor() {
        this.args = {
            openButton: document.querySelector('.chatbox__button'),
            chatBox: document.querySelector('.chatbox__support'),
            sendButton: document.getElementById('send-button')
        };

        this.state = false;
        this.messages = [];
        this.predefinedPrompts = [
            "Hello! How can I assist you today?",
            "Free Internships",
            "Where is UptoSkills located?",
            "What is Learn To Earn?",
            "What courses are available?"
        ];
    }

    display() {
        const { openButton, chatBox, sendButton } = this.args;

        openButton.addEventListener('click', () => this.toggleState(chatBox));
        sendButton.addEventListener('click', () => this.onSendButton(chatBox));

        const node = chatBox.querySelector('#user-input');
        node.addEventListener("keyup", ({ key }) => {
            if (key === "Enter") {
                this.onSendButton(chatBox);
            }
        });
    }

    toggleState(chatbox) {
        this.state = !this.state;

        if (this.state) {
            chatbox.classList.add('chatbox--active');
            if (this.messages.length === 0) {
                this.displayInitialPrompts(chatbox);
            }
        } else {
            chatbox.classList.remove('chatbox--active');
        }
    }

    displayInitialPrompts(chatbox) {
        this.predefinedPrompts.forEach(prompt => {
            this.messages.push({ name: "CUTM BOT", message: prompt });
        });
        this.updateChatText(chatbox);
    }

    async onSendButton(chatbox) {
        const textField = chatbox.querySelector('#user-input');
        const userInput = textField.value;

        if (userInput === "") return;

        this.messages.push({ name: "User", message: userInput });
        this.updateChatText(chatbox);
        textField.value = '';

        const loadingIndicator = chatbox.querySelector('.loading');
        loadingIndicator.style.display = 'block';

        try {
            const response = await fetch('http://127.0.0.1:8000/api/chat', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ message: userInput }),
            });
            const data = await response.json();
            this.typingEffect(data.response, chatbox);
        } catch (error) {
            console.error('Error:', error);
        } finally {
            loadingIndicator.style.display = 'none';
        }
    }

    typingEffect(message, chatbox) {
        const msg2 = { name: "CUTM BOT", message: "" };
        this.messages.push(msg2);
        this.updateChatText(chatbox);

        let index = 0;
        const interval = setInterval(() => {
            if (index < message.length) {
                msg2.message += message.charAt(index);
                index++;
                this.updateChatText(chatbox);
            } else {
                clearInterval(interval);
            }
        }, 50); // Adjust the typing speed (in milliseconds)
    }

    updateChatText(chatbox) {
        const chatMessages = chatbox.querySelector('.chatbox__messages');
        chatMessages.innerHTML = this.messages.map(item => `
            <div class="messages__item ${item.name === "User" ? "messages__item--operator" : "messages__item--visitor"}">
                ${item.message}
            </div>
        `).join('');
        chatMessages.scrollTop = chatMessages.scrollHeight; // Auto scroll to the bottom
    }
}

const chatbox = new Chatbox();
chatbox.display();
