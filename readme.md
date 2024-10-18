# Customer Care Chatbot

This project is a customer care chatbot built using a combination of Python, Flask, Node.js, and a DistilBERT model for natural language processing. The chatbot is designed to assist users by answering queries related to a specific topic, such as information about UpToSkills.

## Project Structure

project-root/
│
├── python-backend/
│   ├── chatbot_api.py            # Your Flask API
│   ├── database.json             # Your intents and responses database
│   ├── customer_care_bert_model/ # Directory for your trained BERT model
│   ├── customer_care_bert_tokenizer/ # Directory for your tokenizer
│   └── requirements.txt           # List of Python dependencies
│
├── node-backend/
│   ├── server.js                  # Your Node.js server
│   └── package.json               # Node.js dependencies and scripts
│
└── frontend/
    ├── index.html                 # Your HTML file for frontend
    ├── styles.css                 # Your CSS file for styling
    └── script.js                  # JavaScript for handling user input and displaying responses


Create a virtual environment:
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install the required Python packages:
    pip install -r requirements.txt

Node.js Backend
    Navigate to the Node.js backend directory:


    cd chatbot_backend
        Install the required Node.js packages:

        npm install

Running the Project
    in the root directory
    run
    python.exe run.py