import sys

from tweepy import OAuthHandler
from tweepy import API
from tweepy import Stream
from tweepy.streaming import StreamListener

from credentials import ACCESS_TOKEN, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET
from datum import Tweet


class Listener(StreamListener):
    def __init__(self, output_file=sys.stdout):
        super(Listener,self).__init__()
        self.output_file = output_file
    def on_status(self, status):
        tweet = Tweet(status.text)
        if not(tweet.isTagged()) or tweet.isRT():
            return None, None
        else:
            print(tweet.format(), file=self.output_file)
    def on_error(self, status_code):
        print(status_code)
        return False

if __name__ == "__main__":
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = API(auth, wait_on_rate_limit=True,
              wait_on_rate_limit_notify=True)

    from argparse import ArgumentParser, FileType
    parser = ArgumentParser()
    parser.add_argument('outfile', nargs='?'
                    , type=FileType('w'), default=sys.stdout)
    args = parser.parse_args()
    
    listener = Listener(output_file=args.outfile)

    stream = Stream(auth=api.auth, listener=listener)
    try:
        print('Start streaming.')
        stream.sample(languages=['en'])
    except KeyboardInterrupt:
        print("Stopped.")
    finally:
        print('Done.')
        stream.disconnect()
        args.outfile.close()
