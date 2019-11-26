import sys

from tweepy import OAuthHandler
from tweepy import API
from tweepy import Stream
from tweepy.streaming import StreamListener

# Replace the "None"s by your own credentials
ACCESS_TOKEN = None
ACCESS_TOKEN_SECRET = None
CONSUMER_KEY = None
CONSUMER_SECRET = None

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = API(auth, wait_on_rate_limit=True,
          wait_on_rate_limit_notify=True)

class Listener(StreamListener):
    def __init__(self, output_file=sys.stdout):
        super(Listener,self).__init__()
        self.output_file = output_file
    def on_status(self, status):
        print(status.text, file=self.output_file)
    def on_error(self, status_code):
        print(status_code)
        return False

output = open('stream_output.txt', 'w')
listener = Listener(output_file=output)

stream = Stream(auth=api.auth, listener=listener)
try:
    print('Start streaming.')
    stream.sample(languages=['en'])
except KeyboardInterrupt:
    print("Stopped.")
finally:
    print('Done.')
    stream.disconnect()
    output.close()
