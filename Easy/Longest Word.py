#Have the function LongestWord(sen) take the sen parameter being passed and return the longest word in the string. If there are two or more words that are the same length, return the first word from the string with that length. Ignore punctuation and assume sen will not be empty. Words may also contain numbers, for example "Hello world123 567"
def LongestWord(sen):
  import re

  # code goes here
  sen = re.sub(r'[^\w\s]', '', sen)
  sen = max(sen.split(), key = len)
  return sen

# keep this function call here 
print LongestWord(raw_input())