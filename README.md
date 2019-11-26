# Hashtag annotator for Twitter #
Automatically annotates tweets with hashtags, if tweet is similar to other tweets annotated with the same hashtags.

# Scripts and pipeline #
The pipeline in short is download data > train models > annotate tweet.
- `python download.py` to stream and download tweets into `tweets.txt` and `hashtags.txt`
- `python train.py`  to train the neural network. It will save the data models and neural network model into `tweet_model.pkl`, `hashtag_model.pkl`, `model.h5 `
- `python tag.py --tweet "TWEET CONTENT"`will annotate a tweet using pretrained models

# About #
This repository reimplements some of the code I used for my Master thesis *Character-level Convolutional Neural Networks with Gated Recurrent Unit for Twitter Hashtag Prediction* (2017).

For more information, please feel free to  reach me, `my username`@gmail.com
