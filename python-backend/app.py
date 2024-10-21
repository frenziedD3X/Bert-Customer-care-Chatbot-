from flask import Flask, request, jsonify
from sentence_transformers import SentenceTransformer, util  # Import SBERT
import json
import torch
from textblob import TextBlob  # Import TextBlob for spelling correction

app = Flask(__name__)

# Load the SBERT model
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# Load the database of intents and responses
with open('database.json', 'r') as f:
    intents = json.load(f)

# Encode the patterns for all intents
intent_encodings = {}
for intent in intents['intents']:
    tag = intent['tag']
    patterns = intent['patterns']
    intent_encodings[tag] = model.encode(patterns, convert_to_tensor=True)

# Function to correct spelling mistakes in the user input
def correct_spelling(user_input):
    blob = TextBlob(user_input)
    corrected_text = str(blob.correct())
    return corrected_text

# Function to predict the tag for a given input sentence using SBERT
# Function to predict the tag for a given input sentence using SBERT
def predict_tag(sentence, threshold=0.5):
    sentence_embedding = model.encode(sentence, convert_to_tensor=True)
    
    max_similarity = -1
    predicted_tag = None

    # Compare the input sentence with all intent patterns
    for tag, encodings in intent_encodings.items():
        cosine_scores = util.pytorch_cos_sim(sentence_embedding, encodings)
        max_score = torch.max(cosine_scores).item()  # Get the highest similarity score
        
        if max_score > max_similarity:
            max_similarity = max_score
            predicted_tag = tag

    # Check if the max similarity is below the threshold
    if max_similarity < threshold:
        return "unknown"  # Return unknown tag if the score is below the threshold

    return predicted_tag


# Function to get the response for the predicted tag
# Function to get the response for the predicted tag
def get_response(predicted_tag):
    if predicted_tag == "unknown":
        return ["Sorry, I didn't understand that. Could you please rephrase?"]

    for intent in intents['intents']:
        if intent['tag'] == predicted_tag:
            return intent['responses']
    return ["Sorry, I don't understand that."]


@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_input = request.json.get('message', '')
        if not user_input:
            return jsonify(response="Please provide a valid input."), 400

        # Correct spelling mistakes in the user input
        corrected_input = correct_spelling(user_input)

        predicted_tag = predict_tag(corrected_input)
        response = get_response(predicted_tag)
        return jsonify(response=response[0], corrected_input=corrected_input)
    except Exception as e:
        return jsonify(response="An error occurred: {}".format(str(e))), 500

if __name__ == '__main__':
    app.run(port=8000, debug=True)
