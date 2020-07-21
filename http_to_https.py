bio_code = '''Hello, world!'''

def force_https(bbcode):
  return bbcode.replace('http://','https://')

print(force_https(bio_code))
