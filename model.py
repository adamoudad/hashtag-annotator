# import pickle as pkl
from keras.models import Sequential, load_model
from keras.layers import Embedding, Flatten, Dense

def multilayer_perceptron(input_size, input_length, n_classes):
    """
    Simple character-level MLP for hashtag prediction
    """
    model = Sequential()
    model.add(Embedding(input_size, 64, input_length=input_length))
    model.add(Flatten())
    model.add(Dense(128))
    model.add(Dense(n_classes, activation="softmax"))
    model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])
    return model

# Error : OMP: Info #250: KMP_AFFINITY: pid 20252 tid 20269 thread 1 bound to OS proc set 2
# class MultilayerPerceptron:
#     def __init__(self, character_encoder, hashtag_encoder, max_length, model_path=None):
#         """
#         Simple character-level MLP for hashtag prediction
#         """
#         self.character_encoder = character_encoder
#         self.vocabulary = character_encoder.classes_
#         self.hashtag_encoder = hashtag_encoder
#         self.labels = hashtag_encoder.categories_[0].tolist()
#         self.max_length = max_length

#         if None:
#             self.model = load_model(model_path)
#         else:
#             self.model = Sequential()
#             self.build()
        
#     def build(self):
#         self.model.add(Embedding(len(self.vocabulary), 64, input_length=self.max_length))
#         self.model.add(Flatten())
#         self.model.add(Dense(128))
#         self.model.add(Dense(len(self.labels), activation="softmax"))
#         self.model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])

#     def prepare(self, tweets):
#         X = np.zeros((len(tweets), self.max_length))
#         for index, t in enumerate(tweets):
#             X[index, :len(t)] = self.character_encoder.transform(list(t))
#         return X
        
#     def summary(self, *args, **kwargs):
#         return self.model.summary(*args, **kwargs)
#     def fit(self, *args, **kwargs):
#         return self.model.fit(*args, **kwargs)
#     def predict(self, *args, **kwargs):
#         return self.model.predict(*args, **kwargs)
#     def save(self, path):
#         '''
#         Do not add an extension to the filename in path, because two files will be saved: one for class variables, and another for the actual neural network model
#         '''
#         import pickle
#         with open(path + ".pkl", 'wb') as f:
#             pickle.dump((self.character_encoder
#                          , self.hashtag_encoder
#                          , self.max_length)
#                         , f
#                         , pickle.HIGHEST_PROTOCOL)
#         self.model.save(path + ".h5")

