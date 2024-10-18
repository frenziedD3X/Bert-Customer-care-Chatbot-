import os
import json
import torch
import numpy as np
from torch.utils.data import Dataset, DataLoader
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
from torch.optim import AdamW


# Load intents data from the database.json file
with open('database.json', 'r') as f:
    intents = json.load(f)

# Prepare the data
tags = []
xy = []  # A list to hold (pattern, tag) pairs
for intent in intents['intents']:
    tag = intent['tag']
    tags.append(tag)
    for pattern in intent['patterns']:
        xy.append((pattern, tag))

# Initialize DistilBERT tokenizer
tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')

# Tokenize the patterns (inputs) and encode them for BERT
all_patterns = [pattern for pattern, _ in xy]
inputs = tokenizer(all_patterns, padding=True, truncation=True, return_tensors="pt")

# Create labels (tags) by mapping each tag to a numerical index
all_tags = [tags.index(tag) for _, tag in xy]
labels = torch.tensor(all_tags)

# Dataset class for loading data into DataLoader
class ChatDataset(Dataset):
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels

    def __getitem__(self, idx):
        item = {key: val[idx].clone().detach() for key, val in self.encodings.items()}
        item['labels'] = self.labels[idx].clone().detach()
        return item

    def __len__(self):
        return len(self.labels)


# Create a dataset and a data loader
dataset = ChatDataset(inputs, labels)
train_loader = DataLoader(dataset, batch_size=8, shuffle=True)

# Set up device (use GPU if available)
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Load the DistilBERT model for sequence classification
model = DistilBertForSequenceClassification.from_pretrained(
    'distilbert-base-uncased',
    num_labels=len(tags)
).to(device)

# Define the optimizer
optimizer = AdamW(model.parameters(), lr=1e-5)

# Number of epochs for training
num_epochs = 20

# Training loop
for epoch in range(num_epochs):
    epoch_loss = 0.0
    all_labels = []
    all_predicted = []

    model.train()  # Set model to training mode
    for batch in train_loader:
        # Move data to the device (GPU or CPU)
        input_ids = batch['input_ids'].to(device)
        attention_mask = batch['attention_mask'].to(device)
        labels = batch['labels'].to(device)

        # Forward pass
        outputs = model(input_ids, attention_mask=attention_mask, labels=labels)
        loss = outputs.loss
        logits = outputs.logits

        # Backward pass and optimization
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        # Accumulate loss and predictions for accuracy
        epoch_loss += loss.item()
        _, predicted = torch.max(logits, dim=1)
        all_labels.extend(labels.cpu().numpy())
        all_predicted.extend(predicted.cpu().numpy())

    # Calculate average loss and accuracy for the epoch
    avg_epoch_loss = epoch_loss / len(train_loader)
    accuracy = np.mean(np.array(all_labels) == np.array(all_predicted))

    print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {avg_epoch_loss:.4f}, Accuracy: {accuracy:.4f}')

# Save the model and tokenizer for later use
model.save_pretrained("customer_care_bert_model")
tokenizer.save_pretrained("customer_care_bert_tokenizer")

print("Training complete. Model and tokenizer saved.")
