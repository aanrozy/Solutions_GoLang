#Have the function SimpleSymbols(str) take the str parameter being passed and determine if it is an acceptable sequence by either returning the string true or false. The str parameter will be composed of + and = symbols with several characters between them (ie. ++d+===+c++==a) and for the string to be true each letter must be surrounded by a + symbol. So the string to the left would be false. The string will not be empty and will have at least one letter.
def SimpleSymbols(strParam):
  import re

  # code goes here
  if re.match('[+][a-zA-Z][+]',strParam) or re.match('[0-9][+][a-zA-Z][+]',strParam):
    return 'true'
  return 'false'

# keep this function call here 
print SimpleSymbols(raw_input())