# Have the function PrimeMover(num) return the numth prime number. The range will be from 1 to 10^4. For example: if num is 16 the output should be 53 as 53 is the 16th prime number.
def PrimeMover(num):

  # code goes here
  number = 2
  list_num = []
  while number > 1 and number < 10000:
    for i in range(2, number):
      if (number % i) == 0:
        break
    else:
      list_num.append(number)
    number += 1
  return list_num[num - 1]

# keep this function call here 
print PrimeMover(raw_input())