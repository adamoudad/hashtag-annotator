import numpy as np

def tag(tweet, tweet_model, hashtag_model, model):
    x = tweet_model.prepare([tweet])
    prediction = model.predict(x)
    return hashtag_model.encoder.categories_[0][np.argmax(prediction)]

if __name__ == "__main__":
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('--model', type=str)
    parser.add_argument('--tweet', type=str)
    args = parser.parse_args()

    import pickle
    from keras.models import load_model
    with open("tweet_model.pkl", 'rb') as tm, open("hashtag_model.pkl", 'rb') as hm:
        tweet_model = pickle.load(tm)
        hashtag_model = pickle.load(hm)
    model = load_model("mlp.h5")

    print(tag(args.tweet, tweet_model, hashtag_model, model))

