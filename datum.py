HASHTAG_EXP = r"\#+([\w_]+[\w\'_\-]*[\w_]+)"
ATMENTION_EXP = r"([@＠][\S]+)"
URL_EXP = r'(https?[\S]*)'
UNKNOWN_CHARS_EXP = r'([^\w\#\s\?\<\>\:,]+)'
RETWEET_EXP = r'rt +'+ ATMENTION_EXP
class Tweet:
    alphabet = "Pabcdefghijklmnopqrstuvwxyz0123456789-,;.!?:~'\"/\\|_@#$%^&*+-=<>()[]{}" 
    # self.alphabet += "BESH" + "L"
    alphabet += "U"    # @ mention
    alphabet += "L"    # URL

    def __init__(self, content):
        self.content = content
        self.flags = re.IGNORECASE
        self.hashtags = re.findall(HASHTAG_EXP, self.content.lower(), flags=self.flags)
    
    def __str__(self):
        return self.content
    
    def clean(self, quantize=False):
        '''
        Cleans the tweet (lower case, characters, etc)
        '''
        result = self.content.lower()
        result = re.sub(HASHTAG_EXP, ' ', result, flags=self.flags)
        result = re.sub(ATMENTION_EXP, ' U ', result, flags=self.flags)
        result = re.sub(URL_EXP, ' L  ', result, flags=self.flags)
        if quantize: result = re.sub(UNKNOWN_CHARS_EXP, ' ', result, flags=self.flags)
        result = re.sub(r'\s+', ' ', result)
        result = result.strip()
        return result

    def isTagged(self):
        """
        Checks whether the tweet contains hashtags
        """
        return bool(self.hashtags)

    def isRT(self):
        """
        Check if it is a retweet
        """
        return re.match(RETWEET_EXP, self.content.lower()) != None

    def format(self, quantize=False):
        """Format tweet content to hashtags and cleaned content pair.
        - Hashtags are separated by comma,
        - the content of the tweet follows the list of hashtags after a tab space,
        - the content of the tweet is processed according to defined regular expressions
        """
        return ','.join(self.hashtags) + '\t' + self.clean(quantize=quantize)

