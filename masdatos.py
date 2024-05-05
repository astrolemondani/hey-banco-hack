import pandas as pd
import matplotlib.pyplot as plt
from transformers import pipeline

# Load the pre-trained sentiment analysis pipeline
classifier = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

# Define a function to apply sentiment analysis
def get_sentiment(tweet):
    result = classifier(tweet)
    label_number = int(result[0]['label'].split()[0])  # Extract only the number
    return label_number, result[0]['score']

# Load your existing dataset
df_existing = pd.read_csv("./Dataset5MAYOR.csv", encoding="utf-8")

# Load new dataset with user and tweet information
df_new = pd.read_csv("./Dataset3.csv", encoding="utf-8")
df_new.rename(columns={'tweets': 'tweet'}, inplace=True)

# Apply sentiment analysis if new columns are not already present
if 'sentiment_label' not in df_new.columns or 'sentiment_score' not in df_new.columns:
    df_new['result'] = df_new['tweet'].apply(get_sentiment)
    df_new['sentiment_label'] = df_new['result'].apply(lambda x: x[0])
    df_new['sentiment_score'] = df_new['result'].apply(lambda x: x[1])
    df_new.drop('result', axis=1, inplace=True)

# Append new data to the existing DataFrame
df_combined = pd.concat([df_existing, df_new], ignore_index=True)

# Remove up to 700 entries with a sentiment label of 5
count_label_5 = (df_combined['sentiment_label'] == 5).sum()
if count_label_5 > 700:
    # Get indices of the first 700 entries with label '5'
    indices_to_remove = df_combined[df_combined['sentiment_label'] == 5].index[-700:]
    df_combined = df_combined.drop(indices_to_remove)

# Save the updated dataset
df_combined.to_csv("DATASET800.csv", index=False)

# Plotting the sentiment distribution for the combined data
sentiment_counts = df_combined['sentiment_label'].value_counts()
sentiment_counts.plot(kind='bar')
plt.title('Distribution of Sentiment Ratings After Update')
plt.xlabel('Sentiment Rating')
plt.ylabel('Count')
plt.show()
