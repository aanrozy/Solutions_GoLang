#Have the function LetterCapitalize(str) take the str parameter being passed and capitalize the first letter of each word. Words will be separated by only one space.
def LetterCapitalize(strParam):

  # code goes here
  word = strParam.split()
  strParam = ''
  for i in word:
    strParam = strParam + ' ' + i.capitalize()
  return strParam

# keep this function call here 
print LetterCapitalize(raw_input())