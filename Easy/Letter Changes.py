#Have the function LetterChanges(str) take the str parameter being passed and modify it using the following algorithm. Replace every letter in the string with the letter following it in the alphabet (ie. c becomes d, z becomes a). Then capitalize every vowel in this new string (a, e, i, o, u) and finally return this modified string.
def LetterChanges(strParam):
  
  # code goes here
  letter = ''
  for i in strParam:
    changes = chr(ord(i) + 1) if i.isalpha() else i
    if changes in ['a','e','i','o','u']:
      changes = changes.upper()
    letter += changes
  return letter

# keep this function call here 
print LetterChanges(raw_input())