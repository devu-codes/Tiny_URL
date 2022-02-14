
"""
Key: Short URL
Value: Long URL
Key: random variable length alphabetic suffix[tinyurl.com/tgwxyz]
"""
import random
import string

d = {}

def getShortURL(longURL):
    # length variable between 6-10
    l = random.randint(6, 10)
    print(l)
    # generate random characters into a string l
    char = string.ascii_lowercase
    seq = [random.choice(char) for i in range(l)]
    shortURL = ''.join(seq)
    print(shortURL)

    # Check if it's already present in dictionary
    if shortURL in d:
        return getShortURL(longURL)
    else:
        d[shortURL] = longURL

    print(d)
    url = 'https://www.shortURL.com/' + shortURL
    return url


# Print Long URL
def getLongURL(shortURL):
    # extract ky from https://www.shortURL.com/tfeplol --->tfeplol
    k = shortURL[25:]
    print(k)
    if k in d:
        return d[k]
    return None:

print(getShortURL('www.devansh.com'))