from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import time
from datasets import load_dataset
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
import base64
from io import BytesIO

app = Flask(__name__)

# Load dataset
print("📥 Loading dataset...")
ds = load_dataset("qasimmunye/kidsillus")
df = pd.DataFrame(ds['train'])

# Check dataset structure
print("\n🔍 Dataset Columns:", df.columns)

# Selecting available columns
df = df[['image', 'text']]  # "image" contains the PIL image object, "text" contains the story

# Splitting dataset
train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

# Tokenizer setup for deep learning
tokenizer = Tokenizer()
tokenizer.fit_on_texts(train_df['text'])
vocab_size = len(tokenizer.word_index) + 1

# TF-IDF and SVM setup
tfidf = TfidfVectorizer(stop_words='english', max_features=5000)
X_train = tfidf.fit_transform(train_df['text'])
y_train = np.arange(len(train_df))
svm_model = SVC(kernel='linear', probability=True)  # Enable probability for multiple matches
svm_model.fit(X_train, y_train)

# Deep Learning Model (LSTM)
def preprocess_input(text):
    return pad_sequences(tokenizer.texts_to_sequences([text]), maxlen=50)

model = Sequential([
    Embedding(input_dim=vocab_size, output_dim=64, input_length=50),
    LSTM(128, dropout=0.2, recurrent_dropout=0.2),
    Dense(len(train_df), activation='softmax')
])
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Function to find multiple matching stories
def match_stories(user_input, top_n=5):  # Return top N matches
    start_time = time.time()
    user_tfidf = tfidf.transform([user_input])
    probabilities = svm_model.predict_proba(user_tfidf)[0]  # Get probabilities for all stories
    top_indices = np.argsort(probabilities)[-top_n:][::-1]  # Get top N indices
    matched_stories = train_df.iloc[top_indices]
    end_time = time.time()
    print(f"\n⏳ Processing Time: {round(end_time - start_time, 4)} seconds")
    return matched_stories, round(end_time - start_time, 4)

# Convert image to base64
def encode_image(image):
    buffer = BytesIO()
    image.save(buffer, format="PNG")
    encoded_image = base64.b64encode(buffer.getvalue()).decode()
    return f"data:image/png;base64,{encoded_image}"

@app.route('/', methods=['GET', 'POST'])
def index():
    stories = []
    processing_time = None

    if request.method == 'POST':
        user_input = request.form['story_input']
        matched_stories, processing_time = match_stories(user_input, top_n=5)  # Get top 5 matches
        for _, row in matched_stories.iterrows():
            story_text = row['text']
            image_data = encode_image(row['image'])
            stories.append({'text': story_text, 'image': image_data})

    return render_template('index.html', stories=stories, processing_time=processing_time)

if __name__ == '__main__':
    app.run(debug=True)