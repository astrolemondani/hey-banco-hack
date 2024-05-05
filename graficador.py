import pandas as pd
import matplotlib.pyplot as plt
from transformers import pipeline

# Load a pre-trained sentiment analysis pipeline
classifier = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

# Load your dataset
df = pd.read_csv("./aaa.csv", encoding="utf-8")

# Define a function to apply sentiment analysis
def get_sentiment(tweet):
    result = classifier(str(tweet))  # Convertir tweet a str
    print(tweet)
    return result[0]['label'], result[0]['score']
    print("Termino de Evaluar")



# Apply sentiment analysis to each tweet
df['result'] = df['tweet'].apply(get_sentiment)
df['sentiment_label'] = df['result'].apply(lambda x: x[0])
df['sentiment_score'] = df['result'].apply(lambda x: x[1])
df.drop('result', axis=1, inplace=True)  # Remove the intermediate column

# Save the results to a new CSV
df.to_csv("./Processed_Tweets_Sentiment.csv", index=False)

# Plotting the sentiment distribution
sentiment_counts = df['sentiment_label'].value_counts()
sentiment_counts.plot(kind='bar')
plt.title('Distribution of Sentiment Ratings')
plt.xlabel('Sentiment Rating')
plt.ylabel('Count')
plt.show()

# Load your processed dataset
df = pd.read_csv("./Processed_Tweets_Sentiment.csv", encoding="utf-8")

# Convert the 'date' column to datetime
df['date'] = pd.to_datetime(df['date'])

# Group by date and sentiment label
sentiment_by_date = df.groupby([df['date'].dt.date, 'sentiment_label']).size().unstack(fill_value=0)

# Plotting the sentiment labels over time
sentiment_by_date.plot(kind='line', marker='o', figsize=(10, 6))
plt.title('Sentiment Labels Over Time')
plt.xlabel('Date')
plt.ylabel('Count')
plt.legend(title='Sentiment Label')
plt.grid(True)
plt.show()

# Group by date and sentiment label
sentiment_by_date = df.groupby([df['date'].dt.date, 'sentiment_label']).size().unstack(fill_value=0)

# Calculate the sum of counts for 1 and 2-star sentiment labels
sum_1_2_star = sentiment_by_date['1 star'].add(sentiment_by_date['2 stars'], fill_value=0)

# Plotting the curve containing counts of 1 and 2-star sentiment labels over time
sum_1_2_star.plot(kind='line', marker='o', color='red', figsize=(10, 6))
plt.title('Counts of 1 and 2-Star Sentiment Labels Over Time')
plt.xlabel('Date')
plt.ylabel('Count')
plt.grid(True)
plt.show()

# Agrupar por mes y sentimiento
sentiment_by_month = df.groupby([df['date'].dt.to_period('M'), 'sentiment_label']).size().unstack(fill_value=0)

# Calcular la suma de las etiquetas de sentimiento de 1 y 2 estrellas
sum_1_2_star_month = sentiment_by_month['1 star'].add(sentiment_by_month['2 stars'], fill_value=0)

# Graficar la curva que contiene los recuentos de las etiquetas de sentimiento de 1 y 2 estrellas a lo largo del tiempo
sum_1_2_star_month.plot(kind='line', marker='o', color='red', figsize=(10, 6))
plt.title('Recuentos de Etiquetas de Sentimiento de 1 y 2 Estrellas a lo Largo del Tiempo')
plt.xlabel('Mes')
plt.ylabel('Recuento')
plt.grid(True)
plt.show()

# Agrupar por mes y sentimiento
sentiment_by_month = df.groupby([df['date'].dt.to_period('M'), 'sentiment_label']).size().unstack(fill_value=0)

# Calcular la suma de las etiquetas de sentimiento de 4 y 5 estrellas
sum_4_5_star_month = sentiment_by_month['4 stars'].add(sentiment_by_month['5 stars'], fill_value=0)

# Graficar la curva que contiene los recuentos de las etiquetas de sentimiento de 4 y 5 estrellas a lo largo del tiempo
sum_4_5_star_month.plot(kind='line', marker='o', color='red', figsize=(10, 6))
plt.title('Recuentos de Etiquetas de Sentimiento de 4 y 5 Estrellas a lo Largo del Tiempo')
plt.xlabel('Mes')
plt.ylabel('Recuento')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
sum_1_2_star_month.plot(kind='line', marker='o', color='red', label='1 and 2 Star Sentiment')
sum_4_5_star_month.plot(kind='line', marker='o', color='green', label='4 and 5 Star Sentiment')
plt.title('Recuentos de Etiquetas de Sentimiento a lo Largo del Tiempo')
plt.xlabel('Mes')
plt.ylabel('Recuento')
plt.legend()
plt.grid(True)
plt.show()