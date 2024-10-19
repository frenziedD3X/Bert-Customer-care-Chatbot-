Here’s the `README.md` content formatted as it would appear in a Markdown file:

```markdown
# Customer Care Chatbot

Welcome to the Customer Care Chatbot project! This chatbot is designed to assist users by answering queries related to UpToSkills. It leverages a combination of Python, Flask, Node.js, and a DistilBERT model for natural language processing.

## Table of Contents

- [Project Structure](#project-structure)
- [Installation](#installation)
- [Running the Project](#running-the-project)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Structure

```
project-root/
│
├── python-backend/
│   ├── chatbot_api.py            # Flask API for handling requests
│   ├── database.json             # Intents and responses database
│   ├── customer_care_bert_model/ # Directory for the trained BERT model
│   ├── customer_care_bert_tokenizer/ # Directory for the tokenizer
│            
├── node-backend/
│   ├── server.js                  # Node.js server
│   └── package.json               # Node.js dependencies and scripts
│
├── frontend/
│   ├── index.html                 # HTML file for the frontend
│   ├── styles.css                 # CSS file for styling
│   └── script.js                  # JavaScript for handling user input and displaying responses
│
├── run.py                         # Start file for the application
├── requirements.txt               # List of Python dependencies
```

## Installation

### Create a Virtual Environment

To get started, you'll need to create a virtual environment for the Python backend:

```bash
python -m venv venv
```

Activate the virtual environment:

- On macOS/Linux:
    ```bash
    source venv/bin/activate
    ```
- On Windows:
    ```bash
    venv\Scripts\activate
    ```

### Install Required Python Packages

Install the required Python packages by running:

```bash
pip install -r requirements.txt
```

### Set Up Node.js Backend

Navigate to the Node.js backend directory:

```bash
cd node-backend
```

Install the required Node.js packages:

```bash
npm install
```

## Running the Project

To run the project, execute the following command in the root directory:

```bash
python run.py
```

## Usage

Once the server is running, you can access the chatbot through the frontend. Simply open `index.html` in your web browser to start interacting with the chatbot.

## Contributing

Contributions are welcome! If you have suggestions or improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
```

You can copy and paste this directly into your `README.md` file! Let me know if you need any further adjustments.