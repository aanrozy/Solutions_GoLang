#Have the function VowelCount(str) take the str string parameter being passed and return the number of vowels the string contains (ie. "All cows eat grass and moo" would return 8). Do not count y as a vowel for this challenge.
def VowelCount(strParam):

  # code goes here
  count, vowels = 0, 'aAeEiIoOuU'
  for i in strParam:
    if i in vowels:
      count += 1
  return count

# keep this function call here 
print VowelCount(raw_input())