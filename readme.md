# Customer Care Chatbot

Welcome to the Customer Care Chatbot project! This chatbot is designed to assist users by answering queries related to UpToSkills. It leverages a combination of Python, Flask, Node.js, and a DistilBERT model for natural language processing.

## Table of Contents

- [Project Structure](#project-structure)
- [Installation](#installation)
- [Running the Project](#running-the-project)
- [Usage](#usage)
- [Troubleshooting](#troubleshooting)
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
cd chatbot-backend
```

Install the required Node.js packages:

```bash
npm install
```

### Model Setup

Ensure you have the DistilBERT model and tokenizer available in the `customer_care_bert_model/` and `customer_care_bert_tokenizer/` directories, respectively. If they are not available, refer to the model download steps, or reach out to the project administrator for access.

## Running the Project

To run the project, execute the following command in the root directory:

```bash
python run.py
```

### Running the Node.js Server

In the `node-backend` directory, run the following command to start the Node.js server:

```bash
node server.js
```

Ensure both the Flask API and the Node.js server are running before accessing the frontend.

## Usage

Once the server is running, you can access the chatbot through the frontend. Simply open `index.html` in your web browser to start interacting with the chatbot.

## Troubleshooting

### Cloning with Git LFS

If the repository contains large files stored via Git LFS, make sure to install Git LFS and pull the files correctly:

1. Install Git LFS:

   ```bash
   git lfs install
   ```

2. Clone the repository:

   ```bash
   git clone https://github.com/frenziedD3X/Bert-Customer-care-Chatbot-.git
   ```

3. Pull LFS files:

   ```bash
   git lfs pull
   ```

### Common Issues

- **Python Version Mismatch:** Ensure you’re using the correct version of Python (e.g., Python 3.12 or above). If the project uses a newer Python version, upgrade your local Python environment.
- **Missing Dependencies:** Double-check that you’ve installed all required Python and Node.js dependencies using `pip install -r requirements.txt` and `npm install`.

## Contributing

Contributions are welcome! If you have suggestions or improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
```
