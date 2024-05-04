import pandas as pd
import tweepy
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
data = pd.read_csv("C:\\Users\\Usuario\\Desktop\\VSC projects\\hey-banco-hack\\Reto-Hey.csv")
# creds
consumer_key = "BpZwzjpsiwQzN9ahF4shzg4cD"
consumer_secret = "aFJqAuXoP7kVsMlQ3wFjMTmITnBccsroUYp34X7w0pYUEAhRYj"
access_token = "1600960659184820226-jQvHlHENX5nTxOU4Wtn8L2HOdM3TFo"
access_token_secret = "AjlRn12RtznvZGryltPsuSYwHqdaFKNYiU4FsZLIKn6kw"
# Aut
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)
