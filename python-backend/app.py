from flask import Flask, request, jsonify
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
import json
import torch

app = Flask(__name__)

# Load the trained model and tokenizer
model = DistilBertForSequenceClassification.from_pretrained("customer_care_bert_model")
tokenizer = DistilBertTokenizer.from_pretrained("customer_care_bert_tokenizer")

# Load the database of intents and responses
with open('database.json', 'r') as f:
    intents = json.load(f)

# Set the model to evaluation mode
model.eval()
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model.to(device)

# Function to predict the tag for a given input sentence
def predict_tag(sentence):
    inputs = tokenizer(sentence, padding=True, truncation=True, return_tensors="pt")
    inputs = {key: value.to(device) for key, value in inputs.items()}

    with torch.no_grad():
        outputs = model(**inputs)

    # Get the predicted tag index
    _, predicted = torch.max(outputs.logits, dim=1)
    predicted_tag_index = predicted.item()

    return predicted_tag_index

# Function to get the response for the predicted tag
def get_response(tag_index):
    if tag_index < len(intents['intents']):
        tag = intents['intents'][tag_index]['tag']
        for intent in intents['intents']:
            if intent['tag'] == tag:
                return intent['responses']
    return ["Sorry, I don't understand that."]

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']
    predicted_tag_index = predict_tag(user_input)
    response = get_response(predicted_tag_index)
    return jsonify(response=response[0])

if __name__ == '__main__':
    app.run(port=8000, debug=True)
