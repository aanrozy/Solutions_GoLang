# Have the function ExOh(str) take the str parameter being passed and return the string true if there is an equal number of x's and o's, otherwise return the string false. Only these two letters will be entered in the string, no punctuation or numbers. For example: if str is "xooxxxxooxo" then the output should return false because there are 6 x's and 5 o's.
def ExOh(strParam):

  # code goes here
  x, o = 0, 0
  for i in range(len(strParam)):
    if strParam[i] == 'x':
      x += 1
    elif strParam[i] == 'o':
      o += 1
  if x == o:
    return 'true'
  return 'false'

# keep this function call here 
print ExOh(raw_input())