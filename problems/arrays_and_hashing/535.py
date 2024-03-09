# https://leetcode.com/problems/encode-and-decode-tinyurl/

# Trivial solution
class Codec:

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        # Create an internal list to hold the longURL and use the index of that element as the key to encode it in a tinyURL
        if hasattr(self, "mapping"):
            if not longUrl in self.mapping:
                self.mapping.append(longUrl)
        else:
            self.mapping = [longUrl]
        
        return f"http://tinyurl.com/{len(self.mapping)}"
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        # Get the final index and look it up in the mapping array
        index = shortUrl.split("/")[-1]
        return self.mapping[int(index) - 1]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))