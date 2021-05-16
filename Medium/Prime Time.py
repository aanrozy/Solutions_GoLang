# Have the function PrimeTime(num) take the num parameter being passed and return the string true if the parameter is a prime number, otherwise return the string false. The range will be between 1 and 2^16.
def PrimeTime(num):

  # code goes here
  if num > 1 and num < (65536):
    for i in range(2, num):
      if (num % i) == 0:
        return 'false'
        break
    return 'true'

# keep this function call here 
print PrimeTime(raw_input())