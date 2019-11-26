import numpy as np
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

class TweetModel:
    def __init__(self, tweets):
        """
        Tweet data model
        """
        self.encoder = LabelEncoder()
        self.encoder.fit(list("".join(tweets)))
        
        self.vocabulary = self.encoder.classes_
        self.max_length = max([ len(s) for s in tweets])
        
    def prepare(self, tweets):
        X = np.zeros((len(tweets), self.max_length))
        for index, t in enumerate(tweets):
            X[index, :len(t)] = self.encoder.transform(list(t))
        return X

class HashtagModel:
    """Documentation for Hashtag

    """
    def __init__(self, hashtags):
        self.encoder = OneHotEncoder()
        self.encoder.fit([ [h] for l in hashtags for h in l])

        self.labels = self.encoder.categories_[0].tolist()

    def prepare(self, hashtags):
        return self.encoder.transform([ [h[0]] for h in hashtags ]).toarray()

