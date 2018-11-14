class Codec:
    alphabet = 'abcdefghijklmnopqrstuvwxyz' + 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' + '0123456789'
    
    def __init__(self):
        self.code2url = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        while True:
            code = ''.join(random.choice(Codec.alphabet) for _ in range(7))
            if code not in self.code2url:
                self.code2url[code] = longUrl
                break
            else:
                continue
        return 'http://tinyurl.com/' + code
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.code2url[shortUrl[-7:]]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
