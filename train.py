# Load data
with open("tweets.txt", 'r') as tweets_file, open("hashtags.txt", 'r') as hashtags_file:
    tweets = []
    hashtags = []
    for t, h in zip(tweets_file, hashtags_file):
        tweets.append(t.strip())
        hashtags.append(h.strip().split(","))

# Build models (Data)
from data_model import TweetModel, HashtagModel
tweet_model = TweetModel(tweets)
hashtag_model = HashtagModel(hashtags)

# Build model (Inference)
from model import multilayer_perceptron
model = multilayer_perceptron(len(tweet_model.vocabulary), tweet_model.max_length, len(hashtag_model.labels))

model.summary()
model.fit(tweet_model.prepare(tweets)
          , hashtag_model.prepare(hashtags)
          , batch_size=1
          , epochs=2)

model.save("mlp.h5")
import pickle
with open("tweet_model.pkl", 'wb') as tm, open("hashtag_model.pkl", 'wb') as hm:
    pickle.dump(tweet_model, tm)
    pickle.dump(hashtag_model, hm)
