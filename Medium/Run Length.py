# Have the function RunLength(str) take the str parameter being passed and return a compressed version of the string using the Run-length encoding algorithm. This algorithm works by taking the occurrence of each repeating character and outputting that number along with a single character of the repeating sequence. For example: "wwwggopp" would return 3w2g1o2p. The string will not contain any numbers, punctuation, or symbols.
def RunLength(strParam):
  import re

  # code goes here
  i, word = 0, ''
  imp = re.sub('[0-9][^\w\s]', '', strParam)
  while i < len(imp):
    count = 1
    while i + 1 < len(imp) and imp[i] == imp[i + 1]:
      count += 1
      i += 1
    word += str(count) + imp[i]
    i += 1
  return word

# keep this function call here 
print RunLength(raw_input())