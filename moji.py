import unicodedata

def zen_to_han(s):
  return unicodedata.normalize('NFKC', s)